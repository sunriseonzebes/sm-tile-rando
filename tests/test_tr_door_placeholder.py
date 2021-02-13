import os
import unittest
from testing_common import tile_rando

from tekton import tekton_door
from tile_rando import tr_door_placeholder


class TestTRDoorPlaceholder(unittest.TestCase):
    def test_init(self):
        test_ph = tr_door_placeholder.TRDoorPlaceholder()
        self.assertTrue(isinstance(test_ph, tr_door_placeholder.TRDoorPlaceholder),
                        msg="TRDoorPlaceholder did not initialize correctly!")
        self.assertEqual(0, test_ph.h_screen, "TRDoorPlaceholder h_screen did not initialize correctly!")
        self.assertEqual(0, test_ph.v_screen, "TRDoorPlaceholder v_screen did not initialize correctly!")
        self.assertIsNone(test_ph.exit_direction, "TRDoorPlaceholder exit_direction did not initialize correctly!")
