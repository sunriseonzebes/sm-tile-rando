import os
import unittest
from testing_common import tile_rando

from tile_rando import tr_room_placeholder

class TestTRRoomPlaceholder(unittest.TestCase):
    def test_init(self):
        test_ph = tr_room_placeholder.TRRoomPlaceholder()
        self.assertTrue(isinstance(test_ph, tr_room_placeholder.TRRoomPlaceholder),
                        msg="TRRoomPlaceholder did not initialize correctly!")