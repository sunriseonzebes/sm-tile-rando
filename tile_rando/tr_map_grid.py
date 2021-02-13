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
                    return_string += 'X '
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


class RoomExceedsGridBoundariesError(Exception):
    """Exception raised when adding a room that goes past the boundaries of the TRMapGrid."""
    pass
