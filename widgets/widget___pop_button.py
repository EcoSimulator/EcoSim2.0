import pygame
from properties import *
from widgets.widget___button import *
from widgets.widget___info_display import *

class PopButton(Button):
    # This is meant to be called in a loop.
    def __init__(self, position, location, species):
        self.position = position    # The button's position in the list of PopButtons.
        self.screen = screen
        self.location = location    # Where the first PopButton in the list appears. Should be (12, 14).
        self.species = species      # String containing the name of the species, for both the sprite and the info screen.
        self.method = display_info
        self.args = species
        self.least_concern = 0
        self.endangered = 1
        self.extinct = 2


    def draw(self):
        self.x = self.location[0]
        self.y = self.location[1] + (self.position * 36) # Each PopButton will be 36 px below the last.

        # warning symbol
        self.update_warning(self.least_concern)

        # button
        self.rect = Rect((self.x + 36, self.y), (90, 27))
        button = pygame.image.load(os.path.join(buttons_dir, "popbutton" + png_ext))
        self.screen.blit(button, self.rect)

        # sprite
        sprite = pygame.image.load((os.path.join(sprites_dir, self.species + png_ext)))
        sprite_rect = Rect((self.x + 97, self.y + 2), (24, 24))
        self.screen.blit(sprite, sprite_rect)
        pygame.display.update()

        self.update_population(0)   # random number because it needs an arg


    def activate(self):
        return self.method(self.species)


    def update_warning(self, level):
        # Determine conservation status of the species
        if level == self.extinct:
            img = "warning_extinct"
        elif level == self.endangered:
            img = "warning_on"
        else:
            img = "warning_off"

        warning = pygame.image.load(os.path.join(sidebar_dir, img + png_ext))
        warning_rect = Rect((self.x, self.y + 1), (27, 24))
        self.screen.blit(warning, warning_rect)
        pygame.display.update()


    def update_population(self, pop):
        font = pygame.font.SysFont("monospace", 22, True, False)
        population = str(pop)

        # generate coordinates and render text
        num_x = 80
        num_y = (self.position * 36) + 15
        label = font.render(population, 1, (0, 0, 0))

        # draw a white rectangle
        white = pygame.image.load(os.path.join(sidebar_dir, "whiterect" + png_ext))
        white_rect = Rect((num_x - 30, num_y + 3), (60, 21))
        self.screen.blit(white, white_rect)
        # blit new text
        self.screen.blit(label, (num_x, num_y))
        pygame.display.update()
