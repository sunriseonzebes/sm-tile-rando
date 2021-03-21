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
