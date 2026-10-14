import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import tarfile
import tempfile
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/update_warninglists.py'
spec = importlib.util.spec_from_file_location('update_warninglists', SCRIPT)
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)


class WarningListCatalogTests(unittest.TestCase):
    def definition(self, **changes):
        return {'name': 'Public DNS', 'description': 'Known DNS resolvers', 'type': 'cidr',
                'version': 20261014, 'matching_attributes': ['ip-src', 'ip-dst'],
                'list': ['192.0.2.1/32', '2001:db8::/32'], **changes}

    def record(self, **changes):
        return w.read_definition(io.BytesIO(json.dumps(self.definition(**changes)).encode()), 'list.json')

    def archive(self, path, names):
        with tarfile.open(path, 'w:gz') as archive:
            for name in names:
                raw = json.dumps(self.definition()).encode()
                member = tarfile.TarInfo(name)
                member.size = len(raw)
                archive.addfile(member, io.BytesIO(raw))

    def test_all_match_types_and_lists_are_included(self):
        kinds = ('cidr', 'hostname', 'string', 'substring', 'regex')
        records = {f'lists/{kind}/list.json': self.record(type=kind) for kind in kinds}
        data = w.catalog(records, 'a' * 40)
        self.assertEqual(data['count'], 5)
        self.assertEqual(data['entry_count'], 10)
        self.assertEqual({item['metadata']['type'] for item in data['warninglists']}, set(kinds))
        self.assertTrue(all('/' + 'a' * 40 + '/' in item['json'] for item in data['warninglists']))

    def test_metadata_counts_and_bounded_examples(self):
        record = self.record(list=[str(i) for i in range(100)], category='known')
        self.assertEqual(record['entry_count'], 100)
        self.assertEqual(record['examples'], ['0', '1', '2', '3', '4'])
        self.assertNotIn('list', record['metadata'])
        self.assertEqual(record['metadata']['category'], 'known')

    def test_omitted_matching_attributes_apply_to_all(self):
        definition = self.definition()
        del definition['matching_attributes']
        record = w.read_definition(io.BytesIO(json.dumps(definition).encode()), 'test')
        self.assertEqual(record['matching_attributes'], ['ALL'])

    def test_empty_list_and_version_zero(self):
        data = w.catalog({'lists/empty/list.json': self.record(list=[], version=0)}, None)
        self.assertEqual(data['entry_count'], 0)
        self.assertIn('This list has no entries', w.render(data))

    def test_invalid_definitions_fail_explicitly(self):
        for changes in ({'name': ''}, {'description': []}, {'version': True}, {'version': -1},
                        {'list': [1]}, {'list': {}}, {'type': None}, {'category': []},
                        {'matching_attributes': 'ALL'}, {'matching_attributes': []}):
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                self.record(**changes)

    def test_html_hugo_and_attribute_injection_are_escaped(self):
        data = w.catalog({'lists/test/list.json': self.record(
            name='<script>{{ dangerous }}</script>',
            description='" onmouseover="evil()', list=['</code><script>alert(1)</script>'])}, None)
        page = w.render(data)
        self.assertNotIn('<script>', page)
        self.assertNotIn('{{ dangerous }}', page)
        self.assertIn('&lt;script&gt;', page)
        self.assertIn('&quot; onmouseover=', page)

    def test_archives_with_or_without_wrapper(self):
        for prefix in ('', './', 'misp-warninglists-snapshot/'):
            with self.subTest(prefix=prefix), tempfile.TemporaryDirectory() as tmp:
                path = Path(tmp) / 'snapshot.tar.gz'
                self.archive(path, [prefix + 'lists/first/list.json', prefix + 'lists/second/list.json'])
                records, revision = w.load_source(path)
                self.assertEqual(w.catalog(records, revision)['count'], 2)

    def test_duplicates_mixed_roots_and_traversal_fail(self):
        for paths in (['lists/a/list.json'] * 2,
                      ['repo/lists/a/list.json', 'other/lists/b/list.json'],
                      ['lists/../list.json'], ['../lists/a/list.json']):
            with self.subTest(paths=paths), tempfile.TemporaryDirectory() as tmp:
                path = Path(tmp) / 'snapshot.tar.gz'
                self.archive(path, paths)
                with self.assertRaises(ValueError):
                    w.read_archive(path)

    def test_local_snapshot_and_revision_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            w.write(root / 'lists/test/list.json', json.dumps(self.definition()))
            records, revision = w.load_source(root)
            self.assertNotIn('source', w.catalog(records, revision)['warninglists'][0])
            w.write(root / 'REVISION', 'b' * 40)
            records, revision = w.load_source(root)
            self.assertEqual(revision, 'b' * 40)
            self.assertIn('source', w.catalog(records, revision)['warninglists'][0])

    def test_remote_archive_is_pinned_to_resolved_commit(self):
        calls = []
        def fetch(url, timeout, target):
            calls.append(url)
            if '/commits/' in url:
                target.write(json.dumps({'sha': 'c' * 40}).encode())
            else:
                with tarfile.open(fileobj=target, mode='w:gz') as archive:
                    raw = json.dumps(self.definition()).encode()
                    member = tarfile.TarInfo('repo/lists/test/list.json')
                    member.size = len(raw)
                    archive.addfile(member, io.BytesIO(raw))
        with patch.object(w, 'fetch', side_effect=fetch):
            records, revision = w.load_source(ref='release/test')
        self.assertTrue(calls[0].endswith('release%2Ftest'))
        self.assertTrue(calls[1].endswith('c' * 40))
        self.assertEqual(w.catalog(records, revision)['count'], 1)

    def test_empty_source_and_invalid_revision_fail(self):
        with self.assertRaises(ValueError):
            w.catalog({}, None)
        with self.assertRaises(ValueError):
            w.catalog({'lists/test/list.json': self.record()}, 'main')

    def test_invalid_source_does_not_overwrite_outputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            w.write(root / 'lists/valid/list.json', json.dumps(self.definition()))
            w.write(root / 'lists/invalid/list.json', '{')
            output = root / 'site/static/data/warninglists.json'
            w.write(output, 'existing catalogue')
            result = subprocess.run([sys.executable, str(SCRIPT), '--source', str(root),
                                     '--website-root', str(root / 'site')], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(output.read_text(), 'existing catalogue')
            self.assertFalse((root / 'site/layouts/shortcodes/warninglist-catalog.html').exists())

    def test_determinism_and_no_timestamp_churn(self):
        records = {'lists/z/list.json': self.record(name='Z'), 'lists/a/list.json': self.record(name='A')}
        data = w.catalog(records, None)
        self.assertEqual(data['warninglists'][0]['id'], 'a')
        self.assertEqual(w.render(data), w.render(w.catalog(dict(reversed(list(records.items()))), None)))
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'page.html'
            w.write(path, w.render(data))
            stamp = path.stat().st_mtime_ns
            w.write(path, w.render(data))
            self.assertEqual(path.stat().st_mtime_ns, stamp)


if __name__ == '__main__':
    unittest.main()
