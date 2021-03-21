import unittest
from testing_common import tile_rando

from tile_rando import __main__

class TestTRMain(unittest.TestCase):
    def test_parse_args(self):
        test_args = __main__.parse_args(['-i', 'original_rom.sfc', '-o', 'modified_rom.sfc'])
        self.assertEqual('original_rom.sfc',
                         test_args.i,
                         "parse_args did not load original_rom_path correctly!")
        self.assertEqual('modified_rom.sfc',
                         test_args.o,
                         "parse_args did not load modified_rom_path correctly!")
        with self.assertRaises(SystemExit):
            __main__.parse_args([])
        with self.assertRaises(SystemExit):
            __main__.parse_args(['-t', 'nonsense_arg'])
        with self.assertRaises(SystemExit):
            __main__.parse_args(['-i', 'original_rom.sfc'])
        with self.assertRaises(SystemExit):
            __main__.parse_args(['-o', 'modified_rom.sfc'])
        test_args = __main__.parse_args(['-i', 'original_rom.sfc', '-o', 'modified_rom.sfc', '--seed', '54321'])
        self.assertEqual('original_rom.sfc',
                         test_args.i,
                         "parse_args did not load original_rom_path correctly!")
        self.assertEqual('modified_rom.sfc',
                         test_args.o,
                         "parse_args did not load modified_rom_path correctly!")
        self.assertEqual('54321',
                         test_args.seed,
                         "parse_args did not load config.seed correctly!")