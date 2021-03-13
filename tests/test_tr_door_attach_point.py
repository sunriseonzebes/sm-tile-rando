import os
import unittest
from testing_common import tile_rando

from tekton import tekton_door
from tile_rando import tr_door_attach_point, tr_room_placeholder


class TestTRDoorAttachPoint(unittest.TestCase):
    def test_init(self):
        test_ap = tr_door_attach_point.TRDoorAttachPoint()
        self.assertTrue(isinstance(test_ap, tr_door_attach_point.TRDoorAttachPoint),
                        msg="TRDoorAttachPoint did not initialize correctly!")
        self.assertEqual(0, test_ap.h_screen, "TRDoorAttachPoint h_screen did not initialize correctly!")
        self.assertEqual(0, test_ap.v_screen, "TRDoorAttachPoint v_screen did not initialize correctly!")
        self.assertIsNone(test_ap.exit_direction, "TRDoorAttachPoint exit_direction did not initialize correctly!")
        self.assertIsNone(test_ap.farside_room, "TRDoorAttachPoint farside_room did not initialize correctly!")
        self.assertIsNone(test_ap.farside_door, "TRDoorAttachPoint farside_door did not initialize correctly!")

    def test_is_attached(self):
        test_ap = tr_door_attach_point.TRDoorAttachPoint()
        second_ap = tr_door_attach_point.TRDoorAttachPoint()
        test_room_ph = tr_room_placeholder.TRRoomPlaceholder()
        self.assertFalse(test_ap.is_attached, msg="TRDoorAttachPoint did not return correct attached status!")

        test_ap.farside_door = second_ap
        self.assertFalse(test_ap.is_attached, msg="TRDoorAttachPoint did not return correct attached status!")

        test_ap.farside_room = test_room_ph
        self.assertTrue(test_ap.is_attached, msg="TRDoorAttachPoint did not return correct attached status!")
        self.assertFalse(second_ap.is_attached, msg="TRDoorAttachPoint did not return correct attached status!")