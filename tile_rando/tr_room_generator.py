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

    def generate_room_tiles(self, attached_doors):
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
        self._width = weighted_random([(1, 0.5),
                                       (2, 0.4),
                                       (3, 0.3),
                                       (4, 0.2),
                                       (5, 0.1)])
        return self._width

    def generate_room_height(self):
        self._height = weighted_random([(1, 0.5),
                                        (2, 0.4),
                                        (3, 0.3),
                                        (4, 0.2),
                                        (5, 0.1)])
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
        new_tiles = TektonTileGrid(self._width * 16, self._height * 16)

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
            if attached_doors[i].eject_direction == DoorEjectDirection.UP or attached_doors[
                i].eject_direction == DoorEjectDirection.DOWN:
                door_depth = 3
            new_door_grid = create_classic_door_tile_grid(attached_doors[i].eject_direction, door_depth, i)
            new_door_x_coord = attached_doors[i].h_screen * 16
            new_door_y_coord = attached_doors[i].v_screen * 16
            if attached_doors[i].eject_direction == DoorEjectDirection.RIGHT:
                new_door_x_coord += 14
                new_door_y_coord += 6
                for j in range(new_door_y_coord, new_door_y_coord + 4):
                    new_tiles[new_door_x_coord - 1][j].tileno = transparent_air_tileno
                    new_tiles[new_door_x_coord - 1][j].bts_type = 0x00
            if attached_doors[i].eject_direction == DoorEjectDirection.LEFT:
                new_door_y_coord += 6
                for j in range(new_door_y_coord, new_door_y_coord + 4):
                    new_tiles[new_door_x_coord + 2][j].tileno = transparent_air_tileno
                    new_tiles[new_door_x_coord + 2][j].bts_type = 0x00
            if attached_doors[i].eject_direction == DoorEjectDirection.DOWN:
                new_door_x_coord += 6
                new_door_y_coord += 13
                for j in range(new_door_x_coord, new_door_x_coord + 4):
                    new_tiles[j][new_door_y_coord - 1].tileno = transparent_air_tileno
                    new_tiles[j][new_door_y_coord - 1].bts_type = 0x00
            if attached_doors[i].eject_direction == DoorEjectDirection.UP:
                new_door_x_coord += 6
                for j in range(new_door_x_coord, new_door_x_coord + 4):
                    new_tiles[j][new_door_y_coord + 2].tileno = transparent_air_tileno
                    new_tiles[j][new_door_y_coord + 2].bts_type = 0x00
                for j in range(new_door_y_coord + 8, new_tiles.height, 7):
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


class TRBlueCanyonRoomGenerator(TRRoomGenerator):
    def __init__(self):
        super(TRBlueCanyonRoomGenerator, self).__init__()
        self._width = None
        self._height = None

    def generate_room_width(self):
        self._width = 1  # This room is always 1 wide.
        return self._width

    def generate_room_height(self):
        self._height = weighted_random([(3, 0.4),
                                        (4, 0.4),
                                        (5, 0.2)])
        return self._height

    def generate_room_tiles(self, attached_doors):
        if self._width is None:
            self.generate_room_width()
        if self._height is None:
            self.generate_room_height()
        new_tiles = TektonTileGrid(self._width * 16, self._height * 16)
        new_tiles.fill()

        outliner_start_x = random.randint(4, 11)
        outliner_start_y = random.randint(2, 5)

        # left_outliner = RockOutliner(outliner_start_x, outliner_start_y)
        # left_outliner.tile_grid = new_tiles
        # left_outliner.direction = DoorEjectDirection.LEFT
        # left_outliner.doors = attached_doors
        #
        # left_outliner.draw_outline()

        right_outliner = RockOutliner(outliner_start_x, outliner_start_y)
        right_outliner.tile_grid = new_tiles
        right_outliner.direction = DoorEjectDirection.RIGHT
        right_outliner.doors = attached_doors

        right_outliner.draw_outline()

        return new_tiles


