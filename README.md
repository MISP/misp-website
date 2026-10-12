# MISP Website

This is the repository of MISP website. The current online version of this portal can be found at [misp-project.org](https://www.misp-project.org/).

## Compiling a local version of the website

The MISP website is based on Hugo, a static site generator. If you plan on contributing major changes to the website, it is important to have a local version, so as to test your changes. 

To compile a local version of the website, run the following commands in a terminal:

1. Install [Hugo Extended 0.165.0 and its prerequisites](https://gohugo.io/getting-started/installing/), matching the version used in CI.

2. Clone the misp-website repository
    ```
    git clone https://github.com/MISP/misp-website.git
    ````
3. Change into your new directory
    ```
    cd misp-website
    ```
4. Init submodules
   ```
   git submodule init
   git submodule update
   ```
5. Build the site and make it available on a local server.
    ```
    hugo server
    ```

6. To preview your site in your web browser, navigate to [http://localhost:1313](http://localhost:1313).


## Updating the default feed catalogue

The feed catalogue is generated from the MISP **2.5** branch's
[`defaults.json`](https://github.com/MISP/MISP/blob/2.5/app/files/feed-metadata/defaults.json).
Python 3.9 or later is sufficient; no packages or API credentials are required.

```sh
python3 scripts/update_feeds.py --website-root .
hugo server
```

The script replaces the old list in `content/feeds.md` with a shortcode and
regenerates `layouts/shortcodes/feed-catalog.html`. It preserves the introduction,
usage instructions, overlap matrix and contribution instructions. Commit both
generated files alongside the script. Run the command again whenever the upstream
metadata changes; identical display metadata produces identical output.

For a standalone preview, run:

```sh
python3 scripts/update_feeds.py --output /tmp/feeds.html
```

Open that HTML file in a browser. To use a pinned or offline copy, add
`--source /path/to/defaults.json` to either command. HTTPS sources have a
30-second request timeout, adjustable with `--timeout`. Invalid metadata fails
before output is written. Only display fields are published; upstream headers,
rules and settings are excluded.

The responsive cards support search by name, provider, URL or tag, with format
and provider filters. All feeds remain visible when JavaScript is disabled.
Entries disabled in the source are included, and the source's `enabled` flag
appears in feed details; this does not report availability or the configuration
of a visitor's own MISP instance. Generating the page does not publish it;
deployment uses the existing website workflow.

Generator checks can be run with `python3 -m unittest discover -s tests`.

## Updating the taxonomy catalogue

The datamodels taxonomy section is generated from all `machinetag.json` files in
[`MISP/misp-taxonomies`](https://github.com/MISP/misp-taxonomies). Python 3.9 or
later is sufficient; no packages or API credentials are required.

```sh
python3 scripts/update_taxonomies.py --website-root .
hugo server
```

The collector resolves `main` to a commit and downloads that revision's archive.
It verifies that every taxonomy in `MANIFEST.json` is present, also includes any
unlisted taxonomy definitions, and validates all definitions before writing.
Version zero and predicate-only taxonomies are supported. The downloadable JSON
preserves the full manifest and every metadata field, including UUIDs, references,
colours, numerical values, predicates and value descriptions. It adds counts,
source links, the source revision and a canonical JSON SHA-256 for each definition.

Commit these generated files alongside the script and its CSS/JavaScript assets:

- `content/datamodels.md`: the list becomes `{{< taxonomy-catalog >}}`, preserving
  the introduction and other data-model sections.
- `layouts/shortcodes/taxonomy-catalog.html`: responsive cards with search over
  namespaces, descriptions, predicate/value labels, references and machine tags.
- `static/data/taxonomies.json`: the complete metadata download.

Search ignores case and accents and requires every space-separated term to match.
The tag-structure filter separates taxonomies with enumerated values from those
containing predicates only; sorting supports namespace or defined-tag count.
Cards show the version, description, counts, tag examples and source/JSON links.
All cards and expandable metadata remain available without JavaScript. Counts
describe defined tags, not every possible free-text tag. A deprecated flag, if
present in a source definition, is displayed without excluding the taxonomy.

For a standalone preview and metadata export:

```sh
python3 scripts/update_taxonomies.py --output /tmp/taxonomy-preview
```

Open `taxonomies.html` in that directory; its download links to the adjacent
`taxonomies.json`. To pin the upstream source, add `--ref <commit-or-tag>`. For
offline operation, add `--source /path/to/misp-taxonomies` or a repository
`.tar.gz` archive. Archives may contain the repository files at the root (as
produced by `git archive`) or beneath one common directory (GitHub downloads).
Offline snapshots without a known commit SHA omit the per-taxonomy upstream
Source/JSON links; the complete metadata download remains available. A directory
may provide its upstream commit in a `REVISION` file containing the full
40-character SHA. Clean Git checkouts use `HEAD`; changes to the manifest or
taxonomy files make the checkout a local snapshot. Network requests use a
30-second timeout and retry transient
failures up to twice; override the timeout with `--timeout`. Repeated runs with
identical source content produce identical output and preserve file timestamps.
Generation does not publish the website; deployment uses the existing workflow.

Run generator checks with `python3 -m unittest discover -s tests`.

## How to deploy the MISP website

The Pages workflow builds on pushes to `new` and every six hours. Each build
downloads the MISP CVE Atom feed from Vulnerability-Lookup and publishes a
same-origin plain-text copy for the security page's JavaScript reader. Hugo's
feed cache key changes hourly so subsequent builds can fetch new advisories.

Local builds need HTTPS access to `vulnerability.circl.lu` to populate this list.
A failed feed request times out after ten seconds and produces a warning without
preventing the site from building. The security page keeps a link to the full
Vulnerability-Lookup results even when the feed is unavailable or JavaScript is
disabled.

## Updating the module catalogue

The searchable `/modules/` page is generated from all public module Python files
in [MISP/misp-modules](https://github.com/MISP/misp-modules), covering expansion,
import, export and workflow action modules. Python 3.9+ and its standard library
are sufficient; the generator never imports or runs module code, so optional
module dependencies and API credentials are unnecessary.

```sh
python3 scripts/update_modules.py --website-root .
hugo server
```

The generator resolves `main` to a commit and reads that exact revision's archive.
Commit `layouts/shortcodes/module-catalog.html` and `static/data/modules.json`
alongside the generator, page, CSS and JavaScript. Re-running with identical
inputs produces identical output and preserves unchanged file timestamps.
Refresh whenever upstream modules change; generation uses the existing website
deployment workflow and does not publish by itself.

For a pinned source, add `--ref <commit-or-tag>`. For offline operation, add
`--source /path/to/misp-modules` or `--source /path/to/snapshot.tar.gz` (repository
files at the root or beneath a common wrapper directory). Clean Git checkouts
use `HEAD`; local snapshots can supply a full upstream commit SHA in a `REVISION`
file. Archives supplied offline and modified checkouts have no verified revision,
so source links use `main` and cards use initials. HTTP requests have a 30-second
timeout, adjustable with `--timeout`. Invalid metadata fails before output writes.
Underscore-prefixed helpers are excluded; every other module must provide static
module metadata (including typed declarations, constant references and simple
formatted strings). Newly introduced dynamic metadata causes an explicit error
instead of silently omitting modules. Dynamic optional input/output declarations
are marked explicitly with a link to their source.

For a standalone preview and JSON export:

```sh
python3 scripts/update_modules.py --output /tmp/module-preview
```

Open `modules.html` in that directory. The responsive cards include names,
descriptions, categories, requirements, inputs/outputs, authors and source links.
Search is case/accent insensitive and matches all space-separated terms; it can
be combined with the type filter. All cards and details are available without
JavaScript. Logos use HTTPS URLs pinned to the same upstream revision, with
initials on missing or failed images. They require access to
`raw.githubusercontent.com`; no visitor search data is sent to any service.
The catalogue describes upstream integrations, not the enabled modules or runtime
availability of a particular MISP instance.

Run checks with `python3 -m unittest discover -s tests`.
