import os
import unittest
from testing_common import tile_rando, original_rom_path, load_test_data_dir

from tile_rando import tr_map_grid

class TestTRMapGrid(unittest.TestCase):
    def test_init(self):
        test_grid = tr_map_grid.TRMapGrid()
        self.assertTrue(isinstance(test_grid, tr_map_grid.TRMapGrid), msg="TRMapGrid did not initialize properly!")
        self.assertEqual(1, len(test_grid._squares), "TRMapGrid.squares has the wrong width!")
        self.assertEqual(1, len(test_grid._squares[0]), "TRMapGrid.squares has the wrong height!")

        test_grid = tr_map_grid.TRMapGrid(25, 15)
        self.assertTrue(isinstance(test_grid, tr_map_grid.TRMapGrid), msg="TRMapGrid did not initialize properly!")
        self.assertEqual(25, len(test_grid._squares), "TRMapGrid.squares has the wrong width!")
        for i in range(len(test_grid._squares)):
            self.assertEqual(15, len(test_grid._squares[i]), "TRMapGrid.squares has the wrong height!")