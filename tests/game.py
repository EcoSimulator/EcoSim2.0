import pygame

from widgets import widget__sidebar
from widgets.SidebarWidget import pop

pygame.init()
screen = pygame.display.set_mode((954, 800))

sidebar.make_sidebar(screen)

# need to render map at (0, 154)

while True:
    PopMonitor.monitor_buttons(screen)
    pygame.event.get()