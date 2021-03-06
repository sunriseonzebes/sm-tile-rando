import random

from tekton.tekton_door import DoorEjectDirection
from tekton.tekton_tile import TektonTile
from tekton.tekton_tile_grid import TektonTileGrid
from tekton.tekton_room_state import TileSet
from .tr_door_attach_point import TRDoorAttachPoint
from .tr_door_generator import create_classic_door_tile_grid

class TRRoomGenerator:
    def __init__(self):
        pass

    def generate_room_width(self):
        pass

    def generate_room_height(self):
        pass

    def generate_door_attach_points(self):
        pass

    def generate_room_tiles(self):
        pass

    def generate_room_tileset(self):
        pass

    def generate_room_background_pointer(self):
        pass

    def generate_room_scrolls_pointer(self, attached_doors):
        pass

    def generate_enemy_set_pointer(self):
        pass

    def generate_plm_set_pointer(self):
        pass

    def generate_room_fx_pointer(self):
        pass

    def delete_room_extra_states(self):
        pass


class TRLandingSiteRoomGenerator(TRRoomGenerator):
    def __init__(self):
        super(TRLandingSiteRoomGenerator, self).__init__()
        self._width = 9
        self._height = 5

    def generate_room_width(self):
        self._width = 9
        return self._width

    def generate_room_height(self):
        self._height = 5
        return self._height

    def generate_door_attach_points(self):
        if self._width is None:
            self.generate_room_width()
        if self._height is None:
            self.generate_room_height()
        attach_points = [[[] for row in range(self._height)] for col in range(self._width)]
        attach_points[0][4].append(TRDoorAttachPoint(0, 4, DoorEjectDirection.LEFT))

        return attach_points

    def generate_room_tiles(self, attached_doors):
        return None

    def generate_room_tileset(self):
        return TileSet.CRATERIA_CAVE

    def generate_room_background_pointer(self):
        return 0xb76a

    def generate_room_scrolls_pointer(self):
        return 0x9283

    def generate_enemy_set_pointer(self):
        return 0x883d

    def generate_plm_set_pointer(self):
        return 0x8000

    def generate_room_fx_pointer(self):
        return 0x80c0

    def delete_room_extra_states(self):
        return False


