import os
import unittest
from testing_common import tile_rando, original_rom_path, load_test_data_dir

from tile_rando import tr_area_creator, tr_map_grid, tr_room_placeholder, tr_door_attach_point, tr_room_generator
from tekton import tekton_room_dict, tekton_room, tekton_tile_grid, tekton_door


class TestTRAreaCreator(unittest.TestCase):
    def test_init(self):
        test_creator = tr_area_creator.TRAreaCreator()
        self.assertTrue(isinstance(test_creator, tr_area_creator.TRAreaCreator),
                        msg="TRRoomCreator did not initialize properly!")
        self.assertIsNone(test_creator.source_rooms,
                          msg="TRRoomCreator rooms did not initialize properly!")

    def test_generate_map_grid(self):
        test_data_dir = os.path.join(os.path.dirname((os.path.abspath(__file__))),
                                     'fixtures',
                                     'test_tr_area_creator',
                                     'test_generate_map_grid'
                                     )
        test_data = load_test_data_dir(test_data_dir)

        for test_case in test_data:
            test_dict = self._populate_test_room_dict(test_case['source_rooms'])
            test_creator = tr_area_creator.TRAreaCreator()
            test_creator.source_rooms = test_dict

            actual_result = test_creator.generate_map_grid()
            self.assertTrue(isinstance(actual_result, tr_map_grid.TRMapGrid),
                            msg="TRRoomCreator.generate_map_grid did not return a TRMapGrid object!")

            self.assertTrue(any(room.tekton_room.header == 0x791f8 for room in actual_result.rooms),
                            "Landing Site not found in return grid!")

            for room in actual_result.rooms:
                self._verify_room_placeholder_placement(actual_result.get_room_top_left_coords(room), actual_result)

            for room in actual_result.rooms:
                for item in room.attached_door_attach_points:
                    if isinstance(item, tr_door_attach_point.TRDoorAttachPoint) and item.is_attached:
                        self.assertEqual(item,
                                         item.farside_door.farside_door,
                                         "Door attachment not reciprocal!")
                        self.assertEqual(room,
                                         item.farside_door.farside_room,
                                         "Door room attachment not reciprocal!")

            for room in actual_result.rooms:
                print(hex(room.tekton_room.header))
                print(room.attached_door_attach_points)
                self.assertIsNotNone(room.room_generator, msg="Room has no Room Generator!")
                self.assertTrue(isinstance(room.room_generator, tr_room_generator.TRRoomGenerator),
                                msg="Room Generator does not inherit from TRRoomGenerator!")
                self.assertEqual(len(room.attached_door_attach_points),
                                 len(room.tekton_room.doors),
                                 msg="Tekton room {} has incorrect number of doors!".format(hex(room.tekton_room.header)))
                for i in range(len(room.attached_door_attach_points)):
                    self.assertEqual(room.attached_door_attach_points[i].farside_room.tekton_room.header,
                                     room.tekton_room.doors[i].target_room_id,
                                     "Tekton Door has incorrect target_room_id!")




        test_creator = tr_area_creator.TRAreaCreator()
        test_dict = tekton_room_dict.TektonRoomDict()
        test_creator.source_rooms = test_dict
        with self.assertRaises(tr_area_creator.RequiredRoomMissingError):
            test_creator.generate_map_grid()

    def _verify_room_placeholder_placement(self, room_coords, map_grid):
        room_placeholder = map_grid[room_coords[0]][room_coords[1]]
        for row in range(room_coords[0], room_coords[0] + room_placeholder.width):
            for col in range(room_coords[1], room_coords[1] + room_placeholder.height):
                self.assertEqual(room_placeholder,
                                 map_grid[row][col],
                                 "Room Placeholder was not correctly added to Map Grid!")

    def _populate_test_room_dict(self, source_rooms):
        test_dict = tekton_room_dict.TektonRoomDict()
        for source_room in source_rooms:
            new_room = tekton_room.TektonRoom(source_room['width'], source_room['height'])
            new_room.header = source_room['header']
            new_room.write_level_data = source_room['write_level_data']
            new_room.tiles = tekton_tile_grid.TektonTileGrid(source_room['width'] * 16, source_room['height'] * 16)
            test_dict.add_room(new_room)
            for source_door in source_room["doors"]:
                new_door = tekton_door.TektonDoor()
                new_door.data_address = source_door
                new_room.doors.append(new_door)

        return test_dict

