from widgets import widget___tiled_map as tiled_map
from properties import *

pygame.init()

world_map = tiled_map.WorldMap("map2.tmx", screen)

world_map.render_entire_map()

# for x in world_map.tiles:
#     for y in x:
#         y.tile_print()

world_map.get_tile_at_pixel((30, 30)).tile_print()
print world_map.get_tile_at_pixel((30, 30))
world_map.get_tile_at_pixel((0, 0)).fill((255, 0, 0))
world_map.get_tile_at_pixel((0, 0)).blit()
pygame.display.update()

while True:
    pass
