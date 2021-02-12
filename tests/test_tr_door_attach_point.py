import os
import unittest
from testing_common import tile_rando

from tekton import tekton_door
from tile_rando import tr_door_attach_point

class TestTRDoorAttachPoint(unittest.TestCase):
    def test_init(self):
        test_attach = tr_door_attach_point.TRDoorAttachPoint(4, 2, [])
        self.assertTrue(isinstance(test_attach, tr_door_attach_point.TRDoorAttachPoint),
                        msg="TRDoorAttachPoint did not initialize correctly!")
        self.assertEqual(4, test_attach.h_screen, "TRDoorAttachPoint h_screen did not initialize correctly!")
        self.assertEqual(2, test_attach.v_screen, "TRDoorAttachPoint v_screen did not initialize correctly!")
        self.assertEqual([],
                         test_attach.allowed_door_exit_directions,
                         "TRDoorAttachPoint allowed_door_exit_directions did not initialize correctly!")