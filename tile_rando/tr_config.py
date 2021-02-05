import os

class TRConfig:
    def __init__(self):
        self.original_rom_path = ""
        self.modified_rom_path = ""
        self._seed = None

    @property
    def seed(self):
        return self._seed

    @seed.setter
    def seed(self, new_seed):
        if not isinstance(new_seed, str):
            try:
                new_seed = str(new_seed)
            except Exception as e:
                raise TypeError("seed must be of type str!")
        self._seed = new_seed