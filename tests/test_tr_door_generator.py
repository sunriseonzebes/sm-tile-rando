import os
import unittest
from testing_common import tile_rando

from tile_rando import tr_door_generator
from tekton import tekton_door, tekton_tile_grid


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