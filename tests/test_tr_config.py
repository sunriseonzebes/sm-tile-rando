import hashlib
import os
import unittest
from testing_common import tile_rando, original_rom_path

from tile_rando import tr_config

class TestTRConfig(unittest.TestCase):
    def test_init(self):
        test_config = tr_config.TRConfig()
        self.assertTrue(isinstance(test_config, tr_config.TRConfig), msg="TRConfig did not initialize properly!")
        self.assertEqual("", test_config._original_rom_path, "TRConfig _original_rom_path did not initialize properly!")
        self.assertEqual(b'', test_config._original_rom, "TRConfig _original_rom did not initialize properly!")
        self.assertEqual("", test_config._modified_rom_path, "TRConfig _modified_rom_path did not initialize properly!")
        self.assertIsNone(test_config._seed, msg="TRConfig _seed did not initialize properly!")

    def test_original_rom_path(self):
        original_rom_md5 = b'\x21\xf3\xe9\x8d\xf4\x78\x0e\xe1\xc6\x67\xb8\x4e\x57\xd8\x86\x75'

        test_config = tr_config.TRConfig()
        test_config.original_rom_path = original_rom_path
        self.assertEqual(original_rom_path,
                         test_config.original_rom_path,
                         "TRConfig original_rom_path was not set correctly!")
        self.assertEqual(3145728, len(test_config._original_rom), "TRConfig _original_rom did not load correctly!")
        self.assertEqual(original_rom_md5,
                         hashlib.md5(test_config._original_rom).digest(),
                         "TRConfig _original_rom has incorrect hash value!")
        bad_rom_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "fixtures", "non_existent_file.sfc")
        with self.assertRaises(OSError):
            test_config.original_rom_path = bad_rom_path
        with self.assertRaises(OSError):
            test_config.original_rom_path = 6

    def test_original_rom(self):
        original_rom_md5 = b'\x21\xf3\xe9\x8d\xf4\x78\x0e\xe1\xc6\x67\xb8\x4e\x57\xd8\x86\x75'

        test_config = tr_config.TRConfig()
        self.assertEqual(0, len(test_config.original_rom), "TRConfig original_rom did not load correctly!")

        test_config.original_rom_path = original_rom_path
        self.assertEqual(3145728, len(test_config.original_rom), "TRConfig original_rom did not load correctly!")
        self.assertEqual(original_rom_md5,
                         hashlib.md5(test_config.original_rom).digest(),
                         "TRConfig original_rom has incorrect hash value!")