import os
import unittest
from testing_common import tile_rando, original_rom_path, load_test_data_dir

from tile_rando import tr_area_creator, tr_map_grid, tr_room_placeholder, tr_door_attach_point
from tekton import tekton_room_dict, tekton_room, tekton_tile_grid


class TestTRAreaCreator(unittest.TestCase):
    def test_init(self):
        test_creator = tr_area_creator.TRAreaCreator()
        self.assertTrue(isinstance(test_creator, tr_area_creator.TRAreaCreator),
                        msg="TRRoomCreator did not initialize properly!")
        self.assertIsNone(test_creator.source_rooms,
                          msg="TRRoomCreator rooms did not initialize properly!")

    def test_generate_map_grid(self):
        test_dict = tekton_room_dict.TektonRoomDict()
        test_creator = tr_area_creator.TRAreaCreator()
        test_creator.source_rooms = test_dict
        with self.assertRaises(tr_area_creator.RequiredRoomMissingError):
            test_creator.generate_map_grid()

        test_dict = tekton_room_dict.TektonRoomDict()
        test_room = tekton_room.TektonRoom(9, 5)
        test_room.header = 0x791f8
        test_room.tiles = tekton_tile_grid.TektonTileGrid(9*16, 5*16)
        test_dict.add_room(test_room)

        test_creator = tr_area_creator.TRAreaCreator()
        test_creator.source_rooms = test_dict

        actual_result = test_creator.generate_map_grid()
        self.assertTrue(isinstance(actual_result, tr_map_grid.TRMapGrid),
                        msg="TRRoomCreator.generate_map_grid did not return a TRMapGrid object!")
        room_coords = [None, None]
        for row in range(actual_result.height):
            for col in range(actual_result.width):
                if isinstance(actual_result[col][row], tr_room_placeholder.TRRoomPlaceholder) and \
                        actual_result[col][row].tekton_room == test_room:
                    room_coords = [col, row]
                    break
            if room_coords != [None, None]:
                break

        self.assertNotEqual([None, None], room_coords, "Landing Site not found in MapGrid!")
        self._verify_room_placeholder_placement(room_coords, actual_result)

        for room in actual_result.rooms:
            for col in range(len(room.screens)):
                for row in range(len(room.screens[col])):
                    for item in room.screens[col][row]:
                        if isinstance(item, tr_door_attach_point.TRDoorAttachPoint) and item.is_attached:
                            self.assertEqual(item,
                                             item.farside_door.farside_door,
                                             "Door attachment not reciprocal!")
                            self.assertEqual(room,
                                             item.farside_door.farside_room,
                                             "Door room attachment not reciprocal!")

    def _verify_room_placeholder_placement(self, room_coords, map_grid):
        room_placeholder = map_grid[room_coords[0]][room_coords[1]]
        for row in range(room_coords[0], room_coords[0] + room_placeholder.width):
            for col in range(room_coords[1], room_coords[1] + room_placeholder.height):
                self.assertEqual(room_placeholder,
                                 map_grid[row][col],
                                 "Landing Site was not correctly added to Map Grid!")

