import pygame
import os
from widgets.widget___button import *
from widgets.widget___button_group import *
from properties import *


class MainMenuScreen:
    def __init__(self):
        self.button_group = ButtonGroup()

        # background image
        background_image = pygame.image.load(os.path.join(resources_dir, "eco_sim_cover" + png_ext))
        bg_rect = Rect((0, 0), (pygame.display.get_surface().get_size()))
        screen.blit(background_image, bg_rect)
        pygame.display.update()

        # start/quit buttons
        start_x = (pygame.display.get_surface().get_width() / 2) - 45 #45 is half a standard button width
        start_y = 300 #random for now
        start_button = Button((start_x, start_y), "startnormal", test_start)
        start_button.draw()

        quit_button = Button((start_x, start_y + 36), "quitnormal", test_quit)
        quit_button.draw()

        return 1

    def test_start(self):
        return 1

    def test_quit(self):
        return 0