import pygame
from screens.screen___game import *
from widgets.widget___button import *
from widgets.widget___button_group import *
from widgets import widget___tiled_map as tiled_map
from properties import *


class MainMenuScreen:
    def __init__(self):
        self.button_group = ButtonGroup()
        self.map = "map2"
        self.game_screen = None

        # background image
        background_image = pygame.image.load(os.path.join(resources_dir, "eco_sim_cover" + png_ext))
        bg_rect = Rect((0, 0), (pygame.display.get_surface().get_size()))
        screen.blit(background_image, bg_rect)
        pygame.display.update()

        # start/quit buttons
        start_x = (pygame.display.get_surface().get_width() / 2) - 45 #45 is half a standard button width
        start_y = 300 #random for now
        start_button = Button((start_x, start_y), "startnormal", "startselected", self.test_start)
        start_button.draw()
        self.button_group.append(start_button)

        quit_button = Button((start_x, start_y + 36), "quitnormal", "quitselected", self.test_quit)
        quit_button.draw()
        self.button_group.append(quit_button)

        while True:
            self.button_group.monitor()
            pygame.event.get()

    def test_start(self):
        self.game_screen = GameScreen(self.map)

    def test_quit(self):
        quit()