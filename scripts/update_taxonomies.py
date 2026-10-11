#!/usr/bin/env python3
"""Collect all MISP taxonomy metadata and generate a searchable catalogue.

Python 3.9+, standard library only. No API key required.
  python3 scripts/update_taxonomies.py --website-root .
  python3 scripts/update_taxonomies.py --output /tmp/taxonomy-preview
  Add --source /path/to/misp-taxonomies for an offline checkout.
"""

import argparse
import hashlib
import html
import io
import json
import math
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
import tarfile
import tempfile
import time
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

REPOSITORY = "https://github.com/MISP/misp-taxonomies"
API = "https://api.github.com/repos/MISP/misp-taxonomies/commits/"
ARCHIVE = "https://codeload.github.com/MISP/misp-taxonomies/tar.gz/"
SHORTCODE = "{{< taxonomy-catalog >}}"
LIMIT = 64 * 1024 * 1024
ASSETS = Path(__file__).resolve().parent


def escape(value):
    # Protect both HTML and the Hugo template parser from upstream strings.
    return html.escape(str(value), quote=True).replace("{", "&#123;").replace("}", "&#125;")


def fetch(url, timeout):
    for attempt in range(3):
        try:
            request = Request(url, headers={"User-Agent": "MISP-taxonomy-catalog/1.0"})
            with urlopen(request, timeout=timeout) as response:
                if not response.geturl().startswith("https://"):
                    raise ValueError("Source redirected to a non-HTTPS URL.")
                content = response.read(LIMIT + 1)
            if len(content) > LIMIT:
                raise ValueError("Source exceeds the 64 MiB limit.")
            return content
        except (HTTPError, URLError, TimeoutError) as error:
            if isinstance(error, HTTPError) and error.code not in (429, 500, 502, 503, 504):
                raise
            if attempt == 2:
                raise
            time.sleep(2 ** attempt)


def archive_records(raw):
    """Read JSON directly; never extract paths from an upstream archive."""
    files = {}
    members = {}
    total = 0
    with tarfile.open(fileobj=io.BytesIO(raw), mode="r:gz") as archive:
        for member in archive:
            parts = member.name.split("/")
            while parts and parts[0] == ".":
                parts.pop(0)
            relevant = (len(parts) in (1, 2) and parts[-1] == "MANIFEST.json") or (
                len(parts) in (2, 3) and parts[-1] == "machinetag.json")
            if not relevant or not member.isfile():
                continue
            if any(p in ("", ".", "..") for p in parts):
                raise ValueError("Invalid archive metadata path.")
            path = tuple(parts)
            total += member.size
            if member.size > LIMIT or total > LIMIT or path in members:
                raise ValueError("Archive metadata exceeds limits or contains duplicate paths.")
            members[path] = member
        manifests = [path for path in members if path[-1] == "MANIFEST.json"]
        if not manifests:
            raise ValueError("Source has no MANIFEST.json.")
        if len(manifests) != 1:
            raise ValueError("Source has multiple MANIFEST.json files.")
        prefix = manifests[0][:-1]
        for parts, member in members.items():
            if parts[:len(prefix)] != prefix:
                continue
            relative = parts[len(prefix):]
            if relative != ("MANIFEST.json",) and not (
                    len(relative) == 2 and relative[1] == "machinetag.json"):
                continue
            files["/".join(relative)] = json.loads(
                archive.extractfile(member).read().decode("utf-8-sig"))
    return files.pop("MANIFEST.json"), files


def read_json(path):
    with path.open("rb") as stream:
        raw = stream.read(LIMIT + 1)
    if len(raw) > LIMIT:
        raise ValueError(f"Metadata file exceeds limit: {path}")
    return json.loads(raw.decode("utf-8-sig"))


def load_source(source, ref, timeout):
    if source:
        path = Path(source)
        if path.is_dir():
            manifest = read_json(path / "MANIFEST.json")
            files = {p.relative_to(path).as_posix(): read_json(p)
                     for p in sorted(path.glob("*/machinetag.json"))}
            revision = None
            if (path / "REVISION").is_file():
                revision = (path / "REVISION").read_text().strip()
            elif (path / ".git").exists():
                revision = subprocess.check_output(
                    ["git", "-C", str(path), "rev-parse", "HEAD"], text=True).strip()
                changed = subprocess.check_output(
                    ["git", "-C", str(path), "status", "--porcelain", "--",
                     "MANIFEST.json", "*/machinetag.json"], text=True)
                if changed:
                    revision = None
            return manifest, files, revision
        with path.open("rb") as stream:
            raw = stream.read(LIMIT + 1)
        if len(raw) > LIMIT:
            raise ValueError("Archive exceeds the 64 MiB limit.")
        manifest, files = archive_records(raw)
        return manifest, files, None
    commit = json.loads(fetch(API + quote(ref, safe=""), timeout)).get("sha", "")
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise ValueError("GitHub returned an invalid commit SHA.")
    manifest, files = archive_records(fetch(ARCHIVE + commit, timeout))
    return manifest, files, commit


def strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for key, child in value.items():
            if key != "uuid":
                yield from strings(child)
    elif isinstance(value, list):
        for child in value:
            yield from strings(child)


def machine_tags(metadata):
    values = {group["predicate"]: group.get("entry", []) for group in metadata.get("values", [])}
    for predicate in metadata["predicates"]:
        prefix = metadata["namespace"] + ":" + predicate["value"]
        entries = values.get(predicate["value"], [])
        if entries:
            for entry in entries:
                yield prefix + "=" + json.dumps(entry["value"], ensure_ascii=False)
        else:
            yield prefix


def validate(metadata, name):
    if not isinstance(metadata, dict):
        raise ValueError(f"{name}: expected a metadata object.")
    for field in ("namespace", "description"):
        if not isinstance(metadata.get(field), str) or not metadata[field].strip():
            raise ValueError(f"{name}: {field} must be a non-empty string.")
    if type(metadata.get("version")) is not int or metadata["version"] < 0:
        raise ValueError(f"{name}: version must be a non-negative integer.")
    for field in ("expanded", "uuid"):
        if field in metadata and not isinstance(metadata[field], str):
            raise ValueError(f"{name}: {field} must be a string.")
    for field in ("deprecated", "exclusive"):
        if field in metadata and type(metadata[field]) is not bool:
            raise ValueError(f"{name}: {field} must be a boolean.")
    for field in ("refs", "type"):
        if field in metadata and (not isinstance(metadata[field], list)
                                  or any(not isinstance(x, str) for x in metadata[field])):
            raise ValueError(f"{name}: {field} must be an array of strings.")
    predicates = metadata.get("predicates")
    if not isinstance(predicates, list) or not predicates:
        raise ValueError(f"{name}: expected a non-empty predicates array.")
    seen = set()
    for predicate in predicates:
        if not isinstance(predicate, dict) or not isinstance(predicate.get("value"), str) or not predicate["value"]:
            raise ValueError(f"{name}: predicate has no string value.")
        if predicate["value"] in seen:
            raise ValueError(f"{name}: duplicate predicate.")
        seen.add(predicate["value"])
    groups = metadata.get("values", [])
    if not isinstance(groups, list):
        raise ValueError(f"{name}: values must be an array.")
    grouped = set()
    for group in groups:
        if not isinstance(group, dict) or group.get("predicate") not in seen:
            raise ValueError(f"{name}: value group references an unknown predicate.")
        if group["predicate"] in grouped:
            raise ValueError(f"{name}: duplicate value group.")
        grouped.add(group["predicate"])
        entries = group.get("entry", [])
        if not isinstance(entries, list):
            raise ValueError(f"{name}: entry must be an array.")
        entry_values = set()
        for entry in entries:
            if not isinstance(entry, dict) or not isinstance(entry.get("value"), str) or not entry["value"]:
                raise ValueError(f"{name}: entry has no string value.")
            if entry["value"] in entry_values:
                raise ValueError(f"{name}: duplicate entry value.")
            entry_values.add(entry["value"])


