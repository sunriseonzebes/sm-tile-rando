import os
import unittest
from testing_common import tile_rando

from tile_rando import tr_room_placeholder

class TestTRRoomPlaceholder(unittest.TestCase):
    def test_init(self):
        test_ph = tr_room_placeholder.TRRoomPlaceholder()
        self.assertTrue(isinstance(test_ph, tr_room_placeholder.TRRoomPlaceholder),
                        msg="TRRoomPlaceholder did not initialize correctly!")
        self.assertIsNone(test_ph.tekton_room, msg="TRRoomPlaceholder did not initialize correctly!")
        self.assertIsNone(test_ph.room_generator, msg="TRRoomPlaceholder did not initialize correctly!")
        self.assertEqual(1, test_ph.width, "TRRoomPlaceholder did not initialize correctly!")
        self.assertEqual(1, test_ph.height, "TRRoomPlaceholder did not initialize correctly!")
        self.assertEqual([], test_ph.possible_door_attach_points, "TRRoomPlaceholder did not initialize correctly!")
        self.assertEqual([], test_ph.door_placeholders, "TRRoomPlaceholder did not initialize correctly!")