import random

from tekton.tekton_door import DoorEjectDirection
from tekton.tekton_tile import TektonTile
from tekton.tekton_tile_grid import TektonTileGrid
from .tr_door_attach_point import TRDoorAttachPoint

class TRRoomGenerator:
    def __init__(self):
        pass

    def generate_room_width(self):
        pass

    def generate_room_height(self):
        pass

    def generate_door_attach_points(self, width, height):
        pass

    def generate_room_tiles(self, screen_info):
        pass


class TRSimpleBoxRoomGenerator(TRRoomGenerator):
    def __init__(self):
        super(TRSimpleBoxRoomGenerator, self).__init__()
        self._width = None
        self._height = None
        self._num_doors = 0

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

    def generate_num_doors(self):
        self._num_doors = 1 + random.randint(0, max(1, (self._width*self._height) // 8))
        return self._num_doors

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
                        attach_points[col][row].append(TRDoorAttachPoint(col, row, DoorEjectDirection.DOWN))
                    if row == self._height - 1:
                        attach_points[col][row].append(TRDoorAttachPoint(col, row, DoorEjectDirection.UP))
                    if col == 0:
                        attach_points[col][row].append(TRDoorAttachPoint(col, row, DoorEjectDirection.RIGHT))
                    if col == self._width - 1:
                        attach_points[col][row].append(TRDoorAttachPoint(col, row, DoorEjectDirection.LEFT))

        return attach_points

    def generate_room_tiles(self, screen_info):
        if self._width is None:
            self.generate_room_width()
        if self._height is None:
            self.generate_room_height()
        new_tiles = TektonTileGrid(self._width * 16, self._height*16)

        bg_tile = TektonTile()
        bg_tile.tileno = 0x080
        bg_tile.bts_type = 0x00

        block_tile = TektonTile()
        block_tile.tileno = 0x2e0
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

        # for col in range(len(screen_info)):
        #     for row in range(len(screen_info[row])):
        #         for item in screen_info[col][row]:
        #             if isinstance(item, TRDoorAttachPoint):
        #                 if not item.is_attached:
        #                     continue
        #

        return new_tiles
