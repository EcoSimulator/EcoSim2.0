from widgets import widget___tiled_map as tiled_map
from properties import *

# deprecated. Doesn't matter though

pygame.init()
screen = pygame.display.set_mode((800, 800))

world_map = tiled_map.WorldMap("map2.tmx", (0, 0))

world_map.render_entire_map()

# for x in world_map.tiles:
#     for y in x:
#         y.tile_print()

world_map.get_tile_at_pixel((30, 30)).tile_print()
print world_map.get_tile_at_pixel((30, 30))

world_map.get_tile_at_pixel((0, 0)).image.fill((255, 0, 0))
world_map.get_tile_at_pixel((0, 0)).image.blit(screen)
pygame.display.update()

while True:
    pass
