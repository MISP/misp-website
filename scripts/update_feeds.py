#!/usr/bin/env python3
"""Generate the MISP feed catalogue. Python 3.9+, standard library only.

Update this Hugo checkout: python3 scripts/update_feeds.py --website-root .
Standalone preview:       python3 scripts/update_feeds.py --output feeds.html
Offline/pinned source:    add --source /path/to/defaults.json
"""

import argparse
import hashlib
import html
import json
import os
from pathlib import Path
import re
import sys
import tempfile
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

SOURCE = "https://raw.githubusercontent.com/MISP/MISP/2.5/app/files/feed-metadata/defaults.json"
SOURCE_PAGE = "https://github.com/MISP/MISP/blob/2.5/app/files/feed-metadata/defaults.json"
SHORTCODE = "{{< feed-catalog >}}"
START = "<!-- BEGIN GENERATED MISP FEEDS -->"
END = "<!-- END GENERATED MISP FEEDS -->"
LIMIT = 10 * 1024 * 1024
EXTERNAL_ICON = '<svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true" focusable="false"><path d="M5 3H3v10h10v-2M8 3h5v5M13 3 7 9"/></svg>'


def escape(value):
    """Escape HTML and Hugo template delimiters in upstream text."""
    return html.escape(str(value), quote=True).replace("{", "&#123;").replace("}", "&#125;")


def web_url(value):
    try:
        parsed = urlsplit(value)
        return (parsed.scheme.lower() in {"https", "http"} and bool(parsed.hostname)
                and not any(c.isspace() or ord(c) < 32 for c in value))
    except ValueError:
        return False


def load_source(source, timeout):
    if source == SOURCE_PAGE:
        source = SOURCE
    if source.startswith(("https://", "http://")):
        if not source.startswith("https://"):
            raise ValueError("The metadata source must use HTTPS (or a local file).")
        request = Request(source, headers={"User-Agent": "MISP-feed-catalog/1.0", "Accept": "application/json"})
        with urlopen(request, timeout=timeout) as response:
            if not response.geturl().startswith("https://"):
                raise ValueError("The metadata source redirected to a non-HTTPS URL.")
            raw = response.read(LIMIT + 1)
    else:
        with Path(source).open("rb") as stream:
            raw = stream.read(LIMIT + 1)
    if len(raw) > LIMIT:
        raise ValueError("Metadata exceeds the 10 MiB limit.")
    return json.loads(raw.decode("utf-8-sig"))


def normalize(data):
    """Whitelist display fields; never publish upstream headers or settings."""
    if not isinstance(data, list) or not data:
        raise ValueError("Expected a non-empty JSON array of MISP feed records.")
    feeds = []
    for index, record in enumerate(data, 1):
        if not isinstance(record, dict) or not isinstance(record.get("Feed"), dict):
            raise ValueError(f"Record {index}: expected a Feed object.")
        feed = record["Feed"]
        item = {}
        for field in ("name", "provider", "url", "source_format"):
            value = feed.get(field)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"Record {index}: {field} must be a non-empty string.")
            item[field] = value.strip()
        item["source_format"] = item["source_format"].lower()
        transport = feed.get("input_source", "network")
        if not isinstance(transport, str):
            raise ValueError(f"Record {index}: input_source must be a string.")
        item["input_source"] = transport
        enabled = feed.get("enabled")
        item["enabled"] = "Yes" if enabled is True or enabled in (1, "1") else "No" if enabled is False or enabled in (0, "0") else "Unspecified"
        tags = record.get("Tag", [])
        if isinstance(tags, dict):
            tags = [tags]
        if not isinstance(tags, list):
            raise ValueError(f"Record {index}: Tag must be an object or array.")
        item["tags"] = sorted({tag["name"] for tag in tags
                                if isinstance(tag, dict) and isinstance(tag.get("name"), str)})
        feeds.append(item)
    return sorted(feeds, key=lambda f: (f["name"].casefold(), f["provider"].casefold(), f["url"]))


