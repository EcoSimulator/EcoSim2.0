import pygame

from widgets import widget___tiled_map
from widgets.widget___sidebar import SideBar as s

pygame.init()

world_map = widget___tiled_map.WorldMap("map2", (155, 0))

screen = pygame.display.set_mode((world_map.widthPX + 154, world_map.heightPX))


sb = s(screen, world_map.heightPX)
sb.draw()

world_map.render_entire_map()
pygame.display.update()

while True:
    pass
