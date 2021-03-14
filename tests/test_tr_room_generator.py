import os
import unittest
from testing_common import tile_rando

from tekton.tekton_door import DoorExitDirection
from tile_rando import tr_room_generator, tr_door_attach_point

class TestTRRoomGenerator(unittest.TestCase):
    def test_init(self):
        test_gen = tr_room_generator.TRRoomGenerator()
        self.assertTrue(isinstance(test_gen, tr_room_generator.TRRoomGenerator),
                        msg="TRRoomGenerator did not initialize correctly!")

class TestTRSimpleBoxRoomGenerator(unittest.TestCase):
    def test_init(self):
        test_gen = tr_room_generator.TRSimpleBoxRoomGenerator()
        self.assertTrue(isinstance(test_gen, tr_room_generator.TRSimpleBoxRoomGenerator),
                        msg="TRSimpleBoxRoomGenerator did not initialize correctly!")
        self.assertEqual(1, test_gen._width, "TRSimpleBoxRoomGenerator did not initialize correctly!")
        self.assertEqual(1, test_gen._height, "TRSimpleBoxRoomGenerator did not initialize correctly!")
        self.assertEqual(0, test_gen._num_doors, "TRSimpleBoxRoomGenerator did not initialize correctly!")

    def test_generate_door_attach_points(self):
        test_gen = tr_room_generator.TRSimpleBoxRoomGenerator()
        test_gen._width = 1
        test_gen._height = 1
        expected_result = [[[tr_door_attach_point.TRDoorAttachPoint(0, 0, DoorExitDirection.DOWN),
                           tr_door_attach_point.TRDoorAttachPoint(0, 0, DoorExitDirection.UP),
                           tr_door_attach_point.TRDoorAttachPoint(0, 0, DoorExitDirection.RIGHT),
                           tr_door_attach_point.TRDoorAttachPoint(0, 0, DoorExitDirection.LEFT)]]]
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
                    self.assertEqual(expected_result[col][row][i].exit_direction,
                                     actual_result[col][row][i].exit_direction,
                                     "TRSimpleBoxRoomGenerator returned wrong door exit direction for attach point {}!".format(i))

        test_gen = tr_room_generator.TRSimpleBoxRoomGenerator()
        test_gen._width = 2
        test_gen._height = 2
        expected_result = [[[tr_door_attach_point.TRDoorAttachPoint(0, 0, DoorExitDirection.DOWN),
                           tr_door_attach_point.TRDoorAttachPoint(0, 0, DoorExitDirection.RIGHT)],
                           [tr_door_attach_point.TRDoorAttachPoint(0, 1, DoorExitDirection.UP),
                           tr_door_attach_point.TRDoorAttachPoint(0, 1, DoorExitDirection.RIGHT)]],
                           [[tr_door_attach_point.TRDoorAttachPoint(1, 0, DoorExitDirection.DOWN),
                           tr_door_attach_point.TRDoorAttachPoint(1, 0, DoorExitDirection.LEFT)],
                           [tr_door_attach_point.TRDoorAttachPoint(1, 1, DoorExitDirection.UP),
                           tr_door_attach_point.TRDoorAttachPoint(1, 1, DoorExitDirection.LEFT)]]]
        actual_result = test_gen.generate_door_attach_points()
        print(actual_result)
        for row in range(len(expected_result)):
            for col in range(len(expected_result[row])):
                for i in range(len(expected_result[col][row])):
                    self.assertEqual(expected_result[col][row][i].h_screen,
                                     actual_result[col][row][i].h_screen,
                                     "TRSimpleBoxRoomGenerator returned wrong h_screen for attach point [{}, {}][{}]!".format(col, row, i))
                    self.assertEqual(expected_result[col][row][i].v_screen,
                                     actual_result[col][row][i].v_screen,
                                     "TRSimpleBoxRoomGenerator returned wrong v_screen for attach point [{}, {}][{}]!".format(col, row, i))
                    self.assertEqual(expected_result[col][row][i].exit_direction,
                                     actual_result[col][row][i].exit_direction,
                                     "TRSimpleBoxRoomGenerator returned wrong door exit direction for attach point [{}, {}][{}]!".format(col, row, i))

        test_gen = tr_room_generator.TRSimpleBoxRoomGenerator()
        test_gen._width = 3
        test_gen._height = 3
        expected_result = [[[tr_door_attach_point.TRDoorAttachPoint(0, 0, DoorExitDirection.DOWN),
                           tr_door_attach_point.TRDoorAttachPoint(0, 0, DoorExitDirection.RIGHT)],
                           [tr_door_attach_point.TRDoorAttachPoint(0, 1, DoorExitDirection.RIGHT)],
                           [tr_door_attach_point.TRDoorAttachPoint(0, 2, DoorExitDirection.UP),
                           tr_door_attach_point.TRDoorAttachPoint(0, 2, DoorExitDirection.RIGHT)]],
                           [[tr_door_attach_point.TRDoorAttachPoint(1, 0, DoorExitDirection.DOWN)],
                           [],
                           [tr_door_attach_point.TRDoorAttachPoint(1, 2, DoorExitDirection.UP)]],
                           [[tr_door_attach_point.TRDoorAttachPoint(2, 0, DoorExitDirection.DOWN),
                           tr_door_attach_point.TRDoorAttachPoint(2, 0, DoorExitDirection.LEFT)],
                           [tr_door_attach_point.TRDoorAttachPoint(2, 1, DoorExitDirection.LEFT)],
                           [tr_door_attach_point.TRDoorAttachPoint(2, 2, DoorExitDirection.UP),
                           tr_door_attach_point.TRDoorAttachPoint(2, 2, DoorExitDirection.LEFT)]]]
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
                    self.assertEqual(expected_result[col][row][i].exit_direction,
                                     actual_result[col][row][i].exit_direction,
                                     "TRSimpleBoxRoomGenerator returned wrong door exit direction for attach point {}!".format(
                                         i))
