"""Offline checks for metadata rendering and safe page updates."""
import contextlib
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("update_feeds", Path(__file__).resolve().parents[1] / "scripts/update_feeds.py")
catalog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(catalog)


def record(**overrides):
    feed = {"name": "Example", "provider": "Provider", "url": "https://example.org/feed", "source_format": "csv", "enabled": False}
    feed.update(overrides)
    return {"Feed": feed}


class CatalogueTests(unittest.TestCase):
    def test_invalid_payloads_fail(self):
        for data in ([], {}, [{"Feed": {}}], [record(name=3)], [record(source_format="")], [None]):
            with self.subTest(data=data), self.assertRaises(ValueError):
                catalog.normalize(data)

    def test_disabled_feeds_and_tags_are_kept(self):
        data = record()
        data["Tag"] = {"name": 'osint:source-type="block-or-filter-list"'}
        feed = catalog.normalize([data])[0]
        self.assertEqual(feed["enabled"], "No")
        self.assertIn("block-or-filter-list", feed["tags"][0])
        self.assertIn("Example", catalog.render([feed], catalog.SOURCE))

    def test_html_and_hugo_injection_escaped(self):
        payload = '<script>alert(1)</script>{{ dangerous }}'
        fragment = catalog.render(catalog.normalize([record(name=payload, provider='" onclick="evil')]), catalog.SOURCE)
        self.assertNotIn(payload, fragment)
        self.assertNotIn("{{ dangerous }}", fragment)
        self.assertIn("&lt;script&gt;", fragment)
        self.assertIn("&#123;&#123; dangerous &#125;&#125;", fragment)

    def test_unsafe_and_local_urls_not_linked(self):
        for url, transport in (("javascript:alert(1)", "network"), ("//example.org/feed", "network"), ("/srv/feed.json", "local"), ("https://example.org/feed", "local")):
            with self.subTest(url=url, transport=transport):
                card = catalog.render_card(catalog.normalize([record(url=url, input_source=transport)])[0])
                self.assertNotIn('href=', card)

    def test_secret_fields_not_published(self):
        feed = catalog.normalize([record(headers="SECRET_HEADER", settings="SECRET_SETTING", rules="SECRET_RULE")])[0]
        fragment = catalog.render([feed], catalog.SOURCE)
        self.assertNotIn("SECRET_", fragment)

    def test_stable_order_and_output(self):
        data = [record(name="zebra"), record(name="Alpha")]
        self.assertEqual(catalog.render(catalog.normalize(data), catalog.SOURCE), catalog.render(catalog.normalize(data[::-1]), catalog.SOURCE))

    def test_page_preserved_and_rerun_idempotent(self):
        before = "---\ntitle: Feeds\n---\n\nINTRO\n\n"
        after = "To enable a feed for caching, check enabled.\n\n## Feed overlap analysis matrix\n\nIMAGE\n"
        page = before + "## Default feeds available in MISP\n\nOLD LIST\n\n" + after
        updated = catalog.update_page(page)
        self.assertTrue(updated.startswith(before))
        self.assertTrue(updated.endswith(after))
        self.assertNotIn("OLD LIST", updated)
        self.assertEqual(updated, catalog.update_page(updated))

    def test_unknown_page_or_bad_markers_fail(self):
        for page in ("Unrelated page", catalog.START, catalog.END + "\n" + catalog.START, catalog.START + catalog.START + catalog.END):
            with self.subTest(page=page), self.assertRaises(ValueError):
                catalog.update_page(page)

    def test_bad_source_preserves_existing_output(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, output = root / "bad.json", root / "feeds.html"
            source.write_text('{"unexpected":true}', encoding="utf-8")
            output.write_text("KEEP", encoding="utf-8")
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(catalog.main(["--source", str(source), "--output", str(output)]), 1)
            self.assertEqual(output.read_text(encoding="utf-8"), "KEEP")

    def test_unchanged_output_not_rewritten(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "page.html"
            self.assertTrue(catalog.write_if_changed(path, "hello"))
            before = path.stat().st_mtime_ns
            self.assertFalse(catalog.write_if_changed(path, "hello"))
            self.assertEqual(before, path.stat().st_mtime_ns)


if __name__ == "__main__":
    unittest.main()
