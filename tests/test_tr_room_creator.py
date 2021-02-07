import os
import unittest
from testing_common import tile_rando, original_rom_path, load_test_data_dir

from tile_rando import tr_room_creator, tr_map_grid
from tekton import tekton_room_dict


class TestTRRoomCreator(unittest.TestCase):
    def test_init(self):
        test_creator = tr_room_creator.TRRoomCreator()
        self.assertTrue(isinstance(test_creator, tr_room_creator.TRRoomCreator),
                        msg="TRRoomCreator did not initialize properly!")
        self.assertIsNone(test_creator.rooms,
                          msg="TRRoomCreator rooms did not initialize properly!")

    def test_generate_map_grid(self):
        test_dict = tekton_room_dict.TektonRoomDict()
        test_creator = tr_room_creator.TRRoomCreator()
        test_creator.rooms = test_dict
        actual_result = test_creator.generate_map_grid()
        self.assertTrue(isinstance(actual_result, tr_map_grid.TRMapGrid),
                        msg="TRRoomCreator.generate_map_grid did not return a TRMapGrid object!")
        for col in range(actual_result.width):
            for row in range(actual_result.height):
                self.assertIsNone(actual_result[col][row])