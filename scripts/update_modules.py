#!/usr/bin/env python3
"""Generate the MISP module catalogue without importing upstream code (Python 3.9+)."""
import argparse
import ast
import io
import json
from pathlib import Path
import re
import subprocess
import sys
import tarfile
from urllib.parse import quote
from urllib.request import Request, urlopen

REPO = 'https://github.com/MISP/misp-modules'
GROUPS = {'expansion': 'Expansion', 'import_mod': 'Import', 'export_mod': 'Export', 'action_mod': 'Action'}
LIMIT = 64 * 1024 * 1024


def fetch(url, timeout):
    with urlopen(Request(url, headers={'User-Agent': 'MISP-module-catalog/1.0'}), timeout=timeout) as response:
        if not response.geturl().startswith('https://'):
            raise ValueError('Source redirected away from HTTPS')
        raw = response.read(LIMIT + 1)
    if len(raw) > LIMIT:
        raise ValueError('Source exceeds 64 MiB')
    return raw


def load_source(source=None, ref='main', timeout=30):
    revision = None
    if source:
        root = Path(source)
        if root.is_dir():
            paths = sorted((root / 'misp_modules/modules').glob('*/*.py'))
            paths += sorted((root / 'misp_modules/lib').glob('*.py'))
            files = {p.relative_to(root).as_posix(): p.read_text(encoding='utf-8') for p in paths}
            logos = {p.name for p in (root / 'documentation/logos').glob('*') if p.is_file()}
            if (root / 'REVISION').is_file():
                revision = (root / 'REVISION').read_text().strip()
            elif (root / '.git').exists():
                revision = subprocess.check_output(['git', '-C', str(root), 'rev-parse', 'HEAD'], text=True).strip()
                if subprocess.check_output(['git', '-C', str(root), 'status', '--porcelain', '--', 'misp_modules/modules', 'misp_modules/lib', 'documentation/logos'], text=True):
                    revision = None
            return files, logos, revision
        raw = root.read_bytes()
    else:
        revision = json.loads(fetch('https://api.github.com/repos/MISP/misp-modules/commits/' + quote(ref, safe=''), timeout))['sha']
        if not re.fullmatch('[0-9a-f]{40}', revision):
            raise ValueError('Invalid upstream revision')
        raw = fetch('https://codeload.github.com/MISP/misp-modules/tar.gz/' + revision, timeout)
    if len(raw) > LIMIT:
        raise ValueError('Archive exceeds 64 MiB')
    files, logos, total = {}, set(), 0
    with tarfile.open(fileobj=io.BytesIO(raw), mode='r:gz') as archive:
        for member in archive:
            if not member.isfile():
                continue
            path = member.name.removeprefix('./')
            match = re.fullmatch(r'(?:[^/]+/)?(misp_modules/modules/[^/]+/[^/]+\.py|misp_modules/lib/[^/]+\.py|documentation/logos/[^/]+)', path)
            if not match:
                continue
            if '..' in path.split('/'):
                raise ValueError('Unsafe archive path')
            key = match[1]
            total += member.size
            if total > LIMIT:
                raise ValueError('Archive metadata exceeds 64 MiB')
            if key.startswith('documentation/'):
                logos.add(key.rsplit('/', 1)[1])
            else:
                if key in files:
                    raise ValueError('Duplicate module path')
                files[key] = archive.extractfile(member).read().decode('utf-8-sig')
    return files, logos, revision


def literal(node, constants, functions=None):
    """Evaluate a small data-only AST subset; no arbitrary calls or attributes."""
    def read(value):
        return literal(value, constants, functions)

    if isinstance(node, ast.Name) and node.id in constants:
        return constants[node.id]
    if isinstance(node, ast.List):
        return [read(x) for x in node.elts]
    if isinstance(node, ast.Tuple):
        return tuple(read(x) for x in node.elts)
    if isinstance(node, ast.Dict) and all(k is not None for k in node.keys):
        return {read(k): read(v) for k, v in zip(node.keys, node.values)}
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        left, right = read(node.left), read(node.right)
        if type(left) == type(right) and isinstance(left, (str, list, tuple)):
            return left + right
    if isinstance(node, ast.JoinedStr):
        chunks = []
        for part in node.values:
            if isinstance(part, ast.Constant) and isinstance(part.value, str):
                chunks.append(part.value)
            elif isinstance(part, ast.FormattedValue) and part.conversion == -1 and part.format_spec is None:
                value = read(part.value)
                if not isinstance(value, (str, int, float)):
                    raise ValueError('Unsupported format value')
                chunks.append(str(value))
            else:
                raise ValueError('Unsupported formatted string')
        return ''.join(chunks)
    if isinstance(node, ast.Call) and not node.keywords:
        function = (functions or {}).get(ast.unparse(node.func))
        if function is not None:
            parameters, result = function
            if len(node.args) != len(parameters):
                raise ValueError('Invalid metadata helper arguments')
            return literal(result, dict(zip(parameters, (read(arg) for arg in node.args))))
        if isinstance(node.func, ast.Name) and node.func.id == 'list' and len(node.args) == 1:
            return list(read(node.args[0]))
        if isinstance(node.func, ast.Attribute) and node.func.attr == 'keys' and not node.args:
            value = read(node.func.value)
            if isinstance(value, dict):
                return list(value)
        if isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name) and node.func.value.id == 'dict' and node.func.attr == 'fromkeys' and len(node.args) == 1:
            return dict.fromkeys(read(node.args[0]))
    return ast.literal_eval(node)