class RockOutliner:
    rock_wall_vertical = 0x110
    rock_wall_slope = 0x10e
    rock_wall_slope_interior = 0x114
    rock_floor_ceiling = 0x10f
    rock_corner = 0x10d
    bts_slope_45 = 0x12

    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.doors = None
        self.direction = None
        self.tile_grid = None
        self._average_rock_widths = None

    @property
    def towards(self):
        if self.direction == DoorEjectDirection.LEFT:
            return -1
        else:
            return 1

    @property
    def away(self):
        return self.towards * -1

    def draw_outline(self):
        self._average_rock_widths = []
        for i in range(self.tile_grid.height // 16):
            self._average_rock_widths.append(max(0, random.randint(2, 5) - i))
        while self.y_coord < self.tile_grid.height - 1:
            self._draw_next()

    def _draw_next(self):
        target_coords = self._get_target_coords()

        y_movement = self._determine_y_movement(target_coords)
        x_movement = self._determine_x_movement(target_coords, y_movement)

        print("Coordinates are {},{} and I want to move {}, {}. Average rock width: {}".format(self.x_coord,
                                                                                               self.y_coord,
                                                                                               x_movement,
                                                                                               y_movement,
                                                                                               self._average_rock_widths[self.y_coord // 16]))

        self._move(x_movement, y_movement)
        self._set_tileno_at_coords(x_movement, y_movement)

    def _move(self, x_movement, y_movement):
        if x_movement == "towards":
            self.x_coord += self.towards
        elif x_movement == "away":
            self.x_coord += self.away
        self.y_coord += y_movement

    def _set_tileno_at_coords(self, x_movement, y_movement):
        if x_movement == "straight":
            self.tile_grid[self.x_coord][self.y_coord].tileno = self.rock_wall_vertical
            if self.direction == DoorEjectDirection.LEFT:
                self.tile_grid[self.x_coord][self.y_coord].h_mirror = True
        elif x_movement == "away":
            if y_movement == 0:
                self.tile_grid[self.x_coord][self.y_coord].tileno = self.rock_floor_ceiling
                self.tile_grid[self.x_coord][self.y_coord].v_mirror = self.tile_grid[self.x_coord + self.towards][
                    self.y_coord].v_mirror
            else:
                self.tile_grid[self.x_coord][self.y_coord].tileno = self.rock_wall_slope
                self.tile_grid[self.x_coord][self.y_coord].bts_type = 0x01
                self.tile_grid[self.x_coord][self.y_coord].bts_num = self.bts_slope_45
                if 0 <= (self.x_coord + self.towards) < 16:
                    self.tile_grid[self.x_coord + self.towards][self.y_coord].tileno = self.rock_wall_slope_interior
                if self.direction == DoorEjectDirection.LEFT:
                    self.tile_grid[self.x_coord][self.y_coord].h_mirror = True
                    if 0 <= (self.x_coord + self.towards) < 16:
                        self.tile_grid[self.x_coord + self.towards][self.y_coord].h_mirror = True
        elif x_movement == "towards":
            if y_movement == 0:
                self.tile_grid[self.x_coord][self.y_coord].tileno = self.rock_floor_ceiling
                self.tile_grid[self.x_coord][self.y_coord].v_mirror = self.tile_grid[self.x_coord + self.away][
                    self.y_coord].v_mirror
            else:
                self.tile_grid[self.x_coord][self.y_coord].tileno = self.rock_wall_slope
                self.tile_grid[self.x_coord][self.y_coord].bts_type = 0x01
                self.tile_grid[self.x_coord][self.y_coord].bts_num = self.bts_slope_45
                self.tile_grid[self.x_coord][self.y_coord].v_mirror = True
                if 0 <= (self.x_coord + self.away) < 16:
                    self.tile_grid[self.x_coord + self.away][self.y_coord].tileno = self.rock_wall_slope_interior
                    self.tile_grid[self.x_coord + self.away][self.y_coord].v_mirror = True
                if self.direction == DoorEjectDirection.LEFT:
                    self.tile_grid[self.x_coord][self.y_coord].h_mirror = True
                    if 0 <= (self.x_coord + self.away) < 16:
                        self.tile_grid[self.x_coord + self.away][self.y_coord].h_mirror = True

    def _get_target_coords(self):
        target_coords = None
        if self._door_on_this_screen():
            if (self.y_coord % 16) < 5:
                target_coords = (2 if self.direction == DoorEjectDirection.LEFT else 13,
                                 self.y_coord - (self.y_coord % 16) + 5)
        return target_coords

    def _determine_x_movement(self, target_coords, y_movement):
        x_movement = None
        if target_coords is not None:
            rows_left_to_target = target_coords[1] - self.y_coord
            if self.direction == DoorEjectDirection.LEFT:
                cols_left_to_target = self.x_coord - target_coords[0]
            if self.direction == DoorEjectDirection.RIGHT:
                cols_left_to_target = target_coords[0] - self.x_coord
            can_straight = rows_left_to_target > cols_left_to_target
            can_away = rows_left_to_target > (cols_left_to_target + 1)

            urgency_ratio = cols_left_to_target / rows_left_to_target

            movement_likelihoods = [("towards", urgency_ratio),
                                    ("straight", 1 / urgency_ratio if can_straight else 0),
                                    ("away", 1 / urgency_ratio if can_away else 0)]

            x_movement = weighted_random(movement_likelihoods)
        else:
            if y_movement == 0:
                if self.x_coord > 0 and self.tile_grid[self.x_coord + self.towards][self.y_coord].tileno == 0:
                    x_movement = "towards"
                else:
                    x_movement = "away"
            else:
                can_towards = 0 <= (self.x_coord + self.towards) < 16
                can_away = 0 <= (self.x_coord + self.away) < 16
                urgency_offset = (self._average_rock_widths[self.y_coord // 16] - self.x_coord) * self.towards
                movement_likelihoods = [("towards", 2 + urgency_offset if can_towards else 0),
                                        ("straight", 4),
                                        ("away", max(0, 2 - urgency_offset) if can_away else 0)]

                x_movement = weighted_random(movement_likelihoods)

        return x_movement

    def _determine_y_movement(self, target_coords):
        if target_coords is not None:
            return 1
        movement_likelihoods = [(0, 1 / self.y_coord),  # Y movement very unlikely near top of canyon
                                (1, 1)]
        return weighted_random(movement_likelihoods)

    def _door_on_this_screen(self):
        h_screen = self.y_coord // 16
        for door in self.doors:
            if door.h_screen == h_screen and door.eject_direction == self.direction:
                return True
        return False


def weighted_random(options):
    weight_sum = sum([weight for option, weight in options])
    choice = random.random() * weight_sum
    for option, weight in options:
        if choice <= weight:
            return option
        choice -= weight
    return options[-1][0]
