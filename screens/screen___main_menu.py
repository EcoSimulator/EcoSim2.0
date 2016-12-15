import pygame
from screens.screen___game import *
from widgets.widget___button import *
from widgets.widget___button_group import *
from properties import *


class MainMenuScreen:
    def __init__(self):
        self.button_group = ButtonGroup()
        self.map = "map1"
        self.game_screen = None

        # background image
        background_image = pygame.image.load(os.path.join(resources_dir, "eco_sim_cover" + png_ext))
        bg_rect = Rect((0, 0), (pygame.display.get_surface().get_size()))
        background_image = pygame.transform.scale(background_image, bg_rect.size)
        screen.blit(background_image, bg_rect)
        pygame.display.update()

        # start/quit buttons
        start_x = (pygame.display.get_surface().get_width() / 2) - 45   # 45 is half a standard button width
        start_y = 300
        start_button = Button((start_x, start_y), "startnormal", "startselected", self.start_game)
        start_button.draw()
        self.button_group.append(start_button)

        quit_button = Button((start_x, start_y + 36), "quitnormal", "quitselected", quit)
        quit_button.draw()
        self.button_group.append(quit_button)

        done = False
        while not done:
            self.button_group.monitor()
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    quit()

    def start_game(self):
        self.game_screen = GameScreen(self.map)
        self.game_screen.run_map()
