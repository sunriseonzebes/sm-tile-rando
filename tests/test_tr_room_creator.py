import os
import unittest
from testing_common import tile_rando, original_rom_path, load_test_data_dir

from tile_rando import tr_room_creator


class TestTRRoomCreator(unittest.TestCase):
    def test_init(self):
        test_creator = tr_room_creator.TRRoomCreator()
        self.assertTrue(isinstance(test_creator, tr_room_creator.TRRoomCreator),
                        msg="TRRoomCreator did not initialize properly!")
        self.assertIsNone(test_creator.rooms,
                          msg="TRRoomCreator rooms did not initialize properly!")