def build_catalog(manifest, files, revision=None):
    if revision is not None and not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise ValueError("Source revision must be a full immutable commit SHA.")
    if not isinstance(manifest, dict) or not isinstance(manifest.get("taxonomies"), list) or not manifest["taxonomies"]:
        raise ValueError("Expected a non-empty manifest taxonomies array.")
    listed = {}
    for item in manifest["taxonomies"]:
        name = item.get("name") if isinstance(item, dict) else None
        if not isinstance(name, str) or not re.fullmatch(r"[A-Za-z0-9_.-]+", name) or name in (".", "..") or name in listed:
            raise ValueError("Manifest has an invalid or duplicate taxonomy name.")
        listed[name] = item
    expected = {name + "/machinetag.json" for name in listed}
    if expected - files.keys():
        raise ValueError("Missing taxonomies: " + ", ".join(sorted(expected - files.keys())))
    records = []
    namespaces = set()
    for path, metadata in sorted(files.items()):
        name = path.split("/")[0]
        validate(metadata, name)
        if metadata["namespace"] in namespaces:
            raise ValueError("Duplicate taxonomy namespace: " + metadata["namespace"])
        namespaces.add(metadata["namespace"])
        encoded = json.dumps(metadata, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        records.append({"name": name, "metadata": metadata, "manifest_entry": listed.get(name),
                        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
                        "predicate_count": len(metadata["predicates"]),
                        "value_count": sum(len(v.get("entry", [])) for v in metadata.get("values", [])),
                        "tag_count": sum(1 for _ in machine_tags(metadata)),
                        "source_url": REPOSITORY + "/tree/" + revision + "/" + quote(name, safe="") if revision else None,
                        "json_url": "https://raw.githubusercontent.com/MISP/misp-taxonomies/" + revision + "/" + quote(name, safe="") + "/machinetag.json" if revision else None})
    records.sort(key=lambda r: (r["metadata"]["namespace"].casefold(), r["name"]))
    return {"schema_version": 1, "repository": REPOSITORY, "revision": revision,
            "manifest": manifest, "taxonomy_count": len(records), "taxonomies": records}


def render_card(record):
    metadata = record["metadata"]
    name = metadata["namespace"]
    status = "deprecated" if metadata.get("deprecated") else "current"
    # Queries use whitespace-separated terms, so repeated words need only one
    # copy. This greatly reduces large vocabularies (for example satellites).
    search = " ".join(sorted(set(" ".join(
        [record["name"], *strings(metadata), *machine_tags(metadata)]).lower().split())))
    tags = list(machine_tags(metadata))[:3]
    expanded = metadata.get("expanded", "")
    title = f'<p class="mt-expanded">{escape(expanded)}</p>' if expanded and expanded != name else ""
    details = f'<dt>Predicates</dt><dd>{record["predicate_count"]}</dd><dt>Defined values</dt><dd>{record["value_count"]}</dd>'
    for field, label in (("type", "Applies to"), ("exclusive", "Exclusive taxonomy"), ("uuid", "UUID")):
        if field in metadata:
            value = metadata[field]
            display = ", ".join(value) if isinstance(value, list) else ("Yes" if value else "No") if isinstance(value, bool) else value
            details += f'<dt>{label}</dt><dd>{escape(display)}</dd>'
    examples = "".join(f'<li><code>{escape(tag)}</code></li>' for tag in tags)
    refs = "".join(f'<li>{escape(ref)}</li>' for ref in metadata.get("refs", []))
    if refs:
        details += f'<dt>References</dt><dd><ul>{refs}</ul></dd>'
    badge = '<span class="mt-deprecated">Deprecated</span>' if status == "deprecated" else ""
    structure = "values" if record["value_count"] else "predicates"
    resources = (f'<nav aria-label="{escape(name)} resources"><a href="{escape(record["source_url"])}">Source</a>'
                 f'<a href="{escape(record["json_url"])}">JSON</a></nav>'
                 if record["source_url"] and record["json_url"] else "")
    return f'''<article class="mt-card" id="taxonomy-{escape(record['name'])}" data-search="{escape(search)}" data-status="{status}" data-structure="{structure}" data-namespace="{escape(name.lower())}" data-tags="{record['tag_count']}">
<div class="mt-card-head"><h3>{escape(name)}</h3>{badge}<span class="mt-version">v{metadata['version']}</span></div>
{title}<p class="mt-description">{escape(metadata['description'])}</p>
<div class="mt-card-footer"><span class="mt-tag-count">{record['tag_count']:,} defined tags</span>{resources}</div>
<details><summary>Tag examples &amp; metadata</summary><ul class="mt-examples">{examples}</ul><dl>{details}</dl></details>
</article>'''


def render(catalog, download_url):
    records = catalog["taxonomies"]
    cards = "\n".join(render_card(record) for record in records)
    total = sum(r["tag_count"] for r in records)
    predicates = sum(r["predicate_count"] for r in records)
    revision = catalog["revision"]
    provenance = f'<a href="{REPOSITORY}/commit/{escape(revision)}">Source revision {escape(revision[:12])}</a>' if revision else "Local metadata snapshot"
    css = (ASSETS / "taxonomy-catalog.css").read_text()
    js = (ASSETS / "taxonomy-catalog.js").read_text()
    return f'''<!-- Generated by scripts/update_taxonomies.py. -->
<style>{css}</style>
<section id="misp-taxonomy-catalog" aria-label="Taxonomy catalogue">
<div class="mt-intro"><p class="mt-eyebrow">Community classification library</p><p>Find the right vocabulary for your events and attributes.</p>
<div class="mt-stats"><span><strong>{len(records)}</strong> taxonomies</span><span><strong>{predicates:,}</strong> predicates</span><span><strong>{total:,}</strong> defined tags</span></div>
<a class="mt-download" href="{escape(download_url)}" download>Download all metadata (JSON) ↓</a></div>
<div class="mt-toolbar" hidden><div class="mt-search-field"><label for="mt-search">Search taxonomies</label><input id="mt-search" type="search" placeholder="Namespace, description or machine tag…" aria-describedby="mt-help" aria-controls="mt-grid" autocomplete="off"></div>
<div><label for="mt-structure">Tag structure</label><select id="mt-structure"><option value="">All taxonomies</option><option value="values">With defined values</option><option value="predicates">Predicates only</option></select></div>
<div><label for="mt-sort">Sort by</label><select id="mt-sort"><option value="name">Namespace A–Z</option><option value="tags">Most defined tags</option></select></div><button id="mt-reset" type="button">Reset</button></div>
<p id="mt-help" class="mt-help">Search includes predicate and value labels, descriptions, references and full machine tags.</p>
<p id="mt-count" class="mt-result" role="status" aria-live="polite" aria-atomic="true">Showing all {len(records)} taxonomies</p>
<div id="mt-grid" class="mt-grid">{cards}</div>
<div class="mt-empty" hidden><strong>No taxonomies match your search.</strong><p>Try a broader term or reset the filters.</p></div>
<p class="mt-note">{provenance}. Counts include enumerated values and predicates without values; they do not enumerate free-text tags. Deprecated taxonomies remain included for compatibility.</p>
</section><script>{js}</script>
'''


def update_page(content):
    matches = list(re.finditer(r"^## MISP Taxonomies\s*$", content, re.MULTILINE))
    if len(matches) != 1:
        raise ValueError("Expected exactly one MISP Taxonomies heading in content/datamodels.md.")
    start = matches[0].end()
    next_heading = re.search(r"^## ", content[start:], re.MULTILINE)
    end = start + next_heading.start() if next_heading else len(content)
    section = content[start:end]
    if SHORTCODE in section:
        return content
    first_item = re.search(r"^### ", section, re.MULTILINE)
    if not first_item:
        raise ValueError("Cannot locate the existing taxonomy list; page left unchanged.")
    return content[:start] + section[:first_item.start()].rstrip() + "\n\n" + SHORTCODE + "\n\n" + content[end:]


def write_if_changed(path, content):
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    mode = stat.S_IMODE(path.stat().st_mode) if path.exists() else 0o644
    handle = tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False)
    try:
        with handle:
            handle.write(content)
        os.chmod(handle.name, mode)
        os.replace(handle.name, path)
    finally:
        if os.path.exists(handle.name):
            os.unlink(handle.name)
    return True