CSS = r"""
#misp-feed-catalog { --mf-ink:#172c42; --mf-muted:#52667b; --mf-border:#dce5ed; --mf-blue:#17669d; color:var(--mf-ink); font:16px/1.6 system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; margin:24px 0; scroll-margin-top:180px; }
#misp-feed-catalog, #misp-feed-catalog * { box-sizing:border-box; }
#misp-feed-catalog [hidden] { display:none !important; }
#misp-feed-catalog a { color:var(--mf-blue); text-decoration:none; }
#misp-feed-catalog a:hover { text-decoration:underline; }
#misp-feed-catalog :is(a,button,input,select,summary):focus-visible { outline:3px solid #1676b5; outline-offset:3px; }
#misp-feed-catalog .mf-hero { background:linear-gradient(120deg,#edf6fc,#f3f9f7); border:1px solid var(--mf-border); border-radius:16px; padding:28px; margin-bottom:24px; }
#misp-feed-catalog .mf-eyebrow { color:#32677f; font-size:12px; font-weight:750; letter-spacing:.12em; text-transform:uppercase; margin:0 0 8px; }
#misp-feed-catalog h2 { font:700 clamp(25px,3vw,34px)/1.2 system-ui,sans-serif; letter-spacing:-.03em; margin:0 0 12px; color:var(--mf-ink); text-transform:none; }
#misp-feed-catalog .mf-intro { max-width:740px; margin:0; color:var(--mf-muted); }
#misp-feed-catalog .mf-stats { display:flex; flex-wrap:wrap; gap:8px; margin-top:20px; }
#misp-feed-catalog .mf-stat { display:inline-flex; align-items:center; gap:6px; background:#fff; border:1px solid var(--mf-border); padding:5px 11px; border-radius:8px; font-size:13px; }
#misp-feed-catalog .mf-toolbar { display:grid; grid-template-columns:minmax(180px,2fr) minmax(110px,1fr) minmax(130px,1fr) auto; align-items:end; gap:12px; margin-bottom:16px; }
#misp-feed-catalog label { display:block; font-size:12px; font-weight:700; margin:0 0 5px; color:var(--mf-muted); }
#misp-feed-catalog :is(input,select,button) { font:inherit; border:1px solid #bacbd9; border-radius:8px; background:#fff; color:var(--mf-ink); min-height:44px; padding:8px 11px; }
#misp-feed-catalog :is(input,select) { width:100%; min-width:0; }
#misp-feed-catalog button { cursor:pointer; font-size:14px; }
#misp-feed-catalog button:hover { background:#edf6fc; }
#misp-feed-catalog .mf-resultbar { display:flex; justify-content:space-between; flex-wrap:wrap; gap:10px; color:var(--mf-muted); font-size:13px; margin-bottom:16px; }
#misp-feed-catalog .mf-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,290px),1fr)); gap:16px; }
#misp-feed-catalog .mf-card { display:flex; flex-direction:column; min-width:0; margin:0; padding:22px; background:#fff; border:1px solid var(--mf-border); border-top:3px solid #70a7c4; border-radius:12px; box-shadow:0 3px 12px #16334e06; transition:box-shadow .16s,border-color .16s; }
#misp-feed-catalog .mf-card:hover { box-shadow:0 7px 22px #16334e12; border-color:#a0bfd4; }
#misp-feed-catalog .mf-badge { align-self:flex-start; border-radius:5px; background:#eaf3fb; color:#225b85; padding:3px 8px; font-size:11px; font-weight:750; letter-spacing:.04em; }
#misp-feed-catalog .mf-badge[data-format="csv"] { background:#eaf5ef; color:#236145; }
#misp-feed-catalog .mf-badge[data-format="freetext"] { background:#f1edfa; color:#624889; }
#misp-feed-catalog h3 { font:650 18px/1.4 system-ui,sans-serif; text-transform:none; letter-spacing:-.015em; margin:14px 0 6px; color:var(--mf-ink); overflow-wrap:anywhere; }
#misp-feed-catalog .mf-provider { color:var(--mf-muted); font-size:13px; margin:0 0 18px; overflow-wrap:anywhere; }
#misp-feed-catalog .mf-bottom { margin-top:auto; padding-top:8px; }
#misp-feed-catalog .mf-link { display:flex; align-items:center; justify-content:space-between; gap:12px; font-size:13px; font-weight:700; }
#misp-feed-catalog svg { display:inline-block; flex-shrink:0; vertical-align:middle; }
#misp-feed-catalog .mf-host { overflow-wrap:anywhere; font-size:12px; font-weight:400; color:var(--mf-muted); }
#misp-feed-catalog details { margin-top:14px; padding-top:12px; border-top:1px solid #edf1f5; font-size:12px; }
#misp-feed-catalog summary { cursor:pointer; color:var(--mf-muted); }
#misp-feed-catalog dl { margin:12px 0 0; }
#misp-feed-catalog dt { font-weight:700; margin-top:8px; }
#misp-feed-catalog dd { margin:0; overflow-wrap:anywhere; }
#misp-feed-catalog code { font:11px/1.6 ui-monospace,monospace; color:var(--mf-muted); background:transparent; padding:0; white-space:normal; overflow-wrap:anywhere; }
#misp-feed-catalog .mf-empty { padding:38px 20px; text-align:center; border:1px dashed #bacbd9; border-radius:12px; background:#f8fbfd; }
#misp-feed-catalog .mf-note { color:var(--mf-muted); font-size:12px; margin:20px 0 0; }
@media(max-width:700px) { #misp-feed-catalog { scroll-margin-top:80px; } #misp-feed-catalog .mf-toolbar { grid-template-columns:1fr 1fr; } #misp-feed-catalog .mf-search { grid-column:1/-1; } #misp-feed-catalog .mf-hero { padding:22px; } }
@media(max-width:380px) { #misp-feed-catalog .mf-toolbar { grid-template-columns:1fr; } }
@media(prefers-reduced-motion:reduce) { #misp-feed-catalog .mf-card { transition:none; } }
"""

