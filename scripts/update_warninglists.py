#!/usr/bin/env python3
"""Generate a searchable MISP warning-list catalogue (Python 3.9+, standard library only)."""

import argparse
import html
import json
import math
from pathlib import Path
import re
import subprocess
import tarfile
import tempfile
from urllib.parse import quote
from urllib.request import Request, urlopen

REPOSITORY = 'https://github.com/MISP/misp-warninglists'
LIMIT = 256 * 1024 * 1024
TOTAL_LIMIT = 512 * 1024 * 1024
EXAMPLES = 5


def fetch(url, timeout, target):
    """Bound downloads and stream archives to disk instead of retaining them in memory."""
    with urlopen(Request(url, headers={'User-Agent': 'MISP-warninglist-catalog/1.0'}), timeout=timeout) as response:
        if not response.geturl().startswith('https://'):
            raise ValueError('Source redirected away from HTTPS')
        total = 0
        while True:
            chunk = response.read(1024 * 1024)
            if not chunk:
                break
            total += len(chunk)
            if total > LIMIT:
                raise ValueError('Download exceeds 256 MiB')
            target.write(chunk)


def read_definition(stream, filename):
    raw = stream.read(LIMIT + 1)
    if len(raw) > LIMIT:
        raise ValueError(f'{filename}: definition exceeds 256 MiB')
    definition = json.loads(raw.decode('utf-8-sig'))
    if not isinstance(definition, dict):
        raise ValueError(f'{filename}: definition must be an object')
    for key in ('name', 'description', 'type'):
        if not isinstance(definition.get(key), str) or not definition[key].strip():
            raise ValueError(f'{filename}: missing or invalid {key}')
    version = definition.get('version')
    if type(version) is not int or version < 0:
        raise ValueError(f'{filename}: invalid version')
    entries = definition.get('list')
    if not isinstance(entries, list) or not all(isinstance(entry, str) for entry in entries):
        raise ValueError(f'{filename}: list must contain strings')
    attributes = definition.get('matching_attributes', ['ALL'])
    if not isinstance(attributes, list) or not attributes or not all(isinstance(a, str) and a.strip() for a in attributes):
        raise ValueError(f'{filename}: invalid matching_attributes')
    if 'category' in definition and (not isinstance(definition['category'], str) or not definition['category'].strip()):
        raise ValueError(f'{filename}: invalid category')
    # Keep the published catalogue small even for lists containing millions of entries.
    metadata = {key: value for key, value in definition.items() if key != 'list'}
    return {'metadata': metadata, 'entry_count': len(entries), 'examples': entries[:EXAMPLES],
            'matching_attributes': attributes}


def read_archive(path):
    records = {}
    total = 0
    prefix = None
    with tarfile.open(path, mode='r:gz') as archive:
        for member in archive:
            name = member.name.removeprefix('./')
            match = re.fullmatch(r'((?:[^/]+/)?)(lists/([^/]+)/list\.json)', name)
            if not match:
                continue
            if not member.isfile() or any(part in ('.', '..') for part in name.split('/')):
                raise ValueError(f'Invalid archive definition path: {name}')
            if prefix is None:
                prefix = match[1]
            if prefix != match[1] or match[2] in records:
                raise ValueError('Archive has mixed roots or duplicate definitions')
            total += member.size
            if member.size > LIMIT or total > TOTAL_LIMIT:
                raise ValueError('Archive definitions exceed size limits')
            with archive.extractfile(member) as stream:
                records[match[2]] = read_definition(stream, name)
    return records


