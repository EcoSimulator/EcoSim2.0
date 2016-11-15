import pygame
from Sidebar import Sidebar, PopMonitor

pygame.init()
screen = pygame.display.set_mode((954, 800))

Sidebar.make_sidebar(screen)

# need to render map at (0, 154)

while True:
    PopMonitor.monitor_buttons(screen)
    pygame.event.get()