def metadata_helpers(tree, files):
    """Read imported lib helpers consisting only of a dictionary return expression."""
    functions = {}
    for node in tree.body:
        if not isinstance(node, ast.ImportFrom) or node.level or not node.module:
            continue
        for alias in node.names:
            if node.module == 'misp_modules.lib':
                module, selected = node.module + '.' + alias.name, None
            elif node.module.startswith('misp_modules.lib.'):
                module, selected = node.module, alias.name
            else:
                continue
            source = files.get(module.replace('.', '/') + '.py')
            if source is None:
                continue
            for function in ast.parse(source, filename=module).body:
                if not isinstance(function, ast.FunctionDef) or function.decorator_list:
                    continue
                body = function.body
                if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant) and isinstance(body[0].value.value, str):
                    body = body[1:]
                args = function.args
                if (len(body) != 1 or not isinstance(body[0], ast.Return) or not isinstance(body[0].value, ast.Dict)
                        or args.defaults or args.kwonlyargs or args.vararg or args.kwarg):
                    continue
                if selected is not None and selected != function.name:
                    continue
                name = alias.asname or alias.name
                key = name if selected else name + '.' + function.name
                functions[key] = ([arg.arg for arg in args.posonlyargs + args.args], body[0].value)
    return functions


def metadata(source, filename, files=None):
    """Read top-level data declarations. Never eval or import modules."""
    constants = {}
    unresolved = set()
    tree = ast.parse(source, filename=filename)
    functions = metadata_helpers(tree, files or {})
    for node in tree.body:
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            for target in targets:
                if isinstance(target, ast.Name):
                    try:
                        constants[target.id] = literal(node.value, constants, functions)
                        unresolved.discard(target.id)
                    except (ValueError, TypeError, KeyError):
                        constants.pop(target.id, None)
                        unresolved.add(target.id)
    if 'moduleinfo' in unresolved:
        raise ValueError(f'{filename}: non-literal moduleinfo')
    info = constants.get('moduleinfo')
    if info is None:
        for function in tree.body:
            if isinstance(function, ast.FunctionDef) and function.name == 'version':
                returns = [n for n in function.body if isinstance(n, ast.Return)]
                if len(returns) == 1 and isinstance(returns[0].value, ast.Name):
                    info = constants.get(returns[0].value.id)
    if not isinstance(info, dict):
        raise ValueError(f'{filename}: missing moduleinfo')
    for field in ('name', 'description', 'logo'):
        if field in info and not isinstance(info[field], str):
            raise ValueError(f'{filename}: invalid {field}')
    attributes = constants.get('mispattributes', constants.get('MISP_ATTRIBUTES', {}))
    if 'mispattributes' in unresolved:
        attributes = {'note': 'Input/output attributes are computed dynamically; see source.'}
    if not isinstance(attributes, dict):
        raise ValueError(f'{filename}: invalid mispattributes')
    return info, attributes


def catalog(files, logos, revision):
    if revision is not None and not re.fullmatch('[0-9a-f]{40}', revision):
        raise ValueError('Revision must be a full commit SHA')
    modules = []
    for path, source in sorted(files.items()):
        parts = path.split('/')
        group, filename = parts[-2:]
        if group not in GROUPS or filename.startswith('_'):
            continue
        info, attributes = metadata(source, path, files)
        slug = filename[:-3]
        logo = info.get('logo', '')
        if logo and (Path(logo).name != logo or logo not in logos):
            logo = ''
        modules.append({'id': group + '/' + slug, 'slug': slug, 'category': group,
                        'name': info.get('name') or slug, 'description': info.get('description') or 'See source for module details.',
                        'metadata': info, 'attributes': attributes,
                        'source': REPO + '/blob/' + (revision or 'main') + '/' + path,
                        'logo': ('https://raw.githubusercontent.com/MISP/misp-modules/' + revision + '/documentation/logos/' + quote(logo)) if logo and revision else ''})
    if not modules:
        raise ValueError('No modules found')
    modules.sort(key=lambda m: (m['name'].casefold(), m['id']))
    return {'repository': REPO, 'revision': revision, 'count': len(modules), 'modules': modules}


