import pygame
import os
from widgets.widget___button import *
from widgets.widget___button_group import *
from properties import *


class PauseScreen:
    def __init__(self):
        self.button_group = ButtonGroup()
        # set up positions for visual elements
        x = ((pygame.display.get_surface().get_width() - 155) / 2) + 155
        y = (pygame.display.get_surface().get_height() / 2)
        half_text_width = 108
        pause_text_height = 36
        half_button_width = 65
        button_height = 39
        gap_height = 16
        # move y value up so that all elements can be centered
        y = y - (pause_text_height + button_height * 2 + gap_height * 2) / 2

        # create an overlay
        pane = pygame.Surface((pygame.display.get_surface().get_width() - 155, pygame.display.get_surface().get_height()))
        pane.set_alpha(40)
        pane.fill((55, 55, 55))
        screen.blit(pane, (155, 0))

        # make the word "PAUSED"
        pause_label = pygame.image.load(os.path.join(buttons_dir, "paused" + png_ext))
        pause_rect = Rect((x - half_text_width, y), (half_text_width * 2, pause_text_height))
        screen.blit(pause_label, pause_rect)
        y = y + pause_text_height + gap_height

        # make resume and quit buttons
        start_button = Button((x - half_button_width, y), "resumenormal", "resumeselected", self.unpause)
        start_button.draw()
        self.button_group.append(start_button)
        y = y + button_height + gap_height

        quit_button = Button((x - half_button_width, y), "quitnormal", "quitselected", self.quit)
        quit_button.draw()
        self.button_group.append(quit_button)

        pygame.display.update()

        while True:
            self.button_group.monitor()

    # I think we're going to need a universal pause/unpause function.
    def unpause(self):
        return 1

    def quit(self):
        quit()