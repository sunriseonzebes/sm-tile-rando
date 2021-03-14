import random

from tekton.tekton_door import DoorEjectDirection
from .tr_door_attach_point import TRDoorAttachPoint

class TRRoomGenerator:
    def __init__(self):
        pass

    def generate_room_width(self):
        pass

    def generate_room_height(self):
        pass

    def generate_door_attach_points(self, width, height):
        pass


class TRSimpleBoxRoomGenerator(TRRoomGenerator):
    def __init__(self):
        super(TRSimpleBoxRoomGenerator, self).__init__()
        self._width = 1
        self._height = 1
        self._num_doors = 0

    def generate_room_width(self):
        self._width = random.randint(1, 5)
        if self._width > 2 and self._height > 2:
            self._width = random.randint(1, 5)  # Re-roll on large square rooms to make them less likely.
        return self._width

    def generate_room_height(self):
        self._height = random.randint(1, 5)
        if self._width > 2 and self._height > 2:
            self._height = random.randint(1, 5)  # Re-roll on large square rooms to make them less likely.
        return self._height

    def generate_num_doors(self):
        self._num_doors = 1 + random.randint(0, max(1, (self._width*self._height) // 8))
        return self._num_doors

    def generate_door_attach_points(self):
        attach_points = [[[] for row in range(self._height)] for col in range(self._width)]
        for col in range(self._width):
            for row in range(self._height):
                if row in [0, self._height - 1] or col in [0, self._width - 1]:
                    if row == 0:
                        attach_points[col][row].append(TRDoorAttachPoint(col, row, DoorEjectDirection.DOWN))
                    if row == self._height - 1:
                        attach_points[col][row].append(TRDoorAttachPoint(col, row, DoorEjectDirection.UP))
                    if col == 0:
                        attach_points[col][row].append(TRDoorAttachPoint(col, row, DoorEjectDirection.RIGHT))
                    if col == self._width - 1:
                        attach_points[col][row].append(TRDoorAttachPoint(col, row, DoorEjectDirection.LEFT))

        return attach_points
