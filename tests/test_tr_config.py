import unittest
from testing_common import tile_rando

from tile_rando import tr_config

class TestTRConfig(unittest.TestCase):
    def test_init(self):
        test_config = tr_config.TRConfig()
        self.assertTrue(isinstance(test_config, tr_config.TRConfig), msg="TRConfig did not initialize properly!")
        self.assertEqual("", test_config._original_rom_path, "TRConfig _original_rom_path did not initialize properly!")
        self.assertEqual(b'', test_config._original_rom, "TRConfig _original_rom did not initialize properly!")
        self.assertEqual("", test_config._modified_rom_path, "TRConfig _modified_rom_path did not initialize properly!")
        self.assertIsNone(test_config._seed, msg="TRConfig _seed did not initialize properly!")