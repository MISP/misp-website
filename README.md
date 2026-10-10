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
