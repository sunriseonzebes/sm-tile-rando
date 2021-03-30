from tekton.tekton_door import TektonDoor, DoorEjectDirection
from tekton.tekton_tile_grid import TektonTileGrid
from tekton.tekton_tile import TektonTile

base_tile = TektonTile()
horizontal_door_tube_outer_tileno = 0x041
horizontal_door_tube_inner_tileno = 0x061
horizontal_door_collar_outer_tileno = 0x040
horizontal_door_collar_inner_tileno = 0x060
horizontal_door_shield_outer_tileno = 0x00c
horizontal_door_shield_inner_tileno = 0x02c
vertical_door_tube_outer_tileno = 0x063
vertical_door_tube_inner_tileno = 0x062
vertical_door_collar_outer_tileno = 0x043
vertical_door_collar_inner_tileno = 0x042
vertical_door_shield_outer_tileno = 0x01d
vertical_door_shield_inner_tileno = 0x01c


def create_classic_door_tile_grid(new_door_eject_direction, door_depth, new_door_id, door_has_shield=True):
    new_door = None
    if new_door_eject_direction == DoorEjectDirection.LEFT or new_door_eject_direction == DoorEjectDirection.LEFT_NO_DOOR_CLOSE:
        new_door = TektonTileGrid(door_depth, 4)
        for i in range(door_depth):
            if i == door_depth - 1 and door_has_shield:
                new_door.overwrite_with(_create_door_shield(new_door_eject_direction), i, 0)
            elif i == door_depth - 2:
                new_door.overwrite_with(_create_door_collar(new_door_eject_direction, i == 0, new_door_id), i, 0)
            elif i < door_depth - 2:
                new_door.overwrite_with(_create_door_tube_segment(new_door_eject_direction, i == 0, new_door_id), i, 0)
    if new_door_eject_direction == DoorEjectDirection.RIGHT or new_door_eject_direction == DoorEjectDirection.RIGHT_NO_DOOR_CLOSE:
        new_door = TektonTileGrid(door_depth, 4)
        for i in range(door_depth):
            if i == 0 and door_has_shield:
                new_door.overwrite_with(_create_door_shield(new_door_eject_direction), i, 0)
            elif i == 1:
                new_door.overwrite_with(_create_door_collar(new_door_eject_direction, i == door_depth - 1, new_door_id), i, 0)
            elif i > 1:
                new_door.overwrite_with(_create_door_tube_segment(new_door_eject_direction, i == door_depth - 1, new_door_id), i, 0)
    if new_door_eject_direction == DoorEjectDirection.DOWN or new_door_eject_direction == DoorEjectDirection.DOWN_NO_DOOR_CLOSE:
        new_door = TektonTileGrid(4, door_depth)
        for i in range(door_depth):
            if i == 0 and door_has_shield:
                new_door.overwrite_with(_create_door_shield(new_door_eject_direction), 0, i)
            elif i == 1:
                new_door.overwrite_with(_create_door_collar(new_door_eject_direction, i == door_depth - 1, new_door_id),
                                        0, i)
            elif i > 1:
                new_door.overwrite_with(
                    _create_door_tube_segment(new_door_eject_direction, i == door_depth - 1, new_door_id), 0, i)
    if new_door_eject_direction == DoorEjectDirection.UP or new_door_eject_direction == DoorEjectDirection.UP_NO_DOOR_CLOSE:
        new_door = TektonTileGrid(4, door_depth)
        for i in range(door_depth):
            if i == door_depth - 1 and door_has_shield:
                new_door.overwrite_with(_create_door_shield(new_door_eject_direction), 0, i)
            elif i == door_depth - 2:
                new_door.overwrite_with(_create_door_collar(new_door_eject_direction, i == 0, new_door_id), 0, i)
            elif i < door_depth - 2:
                new_door.overwrite_with(_create_door_tube_segment(new_door_eject_direction, i == 0, new_door_id), 0, i)

    return new_door


