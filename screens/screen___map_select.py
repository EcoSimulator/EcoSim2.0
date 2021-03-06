import pygame
from screens.screen___setup import *
from widgets.widget___button import *
from widgets.widget___map_button import *
from widgets.widget___button_group import *
from properties import *


class MapSelectScreen:
    def __init__(self):
        self.button_group = ButtonGroup()
        self.map = ""

        # background image
        background_image = pygame.image.load(os.path.join(resources_dir, "soilmap" + png_ext))
        bg_rect = Rect((0, 0), (pygame.display.get_surface().get_size()))
        screen.blit(background_image, bg_rect)
        # create an overlay
        pane = pygame.Surface(
            (pygame.display.get_surface().get_width(), pygame.display.get_surface().get_height()))
        pane.set_alpha(80)
        pane.fill((55, 55, 55))
        screen.blit(pane, (0, 0))
        pygame.display.update()

        self.draw_setup_text()

        # map buttons
        self.start_x = 100
        self.start_y = 200
        self.inc_x = 180
        self.inc_y = 180

        for file in os.listdir(map_dir):
            if file.endswith(tmx_ext):
                (map, ext) = os.path.splitext(file)
                self.make_map_button((self.start_x, self.start_y), map)

        self.done = False
        while not self.done:
            self.button_group.monitor()
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    quit()

    def draw_setup_text(self):
        text_image = pygame.image.load(os.path.join(resources_dir, "select_a_map" + png_ext))
        text_rect = Rect((pygame.display.get_surface().get_width()/2 - 305, 80), (609, 51))
        screen.blit(text_image, text_rect)

    def make_map_button(self, location, map):
        map_button = MapButton(location, map, self.begin_setup)
        map_button.draw()
        self.button_group.append(map_button)
        self.start_x += self.inc_x # This part kinda sucks. If we have more maps, we'll need to make use of inc_y, too.

    def begin_setup(self, map):
        self.done = True
        self.setup_screen = SetupScreen(map)
        self.setup_screen.run()