def load_source(source=None, ref='main', timeout=30):
    revision = None
    if source:
        root = Path(source)
        if not root.is_dir():
            return read_archive(root), revision
        records = {}
        total = 0
        for path in sorted(root.glob('lists/*/list.json')):
            total += path.stat().st_size
            if total > TOTAL_LIMIT:
                raise ValueError('Definitions exceed 512 MiB')
            with path.open('rb') as stream:
                records[path.relative_to(root).as_posix()] = read_definition(stream, str(path))
        if (root / '.git').exists():
            changed = subprocess.check_output(['git', '-C', str(root), 'status', '--porcelain', '--', 'lists'], text=True)
            if not changed:
                revision = subprocess.check_output(['git', '-C', str(root), 'rev-parse', 'HEAD'], text=True).strip()
        elif (root / 'REVISION').is_file():
            revision = (root / 'REVISION').read_text(encoding='utf-8').strip()
        return records, revision
    with tempfile.TemporaryFile() as response:
        fetch('https://api.github.com/repos/MISP/misp-warninglists/commits/' + quote(ref, safe=''), timeout, response)
        response.seek(0)
        revision = json.load(response)['sha']
    if not isinstance(revision, str) or not re.fullmatch('[0-9a-f]{40}', revision):
        raise ValueError('Invalid upstream revision')
    with tempfile.NamedTemporaryFile(suffix='.tar.gz') as archive:
        fetch('https://codeload.github.com/MISP/misp-warninglists/tar.gz/' + revision, timeout, archive)
        archive.flush()
        return read_archive(archive.name), revision


def catalog(records, revision):
    if revision is not None and (not isinstance(revision, str) or not re.fullmatch('[0-9a-f]{40}', revision)):
        raise ValueError('Revision must be a full commit SHA')
    if not records:
        raise ValueError('No warning lists found; expected lists/*/list.json')
    lists = []
    for path, record in sorted(records.items()):
        slug = path.split('/')[1]
        links = {}
        if revision:
            encoded_path = quote(path, safe='/')
            links = {'source': REPOSITORY + '/blob/' + revision + '/' + encoded_path,
                     'json': 'https://raw.githubusercontent.com/MISP/misp-warninglists/' + revision + '/' + encoded_path}
        lists.append({'id': slug, **record, **links})
    lists.sort(key=lambda item: (item['metadata']['name'].casefold(), item['id']))
    return {'repository': REPOSITORY, 'revision': revision, 'count': len(lists),
            'entry_count': sum(item['entry_count'] for item in lists), 'warninglists': lists}


def escape(value):
    return html.escape(str(value), quote=True).replace('{', '&#123;').replace('}', '&#125;')


