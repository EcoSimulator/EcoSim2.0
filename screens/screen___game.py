import pygame

from widgets import widget___tiled_map
from widgets.widget___sidebar import SideBar as s
from widgets.widget___button import *


# We'll need to pass a map param.
class GameScreen:
    def __init__(self, map_name):
        world_map = widget___tiled_map.WorldMap(map_name + tmx_ext, (155, 0))
        screen = pygame.display.set_mode((world_map.widthPX + 154, world_map.heightPX))

        sb = s(world_map.heightPX)
        sb.draw()

        world_map.render_entire_map()
        pygame.display.update()

        while True:
            sb.monitor_buttons()
            pygame.event.get()
