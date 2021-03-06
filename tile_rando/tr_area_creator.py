import random
from tekton.tekton_door import DoorEjectDirection
from .tr_map_grid import TRMapGrid
from .tr_room_placeholder import TRRoomPlaceholder
from .tr_room_generator import TRSimpleBoxRoomGenerator, TRLandingSiteRoomGenerator
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

        while len(return_grid.rooms) < len(self.source_rooms.values()):
            new_placeholder = self._create_room_placeholder(return_grid.rooms)
            remaining_existing_placeholders = return_grid.rooms.copy()
            while len(remaining_existing_placeholders) > 0:
                existing_placeholder = random.choice(remaining_existing_placeholders)
                new_placeholder_coords, existing_ap, new_ap = return_grid.find_room_attach_coords(existing_placeholder, new_placeholder)
                if new_placeholder_coords is not None:
                    return_grid.add_room_placeholder(new_placeholder, new_placeholder_coords[0], new_placeholder_coords[1])
                    existing_ap.attach(new_placeholder, new_ap)
                    new_ap.attach(existing_placeholder, existing_ap)
                    break
                remaining_existing_placeholders.remove(existing_placeholder)
                print("Could not find anywhere to put placeholder!")

        return_grid.generate_rooms_tiles()
        return_grid.generate_tekton_doors()

        print(return_grid)
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
        placeholder.room_generator = TRLandingSiteRoomGenerator()
        placeholder.generate_room_attributes()

        return placeholder

    def _create_room_placeholder(self, used_rooms):
        placeholder = TRRoomPlaceholder()
        placeholder.room_generator = TRSimpleBoxRoomGenerator()
        used_headers = [room.tekton_room.header for room in used_rooms]
        available_source_room_headers = [header for header in self.source_rooms.keys() if header not in used_headers]
        if len(available_source_room_headers) < 1:
            raise ValueError("No source rooms left to randomize!")
        placeholder.tekton_room = self.source_rooms[random.choice(available_source_room_headers)]

        placeholder.generate_room_attributes()

        return placeholder


class RequiredRoomMissingError(Exception):
    """Raised when a required room is not present in the TektonRoomDictionary object."""
    pass
