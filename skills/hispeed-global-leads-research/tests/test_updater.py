import hashlib
import importlib.util
from pathlib import Path
import tempfile
import unittest

MODULE = Path(__file__).resolve().parents[1] / 'scripts' / 'update_rules.py'
spec = importlib.util.spec_from_file_location('hispeed_updater', MODULE)
update = importlib.util.module_from_spec(spec)
spec.loader.exec_module(update)

class UpdateRulesTests(unittest.TestCase):
    def test_valid_manifest_writes_markdown(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            path = 'references/targeting.md'
            data = b'# Approved revised strategy\n'
            manifest = {'version':'1.1.0', 'files': {path: hashlib.sha256(data).hexdigest()}}
            out = update.apply_manifest(root, manifest, lambda _: data)
            self.assertTrue(out['updated'])
            self.assertEqual((root/path).read_bytes(), data)
            self.assertIn('1.1.0', (root/'.rules-version.json').read_text())

    def test_tampered_update_does_not_override_cached_version(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            path='references/targeting.md'
            (root/'references').mkdir()
            (root/path).write_text('old safe rules')
            manifest={'version':'1.1.0','files':{path:hashlib.sha256(b'correct').hexdigest()}}
            with self.assertRaisesRegex(ValueError, 'Checksum mismatch'):
                update.apply_manifest(root, manifest, lambda _:b'tampered')
            self.assertEqual((root/path).read_text(), 'old safe rules')

    def test_executable_target_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            payload=b'print("oops")'
            manifest={'version':'1.1.0','files':{'scripts/update_rules.py':hashlib.sha256(payload).hexdigest()}}
            with self.assertRaisesRegex(ValueError,'unauthorized'):
                update.apply_manifest(Path(d), manifest, lambda _:payload)

if __name__=='__main__': unittest.main()
