import pygame
from widgets.widget___button import *
from widgets.widget___info_display import *

class PopButton:
    # This is meant to be called in a loop.
    def __init__(self, itr, screen, start, species):
        self.itr = itr          # itr is the loop number, which handles the position of the PopButton.
        self.screen = screen
        self.start = start      # Right now, start should be the tuple (12, 14)
        self.species = species  # String containing the name of the species, for both the sprite and the info screen.


    def draw(self):
        monitor = []
        x = self.start[0]
        y = self.start[1] + (self.itr * 36) # Each PopButton will be 36 px below the last.

        # warning symbol
        warning = pygame.image.load(os.path.join(sidebar_dir, "warningoff" + png_ext))
        warning_rect = Rect((x + 0, y + 1), (27, 24))
        self.screen.blit(warning, warning_rect)

        # button
        self.button = Button(self.screen, x + 36, y, "popbutton", display_info, self.screen, self.species)
        self.button.draw()

        # sprite
        sprite = pygame.image.load((os.path.join(sprites_dir, self.species + png_ext)))
        sprite_rect = Rect((x + 97, y + 2), (24, 24))
        self.screen.blit(sprite, sprite_rect)
        pygame.display.update()

        self.update_population(6)   # random number because it needs an arg


    def monitor_button(self):
        if self.button.is_pressed():
            self.button.activate()


    def update_population(self, pop):
        font = pygame.font.SysFont("monospace", 22, True, False)
        population = str(pop)

        # generate coordinates and render text
        num_x = 80
        num_y = (self.itr * 36) + 15
        label = font.render(population, 1, (0, 0, 0))

        # draw a white rectangle
        white = pygame.image.load(os.path.join(sidebar_dir, "whiterect" + png_ext))
        white_rect = Rect((num_x - 30, num_y + 3), (60, 21))
        self.screen.blit(white, white_rect)
        # blit new text
        self.screen.blit(label, (num_x, num_y))
        pygame.display.update()