def escape(value):
    import html
    return html.escape(str(value), quote=True).replace('{', '&#123;').replace('}', '&#125;')


def render(data):
    e = escape
    counts = {key: sum(m['category'] == key for m in data['modules']) for key in GROUPS}
    parts = ['<!-- Generated by scripts/update_modules.py; do not edit. -->',
             '<section class="module-catalog" aria-label="MISP module catalogue">',
             '<div class="module-toolbar" hidden><label>Search modules<input type="search" class="module-search" placeholder="Name, service, input type, requirement…"></label><label>Module type<select class="module-type"><option value="">All types</option>']
    parts.extend(f'<option value="{key}">{label} ({counts[key]})</option>' for key, label in GROUPS.items())
    parts.extend(['</select></label><button type="button" class="module-reset">Reset</button></div>',
                  f'<p class="module-count" role="status" aria-live="polite">{data["count"]} modules</p>',
                  '<noscript><p>All modules are shown. Enable JavaScript to search and filter.</p></noscript>',
                  '<div class="module-grid">'])
    for m in data['modules']:
        info = m['metadata']
        search = json.dumps([m['name'], m['slug'], m['category'], info, m['attributes']], ensure_ascii=False)
        parts.append(f'<article class="module-card" data-type="{m["category"]}" data-search="{e(search)}">')
        parts.append('<div class="module-card-heading"><div class="module-logo">')
        parts.append(f'<span aria-hidden="true">{e(m["name"][:2].upper())}</span>')
        if m['logo']:
            parts.append(f'<img src="{e(m["logo"])}" alt="" loading="lazy" referrerpolicy="no-referrer">')
        parts.append(f'</div><div><span class="module-badge">{GROUPS[m["category"]]}</span><h2>{e(m["name"])}</h2><code>{e(m["slug"])}</code></div></div><p class="module-description">{e(m["description"])}</p>')
        parts.append('<details><summary>Module details</summary><dl>')
        for key in ('note', 'module-type', 'input', 'output', 'requirements', 'features', 'references', 'author', 'version'):
            value = info.get(key) or m['attributes'].get(key)
            if value:
                if isinstance(value, list):
                    value = '\n'.join(str(x) for x in value)
                parts.append(f'<dt>{e(key.replace("-", " ").title())}</dt><dd>{e(value)}</dd>')
        parts.append(f'</dl></details><a class="module-source" href="{e(m["source"])}">View source <span aria-hidden="true">↗</span><span class="module-sr-only"> for {e(m["name"])}</span></a></article>')
    parts.extend(['</div><p class="module-empty" hidden>No modules match your search. Try fewer terms or reset the filters.</p>',
                  f'<p class="module-provenance">Generated from <a href="{REPO}">misp-modules</a>' + (f' · revision <a href="{REPO}/commit/{data["revision"]}">{data["revision"][:12]}</a>' if data['revision'] else ' · local snapshot') + '.</p></section>'])
    return '\n'.join(parts) + '\n'


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or path.read_text() != text:
        path.write_text(text, encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', help='Offline checkout or .tar.gz archive')
    parser.add_argument('--ref', default='main', help='Upstream branch, tag or commit')
    parser.add_argument('--timeout', type=float, default=30)
    parser.add_argument('--website-root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output', type=Path, help='Standalone preview directory')
    args = parser.parse_args()
    try:
        if args.timeout <= 0:
            raise ValueError('Timeout must be positive')
        data = catalog(*load_source(args.source, args.ref, args.timeout))
        body = render(data)
        assets = Path(__file__).resolve().parents[1] / 'static'
        css = (assets / 'css/module-catalog.css').read_text()
        js = (assets / 'js/module-catalog.js').read_text()
        raw = json.dumps(data, ensure_ascii=False, indent=2) + '\n'
        if args.output:
            write(args.output / 'modules.html', '<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>MISP modules</title><style>body{font-family:system-ui;margin:0 auto;padding:32px;max-width:1200px;color:#183549}' + css + '</style><main><h1>MISP modules</h1><p>Explore integrations for enrichment, import, export and workflows.</p>' + body + '</main><script>' + js + '</script></html>')
            write(args.output / 'modules.json', raw)
        else:
            write(args.website_root / 'layouts/shortcodes/module-catalog.html', '<link rel="stylesheet" href="{{ "css/module-catalog.css" | relURL }}">\n' + body + '<script src="{{ "js/module-catalog.js" | relURL }}" defer></script>\n')
            write(args.website_root / 'static/data/modules.json', raw)
        print(f'Generated {data["count"]} modules ({data["revision"] or "local snapshot"})')
    except (ValueError, OSError, SyntaxError, KeyError, tarfile.TarError) as error:
        parser.exit(1, f'Error: {error}\n')


if __name__ == '__main__':
    main()
