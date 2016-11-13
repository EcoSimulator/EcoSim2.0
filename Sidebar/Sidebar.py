import pygame
from pygame.locals import *
#import Utils

def make_sidebar(screen):
    # maybe instead i should draw a rectangle of the screen's height
    sidebar_rect = Rect((0, 0), (154, screen.get_size()[1]))
    pygame.draw.rect(screen, (55, 55, 55, 100), sidebar_rect, width=0)

    #sidebar = []
    #sidebar_img = pygame.image.load("Resources/sidebar/sidebar.png")
    #sidebar_rect = Rect((0, 0), (154, 719))

    #sidebar.append((sidebar_img, sidebar_rect))

    #for tuple in sidebar:
    #    screen.blit(tuple[0], tuple[1])

    # now add a pause button
    # might want to do this on a more global level
    pause = pygame.image.load("Resources/sidebar/pausenormal.png")
    pause_rect = Rect((13, 667), (129, 39))

    screen.blit(pause, pause_rect)
    pygame.display.flip()
