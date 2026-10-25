import importlib.util
import io
import json
from pathlib import Path
import tarfile
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('update_modules', Path(__file__).resolve().parents[1] / 'scripts/update_modules.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class ModuleCatalogTests(unittest.TestCase):
    helper_path = 'misp_modules/lib/network_acl.py'
    helper_source = '''raise RuntimeError("helpers must not be executed")
def module_info(name, slug, description, references):
    """Return shared export metadata."""
    return {"name": name, "description": description, "references": references,
            "module-type": ["export"], "version": "1.0",
            "features": f"See documentation/export_mod/{slug}.md"}
'''
    helper_module = '''from misp_modules.lib import network_acl as acl
moduleinfo = acl.module_info("Cisco ASA ACL Export", "cisco_asa_export", "Export ACL entries.", ["https://example.org/asa"])
'''

    def source(self, name='Test'):
        return 'import nonexistent_dependency\nmoduleinfo = ' + repr({'name': name, 'description': 'An enrichment', 'logo': 'test.png', 'requirements': ['api key']}) + '\nmispattributes = {"input": ["ip-src"]}\n'

    def test_all_categories_and_helpers(self):
        files = {f'misp_modules/modules/{group}/test.py': self.source() for group in m.GROUPS}
        files['misp_modules/modules/expansion/_helper.py'] = 'raise RuntimeError()'
        data = m.catalog(files, {'test.png'}, 'a' * 40)
        self.assertEqual(data['count'], 4)
        self.assertEqual({x['category'] for x in data['modules']}, set(m.GROUPS))
        self.assertTrue(all('/' + 'a' * 40 + '/' in x['logo'] for x in data['modules']))
        self.assertEqual(data['modules'][0]['attributes']['input'], ['ip-src'])

    def test_code_is_never_executed_and_dynamic_metadata_fails(self):
        with self.assertRaisesRegex(ValueError, 'non-literal'):
            m.metadata('moduleinfo = dict(name="Test")', 'test.py')
        with self.assertRaisesRegex(ValueError, 'missing moduleinfo'):
            m.metadata('raise RuntimeError("do not execute")', 'test.py')
        self.assertEqual(m.metadata(self.source(), 'test.py')[0]['name'], 'Test')

    def test_constants_fstrings_and_typed_declarations(self):
        source = 'LABEL = "QR"\nTYPES = {"ip-src": "IP"}\nmoduleinfo: dict = {"name": f"{LABEL} lookup", "description": "Test"}\nmispattributes = {"input": list(TYPES.keys())}'
        info, attrs = m.metadata(source, 'typed.py')
        self.assertEqual(info['name'], 'QR lookup')
        self.assertEqual(attrs['input'], ['ip-src'])
        info, attrs = m.metadata('MODULE_INFO = {"name": "QR"}\ndef version():\n    return MODULE_INFO', 'qr.py')
        self.assertEqual(info['name'], 'QR')

    def test_optional_dynamic_attributes_are_explicit(self):
        info, attrs = m.metadata(self.source() + '\nmispattributes = {"input": get_types()}\n', 'dynamic.py')
        self.assertIn('computed dynamically', attrs['note'])
        self.assertEqual(info['name'], 'Test')

    def test_imported_metadata_helper_is_read_without_execution(self):
        files = {self.helper_path: self.helper_source,
                 'misp_modules/modules/export_mod/cisco_asa_export.py': self.helper_module}
        data = m.catalog(files, set(), 'a' * 40)
        self.assertEqual(data['count'], 1)
        info = data['modules'][0]['metadata']
        self.assertEqual(info['name'], 'Cisco ASA ACL Export')
        self.assertEqual(info['description'], 'Export ACL entries.')
        self.assertEqual(info['references'], ['https://example.org/asa'])
        self.assertEqual(info['module-type'], ['export'])
        self.assertEqual(info['version'], '1.0')
        self.assertEqual(info['features'], 'See documentation/export_mod/cisco_asa_export.md')
        direct = self.helper_module.replace('from misp_modules.lib import network_acl as acl',
                                          'from misp_modules.lib.network_acl import module_info as info').replace('acl.module_info(', 'info(')
        self.assertEqual(m.metadata(direct, 'direct.py', files)[0], info)

    def test_dynamic_metadata_helpers_still_fail(self):
        helpers = [
            self.helper_source.replace('return {', 'print("side effect")\n    return {'),
            self.helper_source.replace('return {', 'return unknown_call() or {'),
            self.helper_source.replace('def module_info', '@unknown_decorator\ndef module_info'),
            self.helper_source.replace('description, references', 'description, references=None'),
            self.helper_source.replace('"name": name', '"name": name.upper()'),
        ]
        for helper in helpers:
            with self.subTest(helper=helper), self.assertRaisesRegex(ValueError, 'non-literal moduleinfo'):
                m.metadata(self.helper_module, 'unsafe.py', {self.helper_path: helper})
        for source in (self.helper_module, self.helper_module.replace(', ["https://example.org/asa"]', '')):
            with self.subTest(source=source), self.assertRaisesRegex(ValueError, 'non-literal moduleinfo'):
                m.metadata(source, 'missing.py', {} if source == self.helper_module else {self.helper_path: self.helper_source})

    def test_directory_snapshot_includes_metadata_helpers(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for path, source in {self.helper_path: self.helper_source,
                                 'misp_modules/modules/export_mod/cisco_asa_export.py': self.helper_module}.items():
                m.write(root / path, source)
            files, logos, revision = m.load_source(root)
            self.assertIn(self.helper_path, files)
            self.assertEqual(m.catalog(files, logos, revision)['count'], 1)

    def test_html_and_hugo_are_escaped(self):
        data = m.catalog({'misp_modules/modules/expansion/test.py': self.source('<script>{{ dangerous }}</script>')}, set(), None)
        page = m.render(data)
        self.assertNotIn('<script>', page)
        self.assertNotIn('{{ dangerous }}', page)
        self.assertIn('&lt;script&gt;', page)
        self.assertEqual(data['modules'][0]['logo'], '')

    def test_missing_logo_and_path_traversal_fall_back(self):
        source = self.source().replace('test.png', '../test.png')
        data = m.catalog({'misp_modules/modules/expansion/test.py': source}, {'../test.png'}, 'b' * 40)
        self.assertEqual(data['modules'][0]['logo'], '')

    def test_archives_with_or_without_wrapper(self):
        for prefix in ('', 'misp-modules-snapshot/'):
            with self.subTest(prefix=prefix), tempfile.TemporaryDirectory() as tmp:
                path = Path(tmp) / 'snapshot.tar.gz'
                with tarfile.open(path, 'w:gz') as archive:
                    for name, source in {self.helper_path: self.helper_source,
                                         'misp_modules/modules/export_mod/cisco_asa_export.py': self.helper_module}.items():
                        raw = source.encode()
                        member = tarfile.TarInfo(prefix + name)
                        member.size = len(raw)
                        archive.addfile(member, io.BytesIO(raw))
                files, logos, revision = m.load_source(path)
                self.assertIn(self.helper_path, files)
                self.assertEqual(m.catalog(files, logos, revision)['count'], 1)

    def test_determinism_and_no_timestamp_churn(self):
        files = {'misp_modules/modules/expansion/test.py': self.source()}
        self.assertEqual(m.render(m.catalog(files, set(), None)), m.render(m.catalog(files, set(), None)))
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / 'data.json'
            m.write(p, json.dumps(m.catalog(files, set(), None)))
            stamp = p.stat().st_mtime_ns
            m.write(p, p.read_text())
            self.assertEqual(p.stat().st_mtime_ns, stamp)

    def test_empty_or_invalid_snapshot_fails(self):
        with self.assertRaises(ValueError):
            m.catalog({}, set(), None)
        with self.assertRaises(ValueError):
            m.catalog({'misp_modules/modules/expansion/test.py': 'moduleinfo = {}'}, set(), 'main')


if __name__ == '__main__':
    unittest.main()
