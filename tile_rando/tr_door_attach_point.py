class TRDoorAttachPoint:
    def __init__(self, new_h_screen=0, new_v_screen=0, new_eject_direction=None):
        self.h_screen = new_h_screen
        self.v_screen = new_v_screen
        self.eject_direction = new_eject_direction
        self.farside_room = None
        self.farside_door = None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "TRDoorAttachPoint ({h}, {v})".format(h=self.h_screen, v=self.v_screen)

    @property
    def is_attached(self):
        return self.farside_room is not None and self.farside_door is not None