class TRSimpleBoxRoomGenerator(TRRoomGenerator):
    def __init__(self):
        super(TRSimpleBoxRoomGenerator, self).__init__()
        self._width = None
        self._height = None

    def generate_room_width(self):
        self._width = random.randint(1, 5)
        if self._height is not None and self._width > 2 and self._height > 2:
            self._width = random.randint(1, 5)  # Re-roll on large square rooms to make them less likely.
        return self._width

    def generate_room_height(self):
        self._height = random.randint(1, 5)
        if self._width is not None and self._width > 2 and self._height > 2:
            self._height = random.randint(1, 5)  # Re-roll on large square rooms to make them less likely.
        return self._height

    def generate_door_attach_points(self):
        if self._width is None:
            self.generate_room_width()
        if self._height is None:
            self.generate_room_height()
        attach_points = [[[] for row in range(self._height)] for col in range(self._width)]
        for col in range(self._width):
            for row in range(self._height):
                if row in [0, self._height - 1] or col in [0, self._width - 1]:
                    if row == 0:
                        attach_points[col][row].append(TRDoorAttachPoint(col, row, DoorEjectDirection.UP))
                    if row == self._height - 1:
                        attach_points[col][row].append(TRDoorAttachPoint(col, row, DoorEjectDirection.DOWN))
                    if col == 0:
                        attach_points[col][row].append(TRDoorAttachPoint(col, row, DoorEjectDirection.LEFT))
                    if col == self._width - 1:
                        attach_points[col][row].append(TRDoorAttachPoint(col, row, DoorEjectDirection.RIGHT))

        return attach_points

    def generate_room_tiles(self, attached_doors):
        if self._width is None:
            self.generate_room_width()
        if self._height is None:
            self.generate_room_height()
        new_tiles = TektonTileGrid(self._width * 16, self._height*16)

        transparent_air_tileno = 0x0ff
        metal_block_tileno = 0x2e0

        bg_tile = TektonTile()
        bg_tile.tileno = transparent_air_tileno
        bg_tile.bts_type = 0x00

        block_tile = TektonTile()
        block_tile.tileno = metal_block_tileno
        block_tile.bts_type = 0x08

        new_tiles.fill(bg_tile)

        # Make a border of blocks around the room.
        for x in range(3):
            for y in range(new_tiles.height):
                new_tiles[x][y] = block_tile.copy()
        for x in range(new_tiles.width - 3, new_tiles.width):
            for y in range(new_tiles.height):
                new_tiles[x][y] = block_tile.copy()
        for x in range(new_tiles.width):
            for y in range(3):
                new_tiles[x][y] = block_tile.copy()
        for x in range(new_tiles.width):
            for y in range(new_tiles.height - 3, new_tiles.height):
                new_tiles[x][y] = block_tile.copy()

        for i in range(len(attached_doors)):
            door_depth = 2
            if attached_doors[i].eject_direction == DoorEjectDirection.UP or attached_doors[i].eject_direction == DoorEjectDirection.DOWN:
                door_depth = 3
            new_door_grid = create_classic_door_tile_grid(attached_doors[i].eject_direction, door_depth, i)
            new_door_x_coord = attached_doors[i].h_screen * 16
            new_door_y_coord = attached_doors[i].v_screen * 16
            if attached_doors[i].eject_direction == DoorEjectDirection.RIGHT:
                new_door_x_coord += 14
                new_door_y_coord += 6
                for j in range(new_door_y_coord, new_door_y_coord + 4):
                    new_tiles[new_door_x_coord-1][j].tileno = transparent_air_tileno
                    new_tiles[new_door_x_coord-1][j].bts_type = 0x00
            if attached_doors[i].eject_direction == DoorEjectDirection.LEFT:
                new_door_y_coord += 6
                for j in range(new_door_y_coord, new_door_y_coord + 4):
                    new_tiles[new_door_x_coord+2][j].tileno = transparent_air_tileno
                    new_tiles[new_door_x_coord+2][j].bts_type = 0x00
            if attached_doors[i].eject_direction == DoorEjectDirection.DOWN:
                new_door_x_coord += 6
                new_door_y_coord += 13
                for j in range(new_door_x_coord, new_door_x_coord + 4):
                    new_tiles[j][new_door_y_coord-1].tileno = transparent_air_tileno
                    new_tiles[j][new_door_y_coord-1].bts_type = 0x00
            if attached_doors[i].eject_direction == DoorEjectDirection.UP:
                new_door_x_coord += 6
                for j in range(new_door_x_coord, new_door_x_coord + 4):
                    new_tiles[j][new_door_y_coord+2].tileno = transparent_air_tileno
                    new_tiles[j][new_door_y_coord+2].bts_type = 0x00
                for j in range(new_door_y_coord+8, new_tiles.height, 7):
                    for k in range(new_door_x_coord, new_door_x_coord + 4):
                        new_tiles[k][j].tileno = metal_block_tileno
                        new_tiles[k][j].bts_type = 0x08
            new_tiles.overwrite_with(new_door_grid, new_door_x_coord, new_door_y_coord)

        return new_tiles

    def generate_room_tileset(self):
        return random.choice([TileSet.CRATERIA_TECH, TileSet.CRATERIA_TECH_DARK])

    def generate_room_background_pointer(self):
        return random.choice([0xb93b, 0xb8ea, 0xb920, 0xb8cf])

    def generate_room_scrolls_pointer(self):
        return 0x1111

    def generate_enemy_set_pointer(self):
        return 0x9f5e  # Statue Hallway, 0x7a5ed

    def generate_plm_set_pointer(self):
        return 0x8246  # Crateria Tube, 0x795d4

    def generate_room_fx_pointer(self):
        return 0x83f2

    def delete_room_extra_states(self):
        return True
