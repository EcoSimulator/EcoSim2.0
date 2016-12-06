"""Vision Module"""

import random


def vision(distance, world_map, tile):
    """
    :param distance: the distance to look in tiles
    :param world_map: the map to look on
    :param tile: the starting tile, should be a sprite current tile
    :return: the set of tiles visible within distance
    """
    vision_set = set(world_map.get_surrounding_movable_tiles(tile))
    for index in range(0, distance - 1):
        temp = set()
        for next_tile in vision_set:
            for new_tile in world_map.get_surrounding_movable_tiles(next_tile):
                temp.add(new_tile)
        vision_set = vision_set.union(temp)
        vision_set.remove(tile)
    return vision_set


def find_target(visible_tiles, targets):
    for tile in visible_tiles:
        if tile.contains_sprite is not None:
            for sprite_type in targets:
                if tile.contains_sprite.type == sprite_type:
                    return tile
    return False


def approach(current_tile, target_tile, world_map):
    """
    :param current_tile: the tile the approaching sprite occupies
    :param target_tile: the tile to approach
    :param world_map:
    :return: a tile along a path to the target tile
    """
    relative_x = target_tile.location_t[0] - current_tile.location_t[0]
    relative_y = target_tile.location_t[1] - current_tile.location_t[1]
    step_x = 0
    step_y = 0
    if random.randint(0, 1) == 0:
        if relative_x < 0:
            step_x = -1
        elif relative_x > 0:
            step_x = 1
        elif relative_y < 0:
            step_y = -1
        elif relative_y > 0:
            step_y = 1
    else:
        if relative_y < 0:
            step_y = -1
        elif relative_y > 0:
            step_y = 1
        elif relative_x < 0:
            step_x = -1
        elif relative_x > 0:
            step_x = 1
    go_to_tile = world_map.get_tile_by_index((current_tile.location_t[1] + step_y, current_tile.location_t[0] + step_x))
    return go_to_tile


def flee(current_tile, repelling_tile, world_map):
    relative_x = repelling_tile.location_t[0] - current_tile.location_t[0]
    relative_y = repelling_tile.location_t[1] - current_tile.location_t[1]
    step_x = 0
    step_y = 0
    lateral_probability = random.randint(0, 3) == 0
    if relative_x == 0 and lateral_probability:
        step_x = random.choice((-1, 1))
    elif relative_y == 0 and lateral_probability:
        step_y = random.choice((-1, 1))
    else:
        if random.randint(0, 1) == 0:
            if relative_x < 0:
                step_x = -1
            elif relative_x > 0:
                step_x = 1
            elif relative_y < 0:
                step_y = -1
            elif relative_y > 0:
                step_y = 1
        else:
            if relative_y < 0:
                step_y = -1
            elif relative_y > 0:
                step_y = 1
            elif relative_x < 0:
                step_x = -1
            elif relative_x > 0:
                step_x = 1
    go_to_tile = world_map.get_tile_by_index((current_tile.location_t[1] - step_y, current_tile.location_t[0] - step_x))
    # if go_to_tile is None:
    #     flee(current_tile, repelling_tile, world_map)
    return go_to_tile
