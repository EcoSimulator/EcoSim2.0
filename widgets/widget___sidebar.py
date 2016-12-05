import pygame
from pygame.locals import *

import widgets.pop_monitor


class SideBar:
    def __init__(self, screen, height):
        self.width = 154
        self.height = height
        self.sidebar_rect = Rect((0, 0), (154, height))
        self.screen = screen

    def draw(self):
        # draw a rectangle for the background
        pygame.draw.rect(self.screen, (55, 55, 55, 100), self.sidebar_rect)

        # iterate through available species and make monitors for them
        species = ["wolf", "deer", "bees", "plant"]
        itr = 0
        for item in species:
            widgets.pop_monitor.make_monitor(self.screen, itr, item)
            itr += 1

        # now add a pause button
        # might want to do this on a more global level
        pause = pygame.image.load("resources/sidebar/pausenormal.png")
        pause_y = self.height - 52
        pause_rect = Rect((13, pause_y), (129, 39))

        self.screen.blit(pause, pause_rect)
        pygame.display.update()
