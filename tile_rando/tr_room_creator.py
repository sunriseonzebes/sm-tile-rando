from .tr_map_grid import TRMapGrid

class TRRoomCreator:
    def __init__(self):
        self.rooms = None

    def generate_map_grid(self):
        if not 0x791f8 in self.rooms.keys():
            raise RequiredRoomMissingError("0x791f8 is a required room.")
        return_grid = TRMapGrid(25, 15)

        return return_grid


class RequiredRoomMissingError(Exception):
    """Raised when a required room is not present in the TektonRoomDictionary object."""
    pass
