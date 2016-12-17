import pygame
from screens.screen___game import *
from widgets.widget___button import *
from widgets.widget___map_button import *
from widgets.widget___button_group import *
from properties import *


class MapSelectScreen:
    def __init__(self):
        self.button_group = ButtonGroup()
        self.map = ""
        self.game_screen = None

        # background image
        background_image = pygame.image.load(os.path.join(resources_dir, "eco_sim_cover" + png_ext))
        bg_rect = Rect((0, 0), (pygame.display.get_surface().get_size()))
        background_image = pygame.transform.scale(background_image, bg_rect.size)
        screen.blit(background_image, bg_rect)
        # create an overlay
        pane = pygame.Surface(
            (pygame.display.get_surface().get_width(), pygame.display.get_surface().get_height()))
        pane.set_alpha(80)
        pane.fill((55, 55, 55))
        screen.blit(pane, (0, 0))
        pygame.display.update()

        # start/quit buttons
        self.start_x = 100
        self.start_y = 100
        self.inc_x = 180
        self.inc_y = 180

        for file in os.listdir(map_dir):
            if file.endswith(tmx_ext):
                (map, ext) = os.path.splitext(file)
                self.make_map_button((self.start_x, self.start_y), map)

        done = False
        while not done:
            self.button_group.monitor()
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    quit()

    def make_map_button(self, location, map):
        map_button = MapButton(location, map, self.start_game)
        map_button.draw()
        self.button_group.append(map_button)
        self.start_x += self.inc_x

    def start_game(self, map):
        self.game_screen = GameScreen(map)
        self.game_screen.run_map()
