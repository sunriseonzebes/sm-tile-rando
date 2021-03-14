import os
import unittest
from testing_common import tile_rando

from tile_rando import tr_room_placeholder, tr_door_attach_point
from tekton.tekton_door import DoorExitDirection

class TestTRRoomPlaceholder(unittest.TestCase):
    def test_init(self):
        test_ph = tr_room_placeholder.TRRoomPlaceholder()
        self.assertTrue(isinstance(test_ph, tr_room_placeholder.TRRoomPlaceholder),
                        msg="TRRoomPlaceholder did not initialize correctly!")
        self.assertIsNone(test_ph.tekton_room, msg="TRRoomPlaceholder did not initialize correctly!")
        self.assertIsNone(test_ph.room_generator, msg="TRRoomPlaceholder did not initialize correctly!")
        self.assertEqual(1, test_ph.width, "TRRoomPlaceholder did not initialize correctly!")
        self.assertEqual(1, test_ph.height, "TRRoomPlaceholder did not initialize correctly!")
        self.assertEqual([[[]]], test_ph.screens, "TRRoomPlaceholder did not initialize correctly!")

        test_ph = tr_room_placeholder.TRRoomPlaceholder(2, 3)
        self.assertTrue(isinstance(test_ph, tr_room_placeholder.TRRoomPlaceholder),
                        msg="TRRoomPlaceholder did not initialize correctly!")
        self.assertEqual(2, test_ph.width, "TRRoomPlaceholder did not initialize correctly!")
        self.assertEqual(3, test_ph.height, "TRRoomPlaceholder did not initialize correctly!")
        self.assertEqual([[[], [], []], [[], [], []]], test_ph.screens, "TRRoomPlaceholder did not initialize correctly!")

    def test_available_door_attach_points(self):
        test_ph = tr_room_placeholder.TRRoomPlaceholder(1, 2)
        expected_results = []
        actual_results = test_ph.available_door_attach_points
        self.assertEqual(expected_results, actual_results, "TRRoomPlaceholder did not return correct available_door_attach_points!")

        test_ph = tr_room_placeholder.TRRoomPlaceholder(9, 5)
        test_ph.screens[0][4].append(tr_door_attach_point.TRDoorAttachPoint(0, 4, DoorExitDirection.RIGHT))
        actual_results = test_ph.available_door_attach_points
        print(actual_results)
        self.assertTrue(isinstance(actual_results[0], tr_door_attach_point.TRDoorAttachPoint),
                        msg="available_door_attach_points did not return the correct results!")