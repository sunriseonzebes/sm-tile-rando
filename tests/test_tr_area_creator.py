import os
import unittest
from testing_common import tile_rando, original_rom_path, load_test_data_dir

from tile_rando import tr_area_creator, tr_map_grid
from tekton import tekton_room_dict, tekton_room


class TestTRAreaCreator(unittest.TestCase):
    def test_init(self):
        test_creator = tr_area_creator.TRAreaCreator()
        self.assertTrue(isinstance(test_creator, tr_area_creator.TRAreaCreator),
                        msg="TRRoomCreator did not initialize properly!")
        self.assertIsNone(test_creator.rooms,
                          msg="TRRoomCreator rooms did not initialize properly!")

    def test_generate_map_grid(self):
        test_dict = tekton_room_dict.TektonRoomDict()
        test_creator = tr_area_creator.TRAreaCreator()
        test_creator.rooms = test_dict
        with self.assertRaises(tr_area_creator.RequiredRoomMissingError):
            test_creator.generate_map_grid()

        test_dict = tekton_room_dict.TektonRoomDict()
        test_room = tekton_room.TektonRoom(9, 5)
        test_room.header = 0x791f8
        test_dict.add_room(test_room)

        test_creator = tr_area_creator.TRAreaCreator()
        test_creator.rooms = test_dict

        actual_result = test_creator.generate_map_grid()
        self.assertTrue(isinstance(actual_result, tr_map_grid.TRMapGrid),
                        msg="TRRoomCreator.generate_map_grid did not return a TRMapGrid object!")
        room_coords = [None, None]
        for row in range(actual_result.height):
            for col in range(actual_result.height):
                if actual_result[col][row] == test_room:
                    room_coords = [col, row]
                    break
            if room_coords != [None, None]:
                break

        self.assertNotEqual([None, None], room_coords, "Landing Site not found in MapGrid!")

        for row in range(room_coords[0], room_coords[0] + 9):
            for col in range(room_coords[1], room_coords[1] + 5):
                self.assertEqual(test_room,
                                 actual_result[row][col],
                                 "Landing Site was not correctly added to Map Grid!")


        print(actual_result)