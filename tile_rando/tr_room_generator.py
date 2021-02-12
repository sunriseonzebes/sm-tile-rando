import random

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

    # def generate_door_attach_points(self):
    #     attach_points = []
    #     if self._height
    #     for col in range(self._width):
    #         attach_points.append((col, 0))
    #         attach_points.append((col, self._height - 1))
    #     for row in range(1, self._height - 1):
    #         attach_points.append((col, 0))
    #         attach_points.append((col, self._height - 1))

