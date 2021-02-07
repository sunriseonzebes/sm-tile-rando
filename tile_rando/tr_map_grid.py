class TRMapGrid:
    def __init__(self, width=1, height=1):
        self._squares = [[None for row in range(height)] for col in range(width)]

    def __getitem__(self, item):
        return self._squares[item]

    @property
    def width(self):
        return len(self._squares)

    @property
    def height(self):
        return len(self._squares[0])

    def add_room(self, new_room, x_position, y_position):
        if new_room.width_screens + x_position > self.width or \
                new_room.height_screens + y_position > self.height:
            raise RoomExceedsGridBoundariesError
        for col in range(x_position, x_position+new_room.width_screens):
            for row in range(y_position, y_position+new_room.height_screens):
                self._squares[col][row] = new_room


class RoomExceedsGridBoundariesError(Exception):
    """Exception raised when adding a room that goes past the boundaries of the TRMapGrid."""
    pass
