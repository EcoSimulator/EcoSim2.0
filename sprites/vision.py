"""Vision Module"""


def vision(distance, world_map, tile):
    """
    :param distance: the distance to look in tiles
    :param world_map: the map to look on
    :param tile: the starting tile, should be a sprite current tile
    :return: the set of tiles visible within distance
    """
    distance -= 1
    vision_set = set(world_map.get_surrounding_movable_tiles(tile))
    for index in range(0, distance):
        temp = set()
        for next_tile in vision_set:
            for new_tile in world_map.get_surrounding_movable_tiles(next_tile):
                temp.add(new_tile)
        vision_set = vision_set.union(temp)
        vision_set.remove(tile)
    return vision_set
