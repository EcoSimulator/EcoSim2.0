import pygame

from widgets import widget___tiled_map
from widgets.widget___sidebar import SideBar as s
from widgets.widget___button import *

pygame.init()

world_map = widget___tiled_map.WorldMap("map2.tmx", (155, 0))

screen = pygame.display.set_mode((world_map.widthPX + 154, world_map.heightPX))


sb = s(world_map.heightPX)
sb.draw()

world_map.render_entire_map()
pygame.display.update()

while True:
    sb.monitor_buttons()
    pygame.event.get()
