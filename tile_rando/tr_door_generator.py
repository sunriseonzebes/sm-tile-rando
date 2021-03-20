from tekton.tekton_door import DoorEjectDirection
from tekton.tekton_tile_grid import TektonTileGrid
from tekton.tekton_tile import TektonTile

base_tile = TektonTile()
horizontal_door_collar_outer_tileno = 0x040
horizontal_door_collar_inner_tileno = 0x060
horizontal_door_shield_outer_tileno = 0x00c
horizontal_door_shield_inner_tileno = 0x02c
vertical_door_collar_outer_tileno = 0x042
vertical_door_collar_inner_tileno = 0x062
vertical_door_shield_outer_tileno = 0x01d
vertical_door_shield_inner_tileno = 0x01c


def create_classic_door_tile_grid(new_door_eject_direction, new_door_id, door_has_shield=True):
    new_door = None
    if new_door_eject_direction == DoorEjectDirection.RIGHT or new_door_eject_direction == DoorEjectDirection.RIGHT_NO_DOOR_CLOSE:
        new_door = TektonTileGrid(2, 4)
        new_door.overwrite_with(_create_door_collar(new_door_eject_direction, new_door_id), 0, 0)
        if door_has_shield:
            new_door.overwrite_with(_create_door_shield(new_door_eject_direction), 1, 0)
    if new_door_eject_direction == DoorEjectDirection.LEFT or new_door_eject_direction == DoorEjectDirection.LEFT_NO_DOOR_CLOSE:
        new_door = TektonTileGrid(2, 4)
        new_door.overwrite_with(_create_door_collar(new_door_eject_direction, new_door_id), 1, 0)
        if door_has_shield:
            new_door.overwrite_with(_create_door_shield(new_door_eject_direction), 0, 0)
    if new_door_eject_direction == DoorEjectDirection.UP or new_door_eject_direction == DoorEjectDirection.UP_NO_DOOR_CLOSE:
        new_door = TektonTileGrid(4, 2)
        new_door.overwrite_with(_create_door_collar(new_door_eject_direction, new_door_id), 0, 1)
        if door_has_shield:
            new_door.overwrite_with(_create_door_shield(new_door_eject_direction), 0, 0)
    if new_door_eject_direction == DoorEjectDirection.DOWN or new_door_eject_direction == DoorEjectDirection.DOWN_NO_DOOR_CLOSE:
        new_door = TektonTileGrid(4, 2)
        new_door.overwrite_with(_create_door_collar(new_door_eject_direction, new_door_id), 0, 0)
        if door_has_shield:
            new_door.overwrite_with(_create_door_shield(new_door_eject_direction), 0, 1)

    return new_door



def _create_door_collar(new_door_eject_direction, new_door_id):
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

        for i in range(4):
            new_door_collar[0][i].bts_type = 0x09
            new_door_collar[0][i].bts_num = new_door_id

        if new_door_eject_direction == DoorEjectDirection.RIGHT or new_door_eject_direction == DoorEjectDirection.RIGHT_NO_DOOR_CLOSE:
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

        for i in range(4):
            new_door_collar[i][0].bts_type = 0x09
            new_door_collar[i][0].bts_num = new_door_id

        if new_door_eject_direction == DoorEjectDirection.DOWN or new_door_eject_direction == DoorEjectDirection.DOWN_NO_DOOR_CLOSE:
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

        if new_door_eject_direction == DoorEjectDirection.RIGHT:
            for i in range(4):
                new_door_shield[0][i].h_mirror = True

        if new_door_eject_direction == DoorEjectDirection.LEFT:
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
            new_door_shield[i][0].bts_type = 0x0d

        if new_door_eject_direction == DoorEjectDirection.DOWN:
            for i in range(4):
                new_door_shield[i][0].V_mirror = True

        if new_door_eject_direction == DoorEjectDirection.DOWN:
            new_door_shield[0][0].bts_num = 0x43
        else:
            new_door_shield[0][0].bts_num = 0x42
        new_door_shield[1][0].bts_num = 0xff
        new_door_shield[2][0].bts_num = 0xfe
        new_door_shield[3][0].bts_num = 0xfd

    return new_door_shield