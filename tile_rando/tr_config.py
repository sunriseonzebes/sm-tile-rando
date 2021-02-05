import os

class TRConfig:
    def __init__(self):
        self._original_rom_path = ""
        self._modified_rom_path = ""
        self._seed = None

    @property
    def original_rom_path(self):
        """str: The path to the original rom file."""
        return self._original_rom_path

    @original_rom_path.setter
    def original_rom_path(self, new_rom_path):
        if not os.path.exists(new_rom_path):
            raise OSError("{} does not exist!".format(new_rom_path))
        self._original_rom_path = new_rom_path