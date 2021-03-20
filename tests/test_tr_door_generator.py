import os
import unittest
from testing_common import tile_rando

from tile_rando import tr_door_generator, tr_door_attach_point, tr_room_placeholder
from tekton import tekton_door, tekton_tile_grid, tekton_room


class TestTRDoorGenerator(unittest.TestCase):
    def test_create_classic_door_tile_grid(self):
        actual_result = tr_door_generator.create_classic_door_tile_grid(tekton_door.DoorEjectDirection.RIGHT, 0)
        self.assertTrue(isinstance(actual_result, tekton_tile_grid.TektonTileGrid))
        self.assertEqual(2, actual_result.width, "Generated TileGrid has wrong width!")
        self.assertEqual(4, actual_result.height, "Generated TileGrid has wrong height!")
        for x in range(actual_result.width):
            for y in range(actual_result.height):
                self.assertIsNotNone(actual_result[x][y], msg="Tile Grid contains None!")
        for y in range(actual_result.height):
            self.assertEqual(9, actual_result[0][y].bts_type, msg="Door collar has wrong BTS Type!")
            self.assertEqual(0, actual_result[0][y].bts_num, msg="Door tiles have incorrect door id!")

        actual_result = tr_door_generator.create_classic_door_tile_grid(tekton_door.DoorEjectDirection.LEFT, 3, False)
        self.assertTrue(isinstance(actual_result, tekton_tile_grid.TektonTileGrid))
        self.assertEqual(2, actual_result.width, "Generated TileGrid has wrong width!")
        self.assertEqual(4, actual_result.height, "Generated TileGrid has wrong height!")
        for y in range(actual_result.height):
            self.assertIsNone(actual_result[0][y], msg="Door should not have tiles in shield but it does!")
            self.assertIsNotNone(actual_result[1][y], msg="Door Collar contains None!")
        for y in range(actual_result.height):
            self.assertEqual(9, actual_result[1][y].bts_type, msg="Door collar has wrong BTS Type!")
            self.assertEqual(3, actual_result[1][y].bts_num, msg="Door tiles have incorrect door id!")

        actual_result = tr_door_generator.create_classic_door_tile_grid(tekton_door.DoorEjectDirection.UP, 2)
        self.assertTrue(isinstance(actual_result, tekton_tile_grid.TektonTileGrid))
        self.assertEqual(4, actual_result.width, "Generated TileGrid has wrong width!")
        self.assertEqual(2, actual_result.height, "Generated TileGrid has wrong height!")
        for x in range(actual_result.width):
            for y in range(actual_result.height):
                self.assertIsNotNone(actual_result[x][y], msg="Tile Grid contains None!")
        for x in range(actual_result.height):
            self.assertEqual(9, actual_result[x][1].bts_type, msg="Door collar has wrong BTS Type!")
            self.assertEqual(2, actual_result[x][1].bts_num, msg="Door tiles have incorrect door id!")

    def test_create_tekton_door(self):
        test_door_ap = tr_door_attach_point.TRDoorAttachPoint(0, 0, tekton_door.DoorEjectDirection.UP)
        test_farside_door_ap = tr_door_attach_point.TRDoorAttachPoint(3, 3, tekton_door.DoorEjectDirection.DOWN)
        test_farside_room = tr_room_placeholder.TRRoomPlaceholder(5, 5)
        test_farside_room.screens[3][3].append(test_farside_door_ap)
        test_farside_room.tekton_room = tekton_room.TektonRoom(5, 5)
        test_farside_room.tekton_room.header = 0x71234
        test_door_ap.attach(test_farside_room, test_farside_door_ap)

        actual_result = tr_door_generator.create_tekton_door(test_door_ap)
        self.assertTrue(isinstance(actual_result, tekton_door.TektonDoor),
                        msg="create_tekton_door did not return TektonDoor")
        self.assertEqual(0x71234, actual_result.target_room_id, msg="TektonDoor has incorrect target_room_id!")
        self.assertEqual(test_farside_door_ap.h_screen,
                         actual_result.target_room_screen_h,
                         msg="TektonDoor has incorrect target_room_screen_h")
        self.assertEqual(test_farside_door_ap.v_screen,
                         actual_result.target_room_screen_v,
                         msg="TektonDoor has incorrect target_room_screen_v")
        self.assertEqual(test_door_ap.eject_direction,
                         actual_result.eject_direction,
                         msg="TektonDoor has incorrect eject_direction!")
        