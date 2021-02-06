import unittest
from testing_common import tile_rando, original_rom_path

from tile_rando import tr_project


class TestTRProject(unittest.TestCase):
    def test_init(self):
        test_project = tr_project.TRProject()
        self.assertTrue(isinstance(test_project, tr_project.TRProject))
        self.assertEqual("", test_project.original_rom_path, "TRProject _original_rom_path did not initialize properly!")
        self.assertEqual("", test_project.modified_rom_path, "TRProject _modified_rom_path did not initialize properly!")
