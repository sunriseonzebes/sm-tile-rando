from tekton.tekton_door import DoorEjectDirection
from . import tr_room_placeholder

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

    def attach(self, new_farside_room, new_farside_door):
        if not isinstance(new_farside_room, tr_room_placeholder.TRRoomPlaceholder):
            raise TypeError("new_farside_room must be TRRoomPlaceholder!")
        if not isinstance(new_farside_door, TRDoorAttachPoint):
            raise TypeError("new_farside_door must be TRDoorAttachPoint!")
        if self.eject_direction == DoorEjectDirection.RIGHT and new_farside_door.eject_direction != DoorEjectDirection.LEFT:
            raise InvalidDoorAttachError("Doors must have opposing eject directions! (Left/Right, etc.)")
        if self.eject_direction == DoorEjectDirection.LEFT and new_farside_door.eject_direction != DoorEjectDirection.RIGHT:
            raise InvalidDoorAttachError("Doors must have opposing eject directions! (Left/Right, etc.)")
        if self.eject_direction == DoorEjectDirection.UP and new_farside_door.eject_direction != DoorEjectDirection.DOWN:
            raise InvalidDoorAttachError("Doors must have opposing eject directions! (Left/Right, etc.)")
        if self.eject_direction == DoorEjectDirection.DOWN and new_farside_door.eject_direction != DoorEjectDirection.UP:
            raise InvalidDoorAttachError("Doors must have opposing eject directions! (Left/Right, etc.)")
        self.farside_room = new_farside_room
        self.farside_door = new_farside_door


class InvalidDoorAttachError(Exception):
    """Raised when two door attach points cannot be attached, for example if their eject directions are not opposites."""
    pass
