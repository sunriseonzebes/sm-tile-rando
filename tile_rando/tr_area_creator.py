import random
from .tr_map_grid import TRMapGrid

class TRAreaCreator:
    def __init__(self):
        self.rooms = None

    def generate_map_grid(self):
        if not 0x791f8 in self.rooms.keys():
            raise RequiredRoomMissingError("0x791f8 is a required room.")

        return_grid = TRMapGrid(35, 20)
        landing_site_coords = self._get_landing_site_coords(return_grid.width, return_grid.height)
        print(landing_site_coords)

        self.rooms[0x791f8].write_level_data = False
        return_grid.add_room(self.rooms[0x791f8], landing_site_coords[0], landing_site_coords[1])

        return return_grid

    def _get_landing_site_coords(self, grid_width, grid_height):
        room_width = 9
        room_height = 5

        x_coord = random.randint(3, grid_width - room_width)
        y_coord = random.randint(3, grid_height - room_height)
        return x_coord, y_coord



class RequiredRoomMissingError(Exception):
    """Raised when a required room is not present in the TektonRoomDictionary object."""
    pass
