from .tr_door_attach_point import TRDoorAttachPoint
from .tr_door_generator import create_tekton_door

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

    @property
    def attached_door_attach_points(self):
        attached_attach_points = []
        for row in range(self.height):
            for col in range(self.width):
                for attach_point in self.screens[col][row]:
                    if not isinstance(attach_point, TRDoorAttachPoint):
                        continue
                    if attach_point.is_attached:
                        attached_attach_points.append(attach_point)

        return attached_attach_points

    def generate_room_attributes(self):
        self.width = self.room_generator.generate_room_width()
        self.height = self.room_generator.generate_room_height()
        self.screens = [[[] for row in range(self.height)] for col in range(self.width)]
        self.tekton_room.width_screens = self.width
        self.tekton_room.height_screens = self.height
        door_attach_points = self.room_generator.generate_door_attach_points()
        for col in range(len(door_attach_points)):
            for row in range(len(door_attach_points[col])):
                self.screens[col][row] += door_attach_points[col][row]

        self.tekton_room.standard_state.tileset = self.room_generator.generate_room_tileset()
        self.tekton_room.standard_state.background_pointer = self.room_generator.generate_room_background_pointer()
        self.tekton_room.standard_state.room_scrolls_pointer = self.room_generator.generate_room_scrolls_pointer()
        self.tekton_room.standard_state.enemy_set_pointer = self.room_generator.generate_enemy_set_pointer()
        self.tekton_room.standard_state.fx_pointer = self.room_generator.generate_room_fx_pointer()
        self.tekton_room.standard_state.plm_set_pointer = self.room_generator.generate_plm_set_pointer()
        if self.room_generator.delete_room_extra_states:
            self.tekton_room.extra_states = []


    def generate_room_tiles(self):
        new_tiles = self.room_generator.generate_room_tiles(self.attached_door_attach_points)
        if new_tiles is not None:
            self.tekton_room.standard_state.tiles = new_tiles

    def generate_tekton_doors(self):
        attached_doors = self.attached_door_attach_points
        new_tekton_door_list = []

        for i in range(len(attached_doors)):
            new_tekton_door = create_tekton_door(attached_doors[i])
            if len(self.tekton_room.doors) > i:
                new_tekton_door.data_address = self.tekton_room.doors[i].data_address
            else:
                new_tekton_door.data_address = new_tekton_door_list[i-1].data_address + 12
            new_tekton_door_list.append(new_tekton_door)

        self.tekton_room.doors = new_tekton_door_list
