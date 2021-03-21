import argparse
import os
import sys
from .tr_config import TRConfig
from .tr_area_creator import TRAreaCreator

from tekton.tekton_project import TektonProject

class TRProject:
    def __init__(self):
        self.original_rom_path = ""
        self.modified_rom_path = ""
        self.config = TRConfig()

        self._tekton_project = TektonProject()

    def parse_args(self, new_args=None):
        if new_args is None:
            new_args = sys.argv[1:]

        parser = argparse.ArgumentParser(
            description='Randomize tiles, rooms, map structure and powerups of a Super Metroid ROM.'
        )
        parser.add_argument('-i',
                            metavar="<input_rom_file>",
                            type=str,
                            required=True,
                            help="Path to unmodified ROM to use as a source file.")
        parser.add_argument('-o', metavar="<output_rom_file>",
                            type=str,
                            required=True,
                            help="Path to write modified ROM to.")
        parser.add_argument('--seed', metavar="<randomizer_seed>",
                            type=str,
                            help="Seed to use for the tile randomizer. If not specified, a random seed is chosen.")
        args = parser.parse_args(new_args)

        self.original_rom_path = args.i
        self.modified_rom_path = args.o
        if args.seed is not None:
            self.config.seed = args.seed

    def randomize(self):
        self._init_tekton_project()
        area_creator = TRAreaCreator()
        area_creator.source_rooms = self._tekton_project.rooms
        area_creator.generate_map_grid()
        modified_rom_contents = self._tekton_project.get_modified_rom_contents()
        self._write_bytes_to_output_file(modified_rom_contents)

    def _init_tekton_project(self):
        self._tekton_project.source_rom_path = self.original_rom_path
        header_address_file = os.path.join(os.path.dirname(__file__), 'rando_source_rooms.yaml')
        self._tekton_project.import_rooms(header_address_file)


    def _write_bytes_to_output_file(self, bytes_string):
        with open(self.modified_rom_path, 'wb') as outfile:
            outfile.write(bytes_string)
