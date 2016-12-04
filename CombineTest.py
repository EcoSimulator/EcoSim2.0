from Widgets.SidebarWidget.Sidebar import SideBar as s
import TiledMap
import pygame

pygame.init()

world_map = TiledMap.WorldMap("Map2", (155, 0))

screen = pygame.display.set_mode((world_map.widthPX + 154, world_map.heightPX))


sb = s(screen, world_map.heightPX)
sb.draw()

world_map.render_entire_map()
pygame.display.update()

while True:
    pass