def create_tekton_door(door_attach_point):
    new_door = TektonDoor()

    new_door.target_room_id = door_attach_point.farside_room.tekton_room.header
    new_door.target_door_cap_col = door_attach_point.farside_door.h_screen * 16
    if door_attach_point.eject_direction == DoorEjectDirection.LEFT or door_attach_point.eject_direction == DoorEjectDirection.LEFT_NO_DOOR_CLOSE:
        new_door.target_door_cap_col += 14
    elif door_attach_point.eject_direction == DoorEjectDirection.RIGHT or door_attach_point.eject_direction == DoorEjectDirection.RIGHT_NO_DOOR_CLOSE:
        new_door.target_door_cap_col += 1
    else:
        new_door.target_door_cap_col += 6
    new_door.target_door_cap_row = door_attach_point.farside_door.v_screen * 16
    if door_attach_point.eject_direction == DoorEjectDirection.UP or door_attach_point.eject_direction == DoorEjectDirection.UP_NO_DOOR_CLOSE:
        new_door.target_door_cap_row += 13
    elif door_attach_point.eject_direction == DoorEjectDirection.DOWN or door_attach_point.eject_direction == DoorEjectDirection.DOWN_NO_DOOR_CLOSE:
        new_door.target_door_cap_row += 2
    else:
        new_door.target_door_cap_row += 6
    new_door.target_room_screen_h = door_attach_point.farside_door.h_screen
    new_door.target_room_screen_v = door_attach_point.farside_door.v_screen
    new_door.distance_to_spawn = _standard_spawn_distance(door_attach_point.eject_direction)
    new_door.eject_direction = door_attach_point.eject_direction

    return new_door


def _create_door_tube_segment(new_door_eject_direction, has_door_bts=False, new_door_id=0):
    new_door_tube_segment = None

    if new_door_eject_direction == DoorEjectDirection.RIGHT or \
            new_door_eject_direction == DoorEjectDirection.RIGHT_NO_DOOR_CLOSE or \
            new_door_eject_direction == DoorEjectDirection.LEFT or \
            new_door_eject_direction == DoorEjectDirection.LEFT_NO_DOOR_CLOSE:
        new_door_tube_segment = TektonTileGrid(1, 4)
        new_door_tube_segment.fill(base_tile)

        for i in [0, 3]:
            new_door_tube_segment[0][i].tileno = horizontal_door_tube_outer_tileno

        for i in range(1, 3):
            new_door_tube_segment[0][i].tileno = horizontal_door_tube_inner_tileno

        for i in range(2, 4):
            new_door_tube_segment[0][i].v_mirror = True

        if has_door_bts:
            for i in range(4):
                new_door_tube_segment[0][i].bts_type = 0x09
                new_door_tube_segment[0][i].bts_num = new_door_id

        if new_door_eject_direction == DoorEjectDirection.LEFT or new_door_eject_direction == DoorEjectDirection.LEFT_NO_DOOR_CLOSE:
            for i in range(4):
                new_door_tube_segment[0][i].h_mirror = True

    if new_door_eject_direction == DoorEjectDirection.UP or \
            new_door_eject_direction == DoorEjectDirection.UP_NO_DOOR_CLOSE or \
            new_door_eject_direction == DoorEjectDirection.DOWN or \
            new_door_eject_direction == DoorEjectDirection.DOWN_NO_DOOR_CLOSE:
        new_door_tube_segment = TektonTileGrid(4, 1)
        new_door_tube_segment.fill(base_tile)

        for i in [0, 3]:
            new_door_tube_segment[i][0].tileno = vertical_door_tube_outer_tileno

        for i in range(1, 3):
            new_door_tube_segment[i][0].tileno = vertical_door_tube_inner_tileno

        for i in range(2):
            new_door_tube_segment[i][0].h_mirror = True

        if has_door_bts:
            for i in range(4):
                new_door_tube_segment[i][0].bts_type = 0x09
                new_door_tube_segment[i][0].bts_num = new_door_id

        if new_door_eject_direction == DoorEjectDirection.UP or new_door_eject_direction == DoorEjectDirection.UP_NO_DOOR_CLOSE:
            for i in range(4):
                new_door_tube_segment[i][0].v_mirror = True

    return new_door_tube_segment


