from .tr_door_attach_point import TRDoorAttachPoint

class TRRoomPlaceholder:
    def __init__(self, width=1, height=1):
        self.tekton_room = None
        self.room_generator = None
        self.width = width
        self.height = height
        self.screens = [[[] for row in range(self.height)] for col in range(self.width)]

    @property
    def available_door_attach_points(self):
        available_attach_points = []
        for row in range(self.height):
            for col in range(self.width):
                for attach_point in self.screens[col][row]:
                    if not isinstance(attach_point, TRDoorAttachPoint):
                        continue
                    if not attach_point.is_attached:
                        available_attach_points.append(attach_point)

        return available_attach_points

    def generate_room_attributes(self):
        self.width = self.room_generator.generate_room_width()
        self.height = self.room_generator.generate_room_height()
        self.screens = [[[] for row in range(self.height)] for col in range(self.width)]
        door_attach_points = self.room_generator.generate_door_attach_points()
        for col in range(len(door_attach_points)):
            for row in range(len(door_attach_points[col])):
                self.screens[col][row] += door_attach_points[col][row]
        self.tekton_room.tiles = self.room_generator.generate_room_tiles(self.screens)