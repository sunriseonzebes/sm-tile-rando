# Super Metroid Tile Randomizer
Infinitely diverse worlds at the click of a button

## What does it do?
SM-Tile-Rando modifies Super Metroid ROMS with procedurally generated randomized maps. This is not a door rando or a route rando - the rooms themselves are randomized, creating new, never-before-seen rooms.

At the moment, this is an extremely early WIP and has very limited functionality. It cannot place enemies or powerups, and the rooms it creates are largely empty, except for doors to other rooms. Lots more functionality is planned for the future.

## That's it? That's all it does?
For now, yes. I'm working on it. ROM hacking is hard :)

## Dependencies
SM-Tile-Rando requires [Tekton](https://github.com/sunriseonzebes/tekton). 

## Usage

    python -m tile_rando -i <path_to_original_rom> -o <output_rom_path>

## Tests

    python -m unittest discover -s tests

The test suite requires the end user to put a copy of the original Super Metroid ROM at **tests/fixtures/original_rom.sfc**

The ROM's md5 checksum should be **21f3e98df4780ee1c667b84e57d88675**