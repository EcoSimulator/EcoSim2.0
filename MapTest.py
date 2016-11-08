import pygame
import TiledMap


pygame.init()
screen = pygame.display.set_mode((800, 800))

world_map = TiledMap.WorldMap("Map2", screen)

world_map.render_entire_map()

# for x in world_map.tiles:
#     for y in x:
#         y.tile_print()

world_map.get_tile_at_pixel((30, 30)).tile_print()
print world_map.get_tile_at_pixel((30, 30))

while True:
    pass
