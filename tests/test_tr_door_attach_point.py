import os
import unittest
from testing_common import tile_rando

from tekton.tekton_door import DoorEjectDirection
from tile_rando import tr_door_attach_point, tr_room_placeholder


class TestTRDoorAttachPoint(unittest.TestCase):
    def test_init(self):
        test_ap = tr_door_attach_point.TRDoorAttachPoint()
        self.assertTrue(isinstance(test_ap, tr_door_attach_point.TRDoorAttachPoint),
                        msg="TRDoorAttachPoint did not initialize correctly!")
        self.assertEqual(0, test_ap.h_screen, "TRDoorAttachPoint h_screen did not initialize correctly!")
        self.assertEqual(0, test_ap.v_screen, "TRDoorAttachPoint v_screen did not initialize correctly!")
        self.assertIsNone(test_ap.eject_direction, "TRDoorAttachPoint eject_direction did not initialize correctly!")
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

    def test_attach(self):
        test_ph_1 = tr_room_placeholder.TRRoomPlaceholder()
        test_ap_1 = tr_door_attach_point.TRDoorAttachPoint(0, 0, DoorEjectDirection.RIGHT)
        test_ph_1.screens[0][0].append(test_ap_1)

        test_ph_2 = tr_room_placeholder.TRRoomPlaceholder()
        test_ap_2 = tr_door_attach_point.TRDoorAttachPoint(0, 0, DoorEjectDirection.LEFT)
        test_ph_2.screens[0][0].append(test_ap_2)

        test_ap_1.attach(test_ph_2, test_ap_2)
        self.assertEqual(test_ph_2, test_ap_1.farside_room, "Door did not attach correctly to farside room!")
        self.assertEqual(test_ap_2, test_ap_1.farside_door, "Door did not attach correctly to farside room!")

        test_ph_3 = tr_room_placeholder.TRRoomPlaceholder()
        test_ap_3 = tr_door_attach_point.TRDoorAttachPoint(0, 0, DoorEjectDirection.UP)
        test_ph_3.screens[0][0].append(test_ap_3)

        with self.assertRaises(tr_door_attach_point.InvalidDoorAttachError):
            test_ap_1.attach(test_ph_3, test_ap_3)

        with self.assertRaises(TypeError):
            test_ap_2.attach("Landing Site", test_ap_1)
        with self.assertRaises(TypeError):
            test_ap_2.attach(test_ph_1, 0)

