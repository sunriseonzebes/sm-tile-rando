class TRDoorAttachPoint:
    def __init__(self, new_h_screen=0, new_v_screen=0, new_exit_direction=None):
        self.h_screen = new_h_screen
        self.v_screen = new_h_screen
        self.exit_direction = new_exit_direction
        self.farside_room = None
        self.farside_door = None

    @property
    def is_attached(self):
        return self.farside_room is not None and self.farside_door is not None
