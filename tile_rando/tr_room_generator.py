import random

from tekton.tekton_door import DoorExitDirection
from .tr_door_placeholder import TRDoorPlaceholder

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
        return self._width

    def generate_room_height(self):
        self._height = random.randint(1, 5)
        return self._height

    def generate_num_doors(self):
        self._num_doors = 1 + random.randint(0, max(1, (self._width*self._height) // 8))
        return self._num_doors

    def generate_door_attach_points(self):
        attach_points = []
        for col in range(self._width):
            for row in range(self._height):
                if row in [0, self._height - 1] or col in [0, self._width - 1]:
                    if row == 0:
                        attach_points.append(TRDoorPlaceholder(col, row, DoorExitDirection.DOWN))
                    if row == self._height - 1:
                        attach_points.append(TRDoorPlaceholder(col, row, DoorExitDirection.UP))
                    if col == 0:
                        attach_points.append(TRDoorPlaceholder(col, row, DoorExitDirection.RIGHT))
                    if col == self._width - 1:
                        attach_points.append(TRDoorPlaceholder(col, row, DoorExitDirection.LEFT))

        return attach_points
