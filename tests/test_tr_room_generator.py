import os
import unittest
from testing_common import tile_rando

from tekton.tekton_door import DoorEjectDirection
from tekton.tekton_tile_grid import TektonTileGrid
from tile_rando import tr_room_generator, tr_door_attach_point

class TestTRRoomGenerator(unittest.TestCase):
    def test_init(self):
        test_gen = tr_room_generator.TRRoomGenerator()
        self.assertTrue(isinstance(test_gen, tr_room_generator.TRRoomGenerator),
                        msg="TRRoomGenerator did not initialize correctly!")

class TestTRLandingSiteRoomGenerator(unittest.TestCase):
    def test_init(self):
        test_gen = tr_room_generator.TRLandingSiteRoomGenerator()
        self.assertTrue(isinstance(test_gen, tr_room_generator.TRLandingSiteRoomGenerator),
                        msg="TRLandingSiteRoomGenerator did not initialize correctly!")

class TestTRSimpleBoxRoomGenerator(unittest.TestCase):
    def test_init(self):
        test_gen = tr_room_generator.TRSimpleBoxRoomGenerator()
        self.assertTrue(isinstance(test_gen, tr_room_generator.TRSimpleBoxRoomGenerator),
                        msg="TRSimpleBoxRoomGenerator did not initialize correctly!")
        self.assertIsNone(test_gen._width, "TRSimpleBoxRoomGenerator did not initialize correctly!")
        self.assertIsNone(test_gen._height, "TRSimpleBoxRoomGenerator did not initialize correctly!")

    def test_generate_door_attach_points(self):
        test_gen = tr_room_generator.TRSimpleBoxRoomGenerator()
        test_gen._width = 1
        test_gen._height = 1
        expected_result = [[[tr_door_attach_point.TRDoorAttachPoint(0, 0, DoorEjectDirection.UP),
                           tr_door_attach_point.TRDoorAttachPoint(0, 0, DoorEjectDirection.DOWN),
                           tr_door_attach_point.TRDoorAttachPoint(0, 0, DoorEjectDirection.LEFT),
                           tr_door_attach_point.TRDoorAttachPoint(0, 0, DoorEjectDirection.RIGHT)]]]
        actual_result = test_gen.generate_door_attach_points()
        for row in range(len(expected_result)):
            for col in range(len(expected_result[row])):
                for i in range(len(expected_result[col][row])):
                    self.assertEqual(expected_result[col][row][i].h_screen,
                                     actual_result[col][row][i].h_screen,
                                     "TRSimpleBoxRoomGenerator returned wrong h_screen for attach point {}!".format(i))
                    self.assertEqual(expected_result[col][row][i].v_screen,
                                     actual_result[col][row][i].v_screen,
                                     "TRSimpleBoxRoomGenerator returned wrong v_screen for attach point {}!".format(i))
                    self.assertEqual(expected_result[col][row][i].eject_direction,
                                     actual_result[col][row][i].eject_direction,
                                     "TRSimpleBoxRoomGenerator returned wrong door eject direction for attach point {}!".format(i))

        test_gen = tr_room_generator.TRSimpleBoxRoomGenerator()
        test_gen._width = 2
        test_gen._height = 2
        expected_result = [[[tr_door_attach_point.TRDoorAttachPoint(0, 0, DoorEjectDirection.UP),
                           tr_door_attach_point.TRDoorAttachPoint(0, 0, DoorEjectDirection.LEFT)],
                           [tr_door_attach_point.TRDoorAttachPoint(0, 1, DoorEjectDirection.DOWN),
                           tr_door_attach_point.TRDoorAttachPoint(0, 1, DoorEjectDirection.LEFT)]],
                           [[tr_door_attach_point.TRDoorAttachPoint(1, 0, DoorEjectDirection.UP),
                           tr_door_attach_point.TRDoorAttachPoint(1, 0, DoorEjectDirection.RIGHT)],
                           [tr_door_attach_point.TRDoorAttachPoint(1, 1, DoorEjectDirection.DOWN),
                           tr_door_attach_point.TRDoorAttachPoint(1, 1, DoorEjectDirection.RIGHT)]]]
        actual_result = test_gen.generate_door_attach_points()
        for row in range(len(expected_result)):
            for col in range(len(expected_result[row])):
                for i in range(len(expected_result[col][row])):
                    self.assertEqual(expected_result[col][row][i].h_screen,
                                     actual_result[col][row][i].h_screen,
                                     "TRSimpleBoxRoomGenerator returned wrong h_screen for attach point [{}, {}][{}]!".format(col, row, i))
                    self.assertEqual(expected_result[col][row][i].v_screen,
                                     actual_result[col][row][i].v_screen,
                                     "TRSimpleBoxRoomGenerator returned wrong v_screen for attach point [{}, {}][{}]!".format(col, row, i))
                    self.assertEqual(expected_result[col][row][i].eject_direction,
                                     actual_result[col][row][i].eject_direction,
                                     "TRSimpleBoxRoomGenerator returned wrong door eject direction for attach point [{}, {}][{}]!".format(col, row, i))

        test_gen = tr_room_generator.TRSimpleBoxRoomGenerator()
        test_gen._width = 3
        test_gen._height = 3
        expected_result = [[[tr_door_attach_point.TRDoorAttachPoint(0, 0, DoorEjectDirection.UP),
                           tr_door_attach_point.TRDoorAttachPoint(0, 0, DoorEjectDirection.LEFT)],
                           [tr_door_attach_point.TRDoorAttachPoint(0, 1, DoorEjectDirection.LEFT)],
                           [tr_door_attach_point.TRDoorAttachPoint(0, 2, DoorEjectDirection.DOWN),
                           tr_door_attach_point.TRDoorAttachPoint(0, 2, DoorEjectDirection.LEFT)]],
                           [[tr_door_attach_point.TRDoorAttachPoint(1, 0, DoorEjectDirection.UP)],
                           [],
                           [tr_door_attach_point.TRDoorAttachPoint(1, 2, DoorEjectDirection.DOWN)]],
                           [[tr_door_attach_point.TRDoorAttachPoint(2, 0, DoorEjectDirection.UP),
                           tr_door_attach_point.TRDoorAttachPoint(2, 0, DoorEjectDirection.RIGHT)],
                           [tr_door_attach_point.TRDoorAttachPoint(2, 1, DoorEjectDirection.RIGHT)],
                           [tr_door_attach_point.TRDoorAttachPoint(2, 2, DoorEjectDirection.DOWN),
                           tr_door_attach_point.TRDoorAttachPoint(2, 2, DoorEjectDirection.RIGHT)]]]
        actual_result = test_gen.generate_door_attach_points()
        self.assertEqual(len(expected_result),
                         len(actual_result),
                         "TRSimpleBoxGenerator generate_door_attach_points did not return the correct number of items!")
        for row in range(len(expected_result)):
            for col in range(len(expected_result[row])):
                for i in range(len(expected_result[col][row])):
                    self.assertEqual(expected_result[col][row][i].h_screen,
                                     actual_result[col][row][i].h_screen,
                                     "TRSimpleBoxRoomGenerator returned wrong h_screen for attach point {}!".format(i))
                    self.assertEqual(expected_result[col][row][i].v_screen,
                                     actual_result[col][row][i].v_screen,
                                     "TRSimpleBoxRoomGenerator returned wrong v_screen for attach point {}!".format(i))
                    self.assertEqual(expected_result[col][row][i].eject_direction,
                                     actual_result[col][row][i].eject_direction,
                                     "TRSimpleBoxRoomGenerator returned wrong door eject direction for attach point {}!".format(
                                         i))

    def test_generate_room_tiles(self):
        test_gen = tr_room_generator.TRSimpleBoxRoomGenerator()
        test_gen._width = 1
        test_gen._height = 1
        test_attached_doors = []

        actual_results = test_gen.generate_room_tiles(test_attached_doors)
        self.assertTrue(isinstance(actual_results, TektonTileGrid),
                        msg="generate_room_tiles did not return the correct object!")
        for row in range(len(actual_results)):
            for col in range(len(actual_results[row])):
                self.assertIsNotNone(actual_results[col][row],
                                     msg="generate_room_tiles returned None at grid position {}, {}!".format(col, row))
