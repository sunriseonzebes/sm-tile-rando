import random

from tekton.tekton_door import DoorExitDirection
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

    def generate_room_width(self):
        self._width = random.randint(1, 5)
        return self._width

    def generate_room_height(self):
        self._height = random.randint(1, 5)
        return self._height

    def generate_door_attach_points(self):
        attach_points = []
        for col in range(self._width):
            for row in range(self._height):
                if row in [0, self._height - 1] or \
                        col in [0, self._width - 1]:
                    new_attach_point = TRDoorAttachPoint(col, row, [])
                    if row == 0:
                        new_attach_point.allowed_door_exit_directions.append(DoorExitDirection.UP)
                    if row == self._height - 1:
                        new_attach_point.allowed_door_exit_directions.append(DoorExitDirection.DOWN)
                    if col == 0:
                        new_attach_point.allowed_door_exit_directions.append(DoorExitDirection.LEFT)
                    if col == self._width - 1:
                        new_attach_point.allowed_door_exit_directions.append(DoorExitDirection.RIGHT)
                    attach_points.append(new_attach_point)

        return attach_points
