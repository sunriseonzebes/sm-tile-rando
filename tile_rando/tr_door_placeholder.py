class TRDoorPlaceholder:
    def __init__(self):
        self.h_screen = 0
        self.v_screen = 0
        self.exit_direction = None


class TRDoorAttachPoint:
    def __init__(self, new_h_screen, new_v_screen, new_allowed_directions):
        self.h_screen = new_h_screen
        self.v_screen = new_v_screen
        self.allowed_door_exit_directions = new_allowed_directions
