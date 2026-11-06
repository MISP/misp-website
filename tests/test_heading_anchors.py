"""Build a small Hugo site to check section links reused in blog summaries."""

from html.parser import HTMLParser
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
HUGO = os.environ.get("HUGO_BINARY") or shutil.which("hugo")


class SectionLinks(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.links = []
        self.ids = set()
        self.feed(html)

    def handle_starttag(self, tag, attributes):
        attributes = dict(attributes)
        if "id" in attributes:
            self.ids.add(attributes["id"])
        if tag == "a" and attributes.get("class") == "heading-anchor":
            self.links.append(attributes["href"])


@unittest.skipUnless(HUGO, "Hugo required; set HUGO_BINARY or add hugo to PATH")
class HeadingAnchorTests(unittest.TestCase):
    def test_summary_links_target_the_owning_article(self):
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            hook = site / "layouts/_default/_markup/render-heading.html"
            hook.parent.mkdir(parents=True)
            shutil.copyfile(ROOT / "layouts/_default/_markup/render-heading.html", hook)
            (site / "hugo.toml").write_text(
                'baseURL = "https://example.org/docs/"\nsummaryLength = 100\n',
                encoding="utf-8",
            )
            (site / "layouts/_default/list.html").write_text(
                "{{ range .Pages }}{{ .Summary }}{{ end }}", encoding="utf-8"
            )
            (site / "layouts/_default/single.html").write_text(
                "{{ .Content }}", encoding="utf-8"
            )
            (site / "content/blog").mkdir(parents=True)
            for slug in ("one", "two"):
                (site / f"content/blog/{slug}.md").write_text(
                    f'---\ntitle: {slug}\n---\n\n## Shared heading\n\n'
                    "Some text.\n\n### Detail {#custom-detail}\n\nMore text.\n",
                    encoding="utf-8",
                )
            subprocess.run(
                [HUGO, "--source", str(site)], check=True, capture_output=True, text=True
            )
            summary = SectionLinks((site / "public/blog/index.html").read_text())
            expected = []
            for slug in ("one", "two"):
                article = SectionLinks((site / f"public/blog/{slug}/index.html").read_text())
                links = [f"/docs/blog/{slug}/#{anchor}" for anchor in ("shared-heading", "custom-detail")]
                self.assertEqual(article.links, links)
                self.assertTrue({"shared-heading", "custom-detail"} <= article.ids)
                expected.extend(links)
            self.assertCountEqual(summary.links, expected)


if __name__ == "__main__":
    unittest.main()