JS = r"""
(() => {
  'use strict';
  const root = document.getElementById('misp-feed-catalog');
  if (!root) return;
  const cards = Array.from(root.querySelectorAll('.mf-card'));
  const search = root.querySelector('#mf-search');
  const format = root.querySelector('#mf-format');
  const provider = root.querySelector('#mf-provider');
  const count = root.querySelector('#mf-count');
  function filter() {
    const terms = search.value.trim().toLowerCase().split(/\s+/).filter(Boolean);
    let visible = 0;
    for (const card of cards) {
      const match = terms.every(term => card.dataset.search.includes(term))
        && (!format.value || card.dataset.format === format.value)
        && (!provider.value || card.dataset.provider === provider.value);
      card.hidden = !match;
      if (match) visible++;
    }
    count.textContent = `${visible} of ${cards.length} feeds`;
    root.querySelector('.mf-empty').hidden = visible !== 0;
  }
  search.addEventListener('input', filter);
  format.addEventListener('change', filter);
  provider.addEventListener('change', filter);
  root.querySelector('#mf-reset').addEventListener('click', () => {
    search.value = ''; format.value = ''; provider.value = ''; filter(); search.focus();
  });
  root.querySelector('.mf-toolbar').hidden = false;
  filter();
})();
"""


def render_card(feed):
    name, provider, url, fmt = (feed[k] for k in ("name", "provider", "url", "source_format"))
    tags = ", ".join(feed["tags"])
    search = " ".join((name, provider, url, fmt, tags)).lower()
    network_link = feed["input_source"] == "network" and web_url(url)
    if network_link:
        host = urlsplit(url).hostname
        label = escape(f"Open feed: {name} (opens in a new tab)")
        link = f'<a class="mf-link" href="{escape(url)}" target="_blank" rel="noopener noreferrer" aria-label="{label}">Open feed {EXTERNAL_ICON}</a><span class="mf-host">{escape(host)}</span>'
    else:
        link = f'<span class="mf-host">{escape(url)}</span>'
    tag_html = f'<dt>Tags</dt><dd>{escape(tags)}</dd>' if tags else ''
    return f'''<article class="mf-card" data-search="{escape(search)}" data-format="{escape(fmt)}" data-provider="{escape(provider)}">
<span class="mf-badge" data-format="{escape(fmt)}">{escape(fmt.upper())}</span>
<h3>{escape(name)}</h3><p class="mf-provider">{escape(provider)}</p>
<div class="mf-bottom">{link}
<details><summary>Feed details</summary><dl>
<dt>Source URL or path</dt><dd><code>{escape(url)}</code></dd>
<dt>Input transport</dt><dd>{escape(feed['input_source'])}</dd>
<dt>Enabled in source metadata</dt><dd>{escape(feed['enabled'])}</dd>{tag_html}
</dl></details></div></article>'''


