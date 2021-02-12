import os
import unittest
from testing_common import tile_rando

from tile_rando import tr_room_generator

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
