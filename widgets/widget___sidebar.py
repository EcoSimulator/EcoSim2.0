import pygame
import os
from properties import *
from pygame.locals import *
from threading import Thread
from screens.screen___pause import *
from widgets.widget___button import *
from widgets.widget___button_group import *
from widgets.widget___pop_button import *


class SideBar:
    def __init__(self, height, sprite_group, GRID_LOCK):
        self.width = 154
        self.height = height
        self.sidebar_rect = Rect((0, 0), (154, height))
        self.screen = screen
        self.pop_buttons = list()
        self.buttons = ButtonGroup()
        self.sprite_group = sprite_group
        self.GRID_LOCK = GRID_LOCK
        self.thread = Thread(target=self.run)
        self.thread.daemon = True
        self.is_alive = True

    def run(self):
        while True:
            self.monitor_buttons()

    def draw(self):
        # draw a rectangle for the background
        pygame.draw.rect(self.screen, (55, 55, 55, 100), self.sidebar_rect)

        # We'll need to pass in a universal list of available species instead of just writing it here.
        species = ["wolf", "deer", "bees", "plant", "bear"]
        self.make_pop_buttons()

        # Replace this with a real button
        pause_y = self.height - 52
        pause = Button((13, pause_y), "pausenormal", "pauseselected", self.pause)
        self.buttons.append(pause)

        pause.draw()

        pygame.display.update()

    def make_pop_buttons(self):
        iterator = 0
        start = (12, 14)
        for species in self.sprite_group.get_subgroups():
            pop_btn = PopButton(iterator, start, species.type, species)
            pop_btn.draw()
            pop_btn.update_population()
            self.pop_buttons.append(pop_btn)
            self.buttons.append(pop_btn)
            iterator += 1

    def monitor_buttons(self):
        # for pop_btn in self.pop_buttons:
        #     info_display = pop_btn.monitor()
        self.buttons.monitor()

    # Placeholder until we have a real way of pausing the game.
    def pause(self):
        # self.sprite_group.pause()
        # pause = PauseScreen()
        return False
