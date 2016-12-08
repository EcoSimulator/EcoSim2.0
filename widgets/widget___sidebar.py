import pygame
import os
from properties import *
from pygame.locals import *
from widgets.widget___button import *
from widgets.widget___button_group import *
from widgets.widget___pop_button import *


class SideBar:
    def __init__(self, height):
        self.width = 154
        self.height = height
        self.sidebar_rect = Rect((0, 0), (154, height))
        self.screen = screen
        self.pop_buttons = list()
        self.buttons = ButtonGroup()


    def draw(self):
        # draw a rectangle for the background
        pygame.draw.rect(self.screen, (55, 55, 55, 100), self.sidebar_rect)

        # We'll need to pass in a universal list of available species instead of just writing it here.
        species = ["wolf", "deer", "bees", "plant"]
        self.make_pop_buttons(species)

        # Replace this with a real button
        pause_y = self.height - 52
        pause = Button((13, pause_y), "pausenormal", self.pause)
        self.buttons.append(pause)
        pause.draw()

        pygame.display.update()


    def make_pop_buttons(self, list):
        iterator = 0
        start = (12, 14)
        for species in list:
            pop_btn = PopButton(iterator, start, species)
            pop_btn.draw()
            self.pop_buttons.append(pop_btn)
            iterator += 1


    def monitor_buttons(self):
        for pop_btn in self.pop_buttons:
            pop_btn.monitor_button()
        self.buttons.monitor()


    # Placeholder until we have a real way of pausing the game.
    def pause(self):
        font = pygame.font.SysFont("monospace", 60, True, False)
        text = "PAUSED"
        label = font.render(text, 1, (255, 255, 255))
        self.screen.blit(label, (300, 300))
        pygame.display.update()
