import argparse
import sys


class TRProject:
    def __init__(self):
        self.original_rom_path = ""
        self.modified_rom_path = ""

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
        args = parser.parse_args(new_args)

        self.original_rom_path = args.i
        self.modified_rom_path = args.o
