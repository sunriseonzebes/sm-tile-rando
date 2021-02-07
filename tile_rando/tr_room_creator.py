from .tr_map_grid import TRMapGrid

class TRRoomCreator:
    def __init__(self):
        self.rooms = None

    def generate_map_grid(self):
        return_grid = TRMapGrid()

        return return_grid