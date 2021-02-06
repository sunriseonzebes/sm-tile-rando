import unittest
from testing_common import tile_rando, original_rom_path

from tile_rando import tr_config


class TestTRConfig(unittest.TestCase):
    def test_init(self):
        test_config = tr_config.TRConfig()
        self.assertTrue(isinstance(test_config, tr_config.TRConfig), msg="TRConfig did not initialize properly!")
        self.assertIsNone(test_config._seed, msg="TRConfig _seed did not initialize properly!")

    def test_seed(self):
        test_config = tr_config.TRConfig()
        test_config.seed = "12345"
        self.assertEqual("12345", test_config.seed, "TRConfig seed set incorrectly!")
        test_config.seed = 4.5
        self.assertEqual("4.5", test_config.seed, "TRConfig seed set incorrectly!")