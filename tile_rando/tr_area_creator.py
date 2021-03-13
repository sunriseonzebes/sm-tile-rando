import random
from tekton.tekton_door import DoorExitDirection
from .tr_map_grid import TRMapGrid
from .tr_room_placeholder import TRRoomPlaceholder
from .tr_room_generator import TRSimpleBoxRoomGenerator
from .tr_door_attach_point import TRDoorAttachPoint

class TRAreaCreator:
    def __init__(self):
        self.source_rooms = None

    def generate_map_grid(self):
        if not 0x791f8 in self.source_rooms.keys():
            raise RequiredRoomMissingError("0x791f8 is a required room.")

        return_grid = TRMapGrid(35, 20)
        landing_site_coords = self._get_landing_site_coords(return_grid.width, return_grid.height)

        self.source_rooms[0x791f8].write_level_data = False
        return_grid.add_room_placeholder(self._create_landing_site_placeholder(self.source_rooms[0x791f8]),
                                         landing_site_coords[0],
                                         landing_site_coords[1])

        #for i in range(1):


        return return_grid

    def _get_landing_site_coords(self, grid_width, grid_height):
        room_width = 9
        room_height = 5

        x_coord = random.randint(3, grid_width - room_width)
        y_coord = random.randint(3, grid_height - room_height)
        return x_coord, y_coord

    def _create_landing_site_placeholder(self, landing_site_tekton_room):
        placeholder = TRRoomPlaceholder(9, 5)
        placeholder.tekton_room = landing_site_tekton_room
        placeholder.screens[0][4] = TRDoorAttachPoint(0, 4, DoorExitDirection.RIGHT)  # Door to Parlor

        return placeholder

    def _create_room_placeholder(self):
        placeholder = TRRoomPlaceholder()
        placeholder.room_generator = TRSimpleBoxRoomGenerator()
        placeholder.width = placeholder.room_generator.generate_room_width()
        placeholder.width = placeholder.room_generator.generate_room_height()
        placeholder.available_door_attach_points = placeholder.room_generator.generate_door_attach_points()

        return placeholder

    # def _find_legal_attach_point(self, existing_placeholder, new_placeholder):
    #     existing_remaining_ap = existing_placeholder.available_door_attach_points
    #
    #     while len(existing_remaining_ap) > 0:
    #         new_remaining_ap = new_placeholder.available_door_attach_points
    #         while len(new_remaining_ap) > 0:







class RequiredRoomMissingError(Exception):
    """Raised when a required room is not present in the TektonRoomDictionary object."""
    pass