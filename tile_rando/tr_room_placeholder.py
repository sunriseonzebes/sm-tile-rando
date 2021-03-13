from .tr_door_attach_point import TRDoorAttachPoint

class TRRoomPlaceholder:
    def __init__(self, width=1, height=1):
        self.tekton_room = None
        self.room_generator = None
        self.width = width
        self.height = height
        self.screens = [[[None] for row in range(self.height)] for col in range(self.width)]

    @property
    def available_door_attach_points(self):
        available_attach_points = []
        for col in range(len(self.screens)):
            for row in range(len(self.screens[col])):
                for attach_point in self.screens[col][row]:
                    if not isinstance(attach_point, TRDoorAttachPoint):
                        continue
                    if attach_point.is_attached:
                        available_attach_points.append(attach_point)

        return available_attach_points