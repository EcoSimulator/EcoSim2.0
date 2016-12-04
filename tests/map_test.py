from widgets import tiled_map
from properties import *

pygame.init()

world_map = tiled_map.WorldMap("Map2", screen)

world_map.render_entire_map()

# for x in world_map.tiles:
#     for y in x:
#         y.tile_print()

world_map.get_tile_at_pixel((30, 30)).tile_print()
print world_map.get_tile_at_pixel((30, 30))

while True:
    pass