def render(feeds, source):
    formats = sorted({f["source_format"] for f in feeds})
    providers = sorted({f["provider"] for f in feeds}, key=str.casefold)
    source_url = SOURCE_PAGE if source in (SOURCE, SOURCE_PAGE) else source if source.startswith("https://") else None
    source_link = f'<a href="{escape(source_url)}" target="_blank" rel="noopener noreferrer" aria-label="View source metadata (opens in a new tab)">View source metadata {EXTERNAL_ICON}</a>' if source_url else '<span>Built from local metadata</span>'
    digest = hashlib.sha256(json.dumps(feeds, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
    stats = ''.join(f'<span class="mf-stat"><strong>{sum(f["source_format"] == fmt for f in feeds)}</strong> {escape(fmt.upper())}</span>' for fmt in formats)
    format_options = ''.join(f'<option value="{escape(fmt)}">{escape(fmt.upper())}</option>' for fmt in formats)
    provider_options = ''.join(f'<option value="{escape(p)}">{escape(p)}</option>' for p in providers)
    cards = '\n'.join(render_card(feed) for feed in feeds)
    return f'''<!-- Generated by scripts/update_feeds.py; display metadata SHA-256: {digest} -->
<style>{CSS}</style>
<section id="misp-feed-catalog" aria-labelledby="mf-title">
<div class="mf-hero"><p class="mf-eyebrow">MISP · Community intelligence</p>
<h2 id="mf-title">Explore the default feeds</h2>
<p class="mf-intro">Find public threat intelligence sources for correlation and import in MISP. Browse by provider, search for a topic, or choose a feed format.</p>
<div class="mf-stats"><span class="mf-stat"><strong>{len(feeds)}</strong> feeds</span><span class="mf-stat"><strong>{len(providers)}</strong> providers</span>{stats}</div></div>
<div class="mf-toolbar" hidden>
<div class="mf-search"><label for="mf-search">Search feeds</label><input id="mf-search" type="search" placeholder="Name, provider, URL or tag…" autocomplete="off" aria-controls="mf-grid"></div>
<div><label for="mf-format">Format</label><select id="mf-format" aria-controls="mf-grid"><option value="">All formats</option>{format_options}</select></div>
<div><label for="mf-provider">Provider</label><select id="mf-provider" aria-controls="mf-grid"><option value="">All providers</option>{provider_options}</select></div>
<button type="button" id="mf-reset">Reset filters</button></div>
<div class="mf-resultbar"><span id="mf-count" role="status" aria-live="polite" aria-atomic="true">{len(feeds)} of {len(feeds)} feeds</span>{source_link}</div>
<div id="mf-grid" class="mf-grid">{cards}</div>
<p class="mf-empty" hidden>No matching feeds. Try a different search or reset the filters.</p>
<p class="mf-note">This catalogue lists source metadata, including disabled entries. It does not check feed availability. Providers may require a licence, authentication or impose rate limits.</p>
</section><script>{JS}</script>
'''


def standalone(fragment):
    return '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>MISP Default Feeds</title><style>body{margin:0;background:#f8fafc}main{max-width:1180px;margin:auto;padding:24px}header{font:700 17px system-ui;color:#17669d;padding:8px 0}footer{font:13px system-ui;color:#52667b;margin:28px 0} @media(max-width:500px){main{padding:14px}}</style></head>
<body><main><header>MISP / Default feeds</header>''' + fragment + '''<footer>Generated from MISP feed metadata. <a href="https://www.misp-project.org/feeds/">About MISP feeds</a></footer></main></body></html>
'''


def update_page(text):
    """Replace the catalogue only, preserving the page's surrounding content."""
    block = f"{START}\n{SHORTCODE}\n{END}\n\n"
    if START in text or END in text:
        if text.count(START) != 1 or text.count(END) != 1:
            raise ValueError("The feed page has invalid generated-section markers.")
        start, end = text.index(START), text.index(END) + len(END)
        if end < start:
            raise ValueError("The feed page has reversed generated-section markers.")
        updated = text[:start] + block.rstrip() + text[end:]
    else:
        pattern = re.compile(r"^## Default feeds available in MISP\s*\n.*?(?=^To enable a feed for caching|^## Feed overlap analysis matrix)", re.M | re.S)
        updated, count = pattern.subn(lambda _: block, text)
        if count != 1:
            raise ValueError("Cannot locate the existing feed list; no files were changed.")
    return updated.replace(SOURCE_PAGE.replace("/2.5/", "/2.4/"), SOURCE_PAGE)


def write_if_changed(path, text):
    """Atomic replacement, stable output, no unnecessary writes on reruns."""
    if path.is_file() and path.read_text(encoding="utf-8") == text:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    mode = path.stat().st_mode & 0o777 if path.exists() else 0o644
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", newline="\n", dir=path.parent, delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(text)
        temporary.chmod(mode)
        os.replace(temporary, path)
    finally:
        if temporary and temporary.exists():
            temporary.unlink()
    return True


def positive_timeout(value):
    number = float(value)
    if not 0 < number <= 300:
        raise argparse.ArgumentTypeError("Timeout must be between 0 and 300 seconds.")
    return number


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--source", default=SOURCE, help="HTTPS metadata URL or local defaults.json")
    parser.add_argument("--timeout", type=positive_timeout, default=30, help="HTTP timeout in seconds (default: 30)")
    target = parser.add_mutually_exclusive_group()
    target.add_argument("--website-root", type=Path, help="Update content/feeds.md and layouts/shortcodes/feed-catalog.html in a Hugo checkout")
    target.add_argument("--output", type=Path, help="Standalone HTML output (default: feeds.html)")
    args = parser.parse_args(argv)
    try:
        page = args.website_root / "content/feeds.md" if args.website_root else None
        # Validate the existing page before downloading or writing any output.
        updated = update_page(page.read_text(encoding="utf-8")) if page else None
        feeds = normalize(load_source(args.source, args.timeout))
        fragment = render(feeds, args.source)
        if page:
            targets = [(args.website_root / "layouts/shortcodes/feed-catalog.html", fragment), (page, updated)]
        else:
            targets = [(args.output or Path("feeds.html"), standalone(fragment))]
        for path, content in targets:
            action = "Updated" if write_if_changed(path, content) else "Unchanged"
            print(f"{action}: {path}")
        print(f"Rendered {len(feeds)} feeds from {args.source}")
        return 0
    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
