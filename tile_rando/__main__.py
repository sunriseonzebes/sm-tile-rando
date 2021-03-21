import argparse
import sys
from .tr_project import TRProject


def parse_args(new_args=None):
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
                        required=False,
                        help="Seed to use for the tile randomizer. If not specified, a random seed is chosen.")
    args = parser.parse_args(new_args)

    return args


def main():
    project = TRProject()
    args = parse_args()
    project.original_rom_path = args.i
    project.modified_rom_path = args.o
    if args.seed is not None:
        project.config.seed = args.seed
    project.randomize()


if __name__ == "__main__":
    main()
