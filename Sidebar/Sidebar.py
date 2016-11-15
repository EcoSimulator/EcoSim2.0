import pygame
from pygame.locals import *
import PopMonitor
#import Utils

def make_sidebar(screen):
    # maybe instead i should draw a rectangle of the screen's height
    sidebar_rect = Rect((0, 0), (154, screen.get_size()[1]))
    pygame.draw.rect(screen, (55, 55, 55, 100), sidebar_rect)

    species = ["wolf", "deer", "bees", "plant"]
    itr = 0
    for item in species:
        PopMonitor.make_monitor(screen, itr, item)
        itr += 1

    # now add a pause button
    # might want to do this on a more global level
    pause = pygame.image.load("Resources/sidebar/pausenormal.png")
    pause_y = screen.get_size()[1] - 52
    pause_rect = Rect((13, pause_y), (129, 39))

    screen.blit(pause, pause_rect)
    pygame.display.flip()