def render(data):
    e = escape
    lists = data['warninglists']
    types = sorted({item['metadata']['type'] for item in lists})
    attributes = sorted({attribute for item in lists for attribute in item['matching_attributes']})
    parts = ['<!-- Generated by scripts/update_warninglists.py; do not edit. -->',
             '<section class="warninglist-catalog" aria-label="MISP warning-list catalogue">',
             '<div class="warninglist-toolbar" hidden><label>Search warning lists<input type="search" class="warninglist-search" placeholder="Name, description, attribute type…"></label>',
             '<label>Match type<select class="warninglist-type"><option value="">All match types</option>']
    for kind in types:
        count = sum(item['metadata']['type'] == kind for item in lists)
        parts.append(f'<option value="{e(kind)}">{e(kind)} ({count})</option>')
    parts.append('</select></label><label>Attribute type<select class="warninglist-attribute"><option value="">All attribute types</option>')
    parts.extend(f'<option value="{e(attribute)}">{e(attribute)}</option>' for attribute in attributes)
    parts.extend(['</select></label><button type="button" class="warninglist-reset">Reset</button></div>',
                  f'<p class="warninglist-count" role="status" aria-live="polite">{data["count"]} warning lists · {data["entry_count"]:,} entries across lists</p>',
                  '<noscript><p>All warning lists are shown. Enable JavaScript to search and filter.</p></noscript>',
                  '<div class="warninglist-grid">'])
    for item in lists:
        info = item['metadata']
        search = json.dumps([item['id'], info], ensure_ascii=False, sort_keys=True)
        attrs = json.dumps(item['matching_attributes'], ensure_ascii=False)
        parts.extend([f'<article class="warninglist-card" id="warninglist-{e(item["id"])}" data-type="{e(info["type"])}" data-attributes="{e(attrs)}" data-search="{e(search)}">',
                      f'<span class="warninglist-badge">{e(info["type"])}{(" · " + e(info["category"])) if info.get("category") else ""}</span>',
                      f'<h2>{e(info["name"])}</h2><code>{e(item["id"])}</code>',
                      f'<p class="warninglist-description">{e(info["description"])}</p>',
                      f'<p class="warninglist-stats"><strong>{item["entry_count"]:,}</strong> entries · version {info["version"]}</p>',
                      '<details><summary>List details</summary><dl>',
                      '<dt>Matching attributes</dt><dd>' + e(', '.join(item['matching_attributes'])) + '</dd>'])
        for key, value in sorted(info.items()):
            if key in ('name', 'description', 'type', 'version', 'matching_attributes', 'category'):
                continue
            display = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False, sort_keys=True)
            parts.append(f'<dt>{e(key.replace("_", " ").title())}</dt><dd>{e(display)}</dd>')
        parts.append('</dl>')
        if item['examples']:
            parts.append(f'<p>First {len(item["examples"])} entries</p><ul class="warninglist-examples">')
            parts.extend(f'<li><code>{e(value)}</code></li>' for value in item['examples'])
            parts.append('</ul>')
        else:
            parts.append('<p>This list has no entries.</p>')
        parts.append('</details>')
        if item.get('source'):
            parts.append(f'<div class="warninglist-links"><a href="{e(item["source"])}">View source<span class="warninglist-sr-only"> for {e(info["name"])}</span></a><a href="{e(item["json"])}">Full JSON<span class="warninglist-sr-only"> for {e(info["name"])}</span></a></div>')
        parts.append('</article>')
    parts.extend(['</div><p class="warninglist-empty" hidden>No warning lists match your search. Try fewer terms or reset the filters.</p>',
                  f'<p class="warninglist-provenance">Generated from <a href="{REPOSITORY}">misp-warninglists</a>' +
                  (f' · revision <a href="{REPOSITORY}/commit/{data["revision"]}">{data["revision"][:12]}</a>' if data['revision'] else ' · local snapshot (upstream links omitted)') +
                  '. Entry counts include duplicates across lists.</p></section>'])
    return '\n'.join(parts) + '\n'


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or path.read_text(encoding='utf-8') != text:
        path.write_text(text, encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', help='Offline checkout or repository .tar.gz archive')
    parser.add_argument('--ref', default='main', help='Upstream branch, tag or commit')
    parser.add_argument('--timeout', type=float, default=30)
    parser.add_argument('--website-root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output', type=Path, help='Standalone preview directory')
    args = parser.parse_args()
    try:
        if not math.isfinite(args.timeout) or args.timeout <= 0:
            raise ValueError('Timeout must be positive and finite')
        data = catalog(*load_source(args.source, args.ref, args.timeout))
        body = render(data)
        raw = json.dumps(data, ensure_ascii=False, sort_keys=True, indent=2) + '\n'
        assets = Path(__file__).resolve().parents[1] / 'static'
        if args.output:
            css = (assets / 'css/warninglist-catalog.css').read_text(encoding='utf-8')
            js = (assets / 'js/warninglist-catalog.js').read_text(encoding='utf-8')
            preview = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>MISP warning lists</title><style>body{font-family:system-ui;margin:0 auto;padding:32px;max-width:1200px;color:#183549}' + css + '</style></head><body><main><h1>MISP warning lists</h1><p>Explore lists of indicators that may be known, benign, or potential false positives.</p><p><a href="warninglists.json">Download catalogue metadata</a></p>' + body + '</main><script>' + js + '</script></body></html>'
            write(args.output / 'warninglists.html', preview)
            write(args.output / 'warninglists.json', raw)
        else:
            write(args.website_root / 'layouts/shortcodes/warninglist-catalog.html', '<link rel="stylesheet" href="{{ "css/warninglist-catalog.css" | relURL }}">\n' + body + '<script src="{{ "js/warninglist-catalog.js" | relURL }}" defer></script>\n')
            write(args.website_root / 'static/data/warninglists.json', raw)
        print(f'Generated {data["count"]} warning lists ({data["revision"] or "local snapshot"})')
    except (ValueError, OSError, KeyError, tarfile.TarError, subprocess.SubprocessError) as error:
        parser.exit(1, f'Error: {error}\n')


if __name__ == '__main__':
    main()
