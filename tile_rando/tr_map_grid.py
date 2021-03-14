import random
from tekton.tekton_door import DoorExitDirection


class TRMapGrid:
    def __init__(self, width=1, height=1):
        self._squares = [[None for row in range(height)] for col in range(width)]
        self.rooms = []

    def __repr__(self):
        print(self.__str__())

    def __str__(self):
        return_string = "TRMapGrid Object:\n"
        for row in range(self.height):
            for col in range(self.width):
                if self._squares[col][row] is None:
                    return_string += '. '
                else:
                    for i in range(len(self.rooms)):
                        if self.rooms[i] == self._squares[col][row]:
                            return_string += '{} '.format(i)
            return_string += "\n"
        return_string += "\n"

        return return_string

    def __getitem__(self, item):
        return self._squares[item]

    @property
    def width(self):
        return len(self._squares)

    @property
    def height(self):
        return len(self._squares[0])

    def add_room_placeholder(self, new_room_placeholder, x_position, y_position):
        if new_room_placeholder.width + x_position > self.width or \
                new_room_placeholder.height + y_position > self.height:
            raise RoomExceedsGridBoundariesError
        for col in range(x_position, x_position + new_room_placeholder.width):
            for row in range(y_position, y_position + new_room_placeholder.height):
                self._squares[col][row] = new_room_placeholder
        self.rooms.append(new_room_placeholder)

    def find_room_attach_coords(self, existing_placeholder, new_placeholder):
        remaining_existing_aps = existing_placeholder.available_door_attach_points
        existing_placeholder_coords = self.get_room_top_left_coords(existing_placeholder)

        while len(remaining_existing_aps) > 0:

            existing_ap = random.choice(remaining_existing_aps)
            existing_ap_coords = (existing_placeholder_coords[0] + existing_ap.h_screen,
                                  existing_placeholder_coords[1] + existing_ap.v_screen)
            if existing_ap.exit_direction == DoorExitDirection.RIGHT:
                remaining_new_aps = [ap for ap in new_placeholder.available_door_attach_points if
                                     ap.exit_direction == DoorExitDirection.LEFT]
            elif existing_ap.exit_direction == DoorExitDirection.LEFT:
                remaining_new_aps = [ap for ap in new_placeholder.available_door_attach_points if
                                     ap.exit_direction == DoorExitDirection.RIGHT]
            elif existing_ap.exit_direction == DoorExitDirection.UP:
                remaining_new_aps = [ap for ap in new_placeholder.available_door_attach_points if
                                     ap.exit_direction == DoorExitDirection.DOWN]
            else:
                remaining_new_aps = [ap for ap in new_placeholder.available_door_attach_points if
                                     ap.exit_direction == DoorExitDirection.UP]
            while len(remaining_new_aps) > 0:
                new_ap = random.choice(remaining_new_aps)
                if existing_ap.exit_direction == DoorExitDirection.RIGHT:
                    new_ap_coords = (existing_ap_coords[0] - 1, existing_ap_coords[1])
                elif existing_ap.exit_direction == DoorExitDirection.LEFT:
                    new_ap_coords = (existing_ap_coords[0] + 1, existing_ap_coords[1])
                elif existing_ap.exit_direction == DoorExitDirection.UP:
                    new_ap_coords = (existing_ap_coords[0], existing_ap_coords[1] + 1)
                else:
                    new_ap_coords = (existing_ap_coords[0], existing_ap_coords[1] - 1)
                proposed_room_coord = (new_ap_coords[0] - new_ap.h_screen,
                                           new_ap_coords[1] - new_ap.v_screen)
                if not self.room_placement_in_bounds(new_placeholder, proposed_room_coord[0], proposed_room_coord[1]):
                    print("Room out of bounds")
                elif self.room_placement_overlaps_existing_room(new_placeholder, proposed_room_coord[0], proposed_room_coord[1]):
                    print("Room overlaps existing room!")
                else:
                    return proposed_room_coord
                remaining_new_aps.remove(new_ap)
            remaining_existing_aps.remove(existing_ap)

        return None

    def room_placement_overlaps_existing_room(self, proposed_room, proposed_top_row, proposed_left_col):
        proposed_x_coords = [*range(proposed_top_row, proposed_top_row + proposed_room.width)]
        proposed_y_coords = [*range(proposed_left_col, proposed_left_col + proposed_room.height)]

        for row in proposed_y_coords:
            for col in proposed_x_coords:
                if self._squares[col][row] is not None:
                    return True
        return False

    def room_placement_in_bounds(self, proposed_room, proposed_left_col, proposed_top_row):
        return proposed_top_row >= 0 and \
               proposed_left_col >= 0 and \
               ((proposed_top_row + proposed_room.height) - 1) < self.height and \
               ((proposed_left_col + proposed_room.width) - 1) < self.width

    def get_room_top_left_coords(self, room_placeholder):
        if room_placeholder not in self.rooms:
            return None
        for row in range(self.height):
            for col in range(self.width):
                if self._squares[col][row] == room_placeholder:
                    return col, row
        return None


class RoomExceedsGridBoundariesError(Exception):
    """Exception raised when adding a room that goes past the boundaries of the TRMapGrid."""
    pass