def positive_timeout(value):
    number = float(value)
    if not math.isfinite(number) or number <= 0:
        raise argparse.ArgumentTypeError("Timeout must be a positive finite number.")
    return number


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--source", type=Path, help="Local misp-taxonomies checkout or .tar.gz archive")
    parser.add_argument("--ref", default="main", help="Upstream branch, tag or commit (default: main)")
    parser.add_argument("--timeout", type=positive_timeout, default=30, help="Timeout per HTTP request, seconds (default: 30)")
    targets = parser.add_mutually_exclusive_group()
    targets.add_argument("--website-root", type=Path, help="Update the Hugo datamodels page, shortcode and JSON catalogue")
    targets.add_argument("--output", type=Path, help="Standalone output directory (default: taxonomy-preview)")
    args = parser.parse_args(argv)
    try:
        page = args.website_root / "content/datamodels.md" if args.website_root else None
        updated = update_page(page.read_text(encoding="utf-8")) if page else None
        catalog = build_catalog(*load_source(args.source, args.ref, args.timeout))
        data = json.dumps(catalog, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
        if page:
            fragment = render(catalog, '{{ "data/taxonomies.json" | relURL }}')
            # This trusted Hugo expression is the only deliberately unescaped URL.
            fragment = fragment.replace(escape('{{ "data/taxonomies.json" | relURL }}'), '{{ "data/taxonomies.json" | relURL }}')
            outputs = [(args.website_root / "static/data/taxonomies.json", data),
                       (args.website_root / "layouts/shortcodes/taxonomy-catalog.html", fragment), (page, updated)]
        else:
            root = args.output or Path("taxonomy-preview")
            fragment = render(catalog, "taxonomies.json")
            preview = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>MISP taxonomy catalogue</title></head><body style="margin:0;padding:24px;background:#f6f8fb"><main style="max-width:1200px;margin:auto"><h1 style="font:700 30px system-ui;color:#172c42">MISP Taxonomies</h1>' + fragment + '</main></body></html>\n'
            outputs = [(root / "taxonomies.json", data), (root / "taxonomies.html", preview)]
        for path, content in outputs:
            print(f"{'Updated' if write_if_changed(path, content) else 'Unchanged'}: {path}")
        print(f"Collected {catalog['taxonomy_count']} taxonomies; revision {catalog['revision'] or 'local snapshot'}")
        return 0
    except (OSError, ValueError, tarfile.TarError, subprocess.CalledProcessError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
