import copy
import importlib.util
import io
import json
from pathlib import Path
import tarfile
import tempfile
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/update_taxonomies.py"
spec = importlib.util.spec_from_file_location("taxonomy_catalog", SCRIPT)
catalog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(catalog)


def fixture():
    manifest = {"taxonomies": [{"name": "demo", "version": 2}], "license": "CC-0"}
    metadata = {"namespace": "demo", "version": 2, "description": "A classification.",
                "predicates": [{"value": "confidence"}, {"value": "reviewed"}],
                "values": [{"predicate": "confidence", "entry": [
                    {"value": "high", "description": "Strong evidence", "numerical_value": 90},
                    {"value": "low", "expanded": "Low confidence"}]}],
                "type": ["event", "attribute"], "uuid": "example-uuid", "exclusive": False,
                "refs": ["https://example.org/reference"], "future_field": {"keep": True}}
    return manifest, {"demo/machinetag.json": metadata}


class TaxonomyCatalogTests(unittest.TestCase):
    def test_all_metadata_preserved_and_tag_counts_correct(self):
        manifest, files = fixture()
        data = catalog.build_catalog(manifest, files)
        item = data["taxonomies"][0]
        self.assertEqual(item["metadata"], files["demo/machinetag.json"])
        self.assertEqual(data["manifest"], manifest)
        self.assertEqual((item["predicate_count"], item["value_count"], item["tag_count"]), (2, 2, 3))
        self.assertEqual(list(catalog.machine_tags(item["metadata"])),
                         ['demo:confidence="high"', 'demo:confidence="low"', 'demo:reviewed'])

    def test_unlisted_taxonomy_included_and_missing_taxonomy_fails(self):
        manifest, files = fixture()
        extra = copy.deepcopy(files["demo/machinetag.json"])
        extra["namespace"] = "unlisted"
        extra["deprecated"] = True
        files["unlisted/machinetag.json"] = extra
        result = catalog.build_catalog(manifest, files)
        self.assertEqual(result["taxonomy_count"], 2)
        self.assertIsNone(result["taxonomies"][1]["manifest_entry"])
        self.assertIn('data-status="deprecated"', catalog.render(result, "taxonomies.json"))
        del files["demo/machinetag.json"]
        with self.assertRaisesRegex(ValueError, "Missing taxonomies"):
            catalog.build_catalog(manifest, files)

    def test_invalid_structure_is_rejected(self):
        for change in ({"version": True}, {"predicates": []}, {"values": [{"predicate": "absent"}]},
                       {"values": [{"predicate": "confidence", "entry": [{"value": 1}]}]}):
            manifest, files = fixture()
            files["demo/machinetag.json"].update(change)
            with self.subTest(change=change), self.assertRaises(ValueError):
                catalog.build_catalog(manifest, files)

    def test_version_zero_is_valid(self):
        manifest, files = fixture()
        files["demo/machinetag.json"]["version"] = 0
        self.assertEqual(catalog.build_catalog(manifest, files)["taxonomies"][0]["metadata"]["version"], 0)

    def test_html_and_hugo_delimiters_escaped_and_search_covers_values(self):
        manifest, files = fixture()
        files["demo/machinetag.json"]["description"] = '<script>alert(1)</script>{{ malicious }}'
        fragment = catalog.render(catalog.build_catalog(manifest, files), "taxonomies.json")
        self.assertNotIn('<script>alert(1)</script>', fragment)
        self.assertNotIn('{{ malicious }}', fragment)
        self.assertIn('&lt;script&gt;', fragment)
        self.assertIn('strong', fragment)
        self.assertIn('evidence', fragment)
        self.assertIn('demo:confidence=&quot;high&quot;', fragment)

    def test_page_update_preserves_surrounding_sections_and_is_repeatable(self):
        before = '# Core\n\n## MISP Taxonomies\n\nIntroduction.\n\n### demo\n\nOld list\n\n## MISP Galaxy\n\nGalaxy text.\n'
        after = catalog.update_page(before)
        self.assertEqual(after, '# Core\n\n## MISP Taxonomies\n\nIntroduction.\n\n{{< taxonomy-catalog >}}\n\n## MISP Galaxy\n\nGalaxy text.\n')
        self.assertEqual(catalog.update_page(after), after)
        with self.assertRaises(ValueError):
            catalog.update_page('# Unexpected page')

    def test_archive_is_read_without_extraction(self):
        manifest, files = fixture()
        stream = io.BytesIO()
        with tarfile.open(fileobj=stream, mode="w:gz") as archive:
            for path, value in {"MANIFEST.json": manifest, **files}.items():
                raw = json.dumps(value).encode()
                member = tarfile.TarInfo("misp-taxonomies-sha/" + path)
                member.size = len(raw)
                archive.addfile(member, io.BytesIO(raw))
            # An unrelated unsafe path is never extracted.
            archive.addfile(tarfile.TarInfo("../../outside"))
        self.assertEqual(catalog.archive_records(stream.getvalue()), (manifest, files))

    def test_online_source_resolves_revision_before_download(self):
        sha = "a" * 40
        with patch.object(catalog, "fetch", side_effect=[json.dumps({"sha": sha}).encode(), b"archive"]) as fetch:
            with patch.object(catalog, "archive_records", return_value=fixture()):
                self.assertEqual(catalog.load_source(None, "main", 30)[2], sha)
        self.assertEqual(fetch.call_args_list[1].args[0], catalog.ARCHIVE + sha)

    def test_invalid_source_leaves_existing_outputs_untouched(self):
        manifest, files = fixture()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "content").mkdir()
            page = root / "content/datamodels.md"
            page.write_text('## MISP Taxonomies\n\nIntro\n\n### demo\nOld\n')
            before = page.read_bytes()
            with patch.object(catalog, "load_source", return_value=(manifest, {}, None)):
                self.assertEqual(catalog.main(["--website-root", directory]), 1)
            self.assertEqual(page.read_bytes(), before)
            self.assertFalse((root / "static/data/taxonomies.json").exists())


if __name__ == "__main__":
    unittest.main()
