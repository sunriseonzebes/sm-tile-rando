import os
import unittest
from testing_common import tile_rando

from tile_rando import tr_room_placeholder, tr_door_attach_point
from tekton.tekton_door import DoorEjectDirection

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
        test_door_ap = tr_door_attach_point.TRDoorAttachPoint(0, 4, DoorEjectDirection.RIGHT)
        test_ph.screens[0][4].append(test_door_ap)
        actual_results = test_ph.available_door_attach_points
        self.assertEqual(1, len(actual_results), "available_door_attach_points returned incorrect number of results!")
        self.assertEqual(test_door_ap, actual_results[0], "available_door_attach_points returned incorrect attach point!")

    def test_attached_door_attach_points(self):
        test_ph = tr_room_placeholder.TRRoomPlaceholder(1, 2)
        expected_results = []
        actual_results = test_ph.attached_door_attach_points
        self.assertEqual(expected_results, actual_results, "TRRoomPlaceholder did not return correct attached_door_attach_points!")

        test_ph = tr_room_placeholder.TRRoomPlaceholder(9, 5)
        test_door_ap = tr_door_attach_point.TRDoorAttachPoint(0, 4, DoorEjectDirection.DOWN)
        test_ph.screens[0][4].append(test_door_ap)
        expected_results = []
        actual_results = test_ph.attached_door_attach_points
        self.assertEqual(expected_results, actual_results, "TRRoomPlaceholder did not return correct attached_door_attach_points!")

        test_farside_room = tr_room_placeholder.TRRoomPlaceholder(2, 2)
        test_farside_door_ap = tr_door_attach_point.TRDoorAttachPoint(1, 1, DoorEjectDirection.UP)
        test_farside_room.screens[1][1].append(test_farside_door_ap)
        test_door_ap.attach(test_farside_room, test_farside_door_ap)
        actual_results = test_ph.attached_door_attach_points
        self.assertEqual(1, len(actual_results), msg="attached_door_attach_points returned incorrect number of results!")
        self.assertEqual(test_door_ap, actual_results[0], "attached_door_attach_points returned incorrect attach point!")