def _create_door_collar(new_door_eject_direction, has_door_bts=False, new_door_id=0):
    new_door_collar = None

    if new_door_eject_direction == DoorEjectDirection.RIGHT or \
            new_door_eject_direction == DoorEjectDirection.RIGHT_NO_DOOR_CLOSE or \
            new_door_eject_direction == DoorEjectDirection.LEFT or \
            new_door_eject_direction == DoorEjectDirection.LEFT_NO_DOOR_CLOSE:
        new_door_collar = TektonTileGrid(1, 4)
        new_door_collar.fill(base_tile)

        for i in [0, 3]:
            new_door_collar[0][i].tileno = horizontal_door_collar_outer_tileno

        for i in range(1, 3):
            new_door_collar[0][i].tileno = horizontal_door_collar_inner_tileno

        for i in range(2, 4):
            new_door_collar[0][i].v_mirror = True

        if has_door_bts:
            for i in range(4):
                new_door_collar[0][i].bts_type = 0x09
                new_door_collar[0][i].bts_num = new_door_id

        if new_door_eject_direction == DoorEjectDirection.LEFT or new_door_eject_direction == DoorEjectDirection.LEFT_NO_DOOR_CLOSE:
            for i in range(4):
                new_door_collar[0][i].h_mirror = True

    if new_door_eject_direction == DoorEjectDirection.UP or \
            new_door_eject_direction == DoorEjectDirection.UP_NO_DOOR_CLOSE or \
            new_door_eject_direction == DoorEjectDirection.DOWN or \
            new_door_eject_direction == DoorEjectDirection.DOWN_NO_DOOR_CLOSE:
        new_door_collar = TektonTileGrid(4, 1)
        new_door_collar.fill(base_tile)

        for i in [0, 3]:
            new_door_collar[i][0].tileno = vertical_door_collar_outer_tileno

        for i in range(1, 3):
            new_door_collar[i][0].tileno = vertical_door_collar_inner_tileno

        for i in range(2):
            new_door_collar[i][0].h_mirror = True

        if has_door_bts:
            for i in range(4):
                new_door_collar[i][0].bts_type = 0x09
                new_door_collar[i][0].bts_num = new_door_id

        if new_door_eject_direction == DoorEjectDirection.UP or new_door_eject_direction == DoorEjectDirection.UP_NO_DOOR_CLOSE:
            for i in range(4):
                new_door_collar[i][0].v_mirror = True

    return new_door_collar


def _create_door_shield(new_door_eject_direction):
    if new_door_eject_direction == DoorEjectDirection.RIGHT or \
            new_door_eject_direction == DoorEjectDirection.LEFT:
        new_door_shield = TektonTileGrid(1, 4)
        new_door_shield.fill(base_tile)

        for i in [0, 3]:
            new_door_shield[0][i].tileno = horizontal_door_shield_outer_tileno

        for i in range(1, 3):
            new_door_shield[0][i].tileno = horizontal_door_shield_inner_tileno

        for i in range(2, 4):
            new_door_shield[0][i].v_mirror = True

        new_door_shield[0][0].bts_type = 0x0c
        for i in range(1, 4):
            new_door_shield[0][i].bts_type = 0x0d

        if new_door_eject_direction == DoorEjectDirection.LEFT:
            for i in range(4):
                new_door_shield[0][i].h_mirror = True

        if new_door_eject_direction == DoorEjectDirection.RIGHT:
            new_door_shield[0][0].bts_num = 0x40
        else:
            new_door_shield[0][0].bts_num = 0x41
        new_door_shield[0][1].bts_num = 0xff
        new_door_shield[0][2].bts_num = 0xfe
        new_door_shield[0][3].bts_num = 0xfd

    if new_door_eject_direction == DoorEjectDirection.UP or new_door_eject_direction == DoorEjectDirection.DOWN:
        new_door_shield = TektonTileGrid(4, 1)
        new_door_shield.fill(base_tile)

        for i in [0, 3]:
            new_door_shield[i][0].tileno = vertical_door_shield_outer_tileno

        for i in range(1, 3):
            new_door_shield[i][0].tileno = vertical_door_shield_inner_tileno

        for i in range(2):
            new_door_shield[i][0].h_mirror = True

        new_door_shield[0][0].bts_type = 0x0c
        for i in range(1, 4):
            new_door_shield[i][0].bts_type = 0x05

        if new_door_eject_direction == DoorEjectDirection.UP:
            for i in range(4):
                new_door_shield[i][0].v_mirror = True

        if new_door_eject_direction == DoorEjectDirection.UP:
            new_door_shield[0][0].bts_num = 0x43
        else:
            new_door_shield[0][0].bts_num = 0x42
        new_door_shield[1][0].bts_num = 0xff
        new_door_shield[2][0].bts_num = 0xfe
        new_door_shield[3][0].bts_num = 0xfd

    return new_door_shield


def _standard_spawn_distance(door_eject_direction):
    if door_eject_direction == DoorEjectDirection.LEFT or \
            door_eject_direction == DoorEjectDirection.LEFT_NO_DOOR_CLOSE or \
            door_eject_direction == DoorEjectDirection.RIGHT or \
            door_eject_direction == DoorEjectDirection.RIGHT_NO_DOOR_CLOSE:
        return 0x8000
    elif door_eject_direction == DoorEjectDirection.DOWN or \
            door_eject_direction == DoorEjectDirection.DOWN_NO_DOOR_CLOSE:
        return 0x0140
    else:
        return 0x01c0
