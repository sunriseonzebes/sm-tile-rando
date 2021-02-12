import os
import unittest
from testing_common import tile_rando, original_rom_path, load_test_data_dir

from tile_rando import tr_map_grid, tr_room_placeholder
from tekton import tekton_room

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

    def test_get_item(self):
        test_grid = tr_map_grid.TRMapGrid(1, 1)
        test_object = 4.5
        test_grid._squares[0][0] = test_object
        self.assertEqual(test_object, test_grid[0][0], "TRMapGrid _get_item did not find correct object!")

    def test_width(self):
        test_grid = tr_map_grid.TRMapGrid(1, 1)
        self.assertEqual(1, test_grid.width, "TRMapGrid.width did not return the correct value!")
        test_grid = tr_map_grid.TRMapGrid(4, 1)
        self.assertEqual(4, test_grid.width, "TRMapGrid.width did not return the correct value!")

    def test_height(self):
        test_grid = tr_map_grid.TRMapGrid(1, 1)
        self.assertEqual(1, test_grid.height, "TRMapGrid.height did not return the correct value!")
        test_grid = tr_map_grid.TRMapGrid(1, 7)
        self.assertEqual(7, test_grid.height, "TRMapGrid.height did not return the correct value!")

    def test_add_room(self):
        test_data_dir = os.path.join(os.path.dirname((os.path.abspath(__file__))),
                                     'fixtures',
                                     'test_tr_map_grid',
                                     'test_add_room'
                                     )
        test_data = load_test_data_dir(test_data_dir)

        for test_case in test_data:
            test_grid = tr_map_grid.TRMapGrid(test_case["grid_width"], test_case["grid_height"])
            test_room_placeholder = tr_room_placeholder.TRRoomPlaceholder()
            test_room_placeholder.width = test_case["room_width"]
            test_room_placeholder.height = test_case["room_height"]
            test_room_placeholder.tekton_room = tekton_room.TektonRoom(test_case["room_width"], test_case["room_height"])
            test_grid.add_room_placeholder(test_room_placeholder, test_case["x_offset"], test_case["y_offset"])
            for col in range(test_case["x_offset"], test_case["x_offset"] + test_case["room_width"]):
                for row in range(test_case["y_offset"], test_case["y_offset"] + test_case["room_height"]):
                    self.assertEqual(test_room_placeholder,
                                     test_grid[col][row],
                                     "Room was not added to TRMapGrid correctly!")

        with self.assertRaises(tr_map_grid.RoomExceedsGridBoundariesError):
            test_grid = tr_map_grid.TRMapGrid(4, 4)
            test_room_placeholder = tr_room_placeholder.TRRoomPlaceholder()
            test_room_placeholder.width = 4
            test_room_placeholder.height = 4
            test_room_placeholder.tekton_room = tekton_room.TektonRoom(4, 4)
            test_grid.add_room_placeholder(test_room_placeholder, 2, 2)



