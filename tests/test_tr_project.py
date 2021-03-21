import hashlib
import os
import unittest
from testing_common import tile_rando, original_rom_path, load_test_data_dir

from tile_rando import tr_project, tr_config
from tekton import tekton_project

class TestTRProject(unittest.TestCase):
    def test_init(self):
        test_project = tr_project.TRProject()
        self.assertTrue(isinstance(test_project, tr_project.TRProject))
        self.assertEqual("", test_project.original_rom_path, "TRProject _original_rom_path did not initialize properly!")
        self.assertEqual("", test_project.modified_rom_path, "TRProject _modified_rom_path did not initialize properly!")
        self.assertTrue(isinstance(test_project.config, tr_config.TRConfig),
                        msg="TRProject config did not initialize properly!")
        self.assertTrue(isinstance(test_project._tekton_project, tekton_project.TektonProject),
                        msg="TRProject _tekton_project did not initialize properly!")

    def test_parse_args(self):
        test_project = tr_project.TRProject()
        test_project.parse_args(['-i', 'original_rom.sfc', '-o', 'modified_rom.sfc'])
        self.assertEqual('original_rom.sfc',
                         test_project.original_rom_path,
                         "parse_args did not load original_rom_path correctly!")
        self.assertEqual('modified_rom.sfc',
                         test_project.modified_rom_path,
                         "parse_args did not load modified_rom_path correctly!")
        with self.assertRaises(SystemExit):
            test_project.parse_args([])
        with self.assertRaises(SystemExit):
            test_project.parse_args(['-t', 'nonsense_arg'])
        with self.assertRaises(SystemExit):
            test_project.parse_args(['-i', 'original_rom.sfc'])
        with self.assertRaises(SystemExit):
            test_project.parse_args(['-o', 'modified_rom.sfc'])
        test_project = tr_project.TRProject()
        test_project.parse_args(['-i', 'original_rom.sfc', '-o', 'modified_rom.sfc', '--seed', '54321'])
        self.assertEqual('original_rom.sfc',
                         test_project.original_rom_path,
                         "parse_args did not load original_rom_path correctly!")
        self.assertEqual('modified_rom.sfc',
                         test_project.modified_rom_path,
                         "parse_args did not load modified_rom_path correctly!")
        self.assertEqual('54321',
                         test_project.config.seed,
                         "parse_args did not load config.seed correctly!")

    def test_write_bytes_to_output_file(self):
        test_project = tr_project.TRProject()
        expected_result = b'\x00\x11\x22\x33'

        test_rom_path = os.path.join('fixtures', 'test_output_rom.sfc')

        test_project.modified_rom_path = test_rom_path
        test_project._write_bytes_to_output_file(expected_result)

        with open(test_rom_path, 'rb') as f:
            actual_result = f.read()
        self.assertEqual(expected_result,
                         actual_result,
                         "TRProject.write_bytes_to_output_file did not write correct byte sequence!")

    def test_init_tekton_project(self):
        test_project = tr_project.TRProject()
        test_project.original_rom_path = original_rom_path

        test_rom_path = os.path.join('fixtures', 'test_output_rom.sfc')
        test_project.modified_rom_path = test_rom_path

        test_project._init_tekton_project()

        self.assertEqual(original_rom_path,
                         test_project._tekton_project.source_rom_path,
                         "TektonProject object has wrong source_rom_path!")
