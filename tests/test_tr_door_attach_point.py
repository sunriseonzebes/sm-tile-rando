import os
import unittest
from testing_common import tile_rando

from tekton import tekton_door
from tile_rando import tr_door_attach_point

class TestTRDoorAttachPoint(unittest.TestCase):
    def test_init(self):
        test_attach = tr_door_attach_point.TRDoorAttachPoint()
        self.assertTrue(isinstance(test_attach, tr_door_attach_point.TRDoorAttachPoint),
                        msg="TRDoorAttachPoint did not initialize correctly!")
        self.assertEqual(0, test_attach.h_screen, "TRDoorAttachPoint h_screen did not initialize correctly!")
        self.assertEqual(0, test_attach.v_screen, "TRDoorAttachPoint v_screen did not initialize correctly!")
        self.assertEqual([],
                         test_attach.allowed_door_exit_directions,
                         "TRDoorAttachPoint door_exit_direction did not initialize correctly!")