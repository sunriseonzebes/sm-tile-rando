class TRDoorPlaceholder:
    def __init__(self, new_h_screen=0, new_v_screen=0, new_exit_direction=None):
        self.h_screen = new_h_screen
        self.v_screen = new_h_screen
        self.exit_direction = new_exit_direction


class TRDoorAttachPoint:
    def __init__(self, new_h_screen, new_v_screen, new_allowed_directions):
        self.h_screen = new_h_screen
        self.v_screen = new_v_screen
        self.allowed_door_exit_directions = new_allowed_directions
