import pygame
from properties import *
from widgets.widget___button import *
from widgets.widget___info_display import *

class SetupButton(Button):
    # This is meant to be called in a loop.
    def __init__(self, position, location, species, group, method):
        self.position = position    # The button's position in the list of PopButtons.
        self.location = location    # Where the first PopButton in the list appears. Should be (12, 14).
        self.species = species      # String containing the name of the species, for both the sprite and the info screen.
        self.group = group
        self.method = method
        self.args = species
        self.least_concern = 0
        self.endangered = 1
        self.extinct = 2
        self.image = "popbutton"
        self.highlight_image = "popbuttonselected"
        self.is_highlighted = False
        self.is_activated = False

    def draw(self):
        self.x = self.location[0]
        self.y = self.location[1] + (self.position * 36) # Each PopButton will be 36 px below the last.
        self.rect = Rect((self.x + 36, self.y), (90, 27))

        self.draw_button_normal()
        self.draw_sprite()
        self.update_population()

    def monitor(self):
        self.update_population()
        mouse = pygame.mouse.get_pos()
        if not self.is_activated:
            # highlight button if it's hovered and not currently highlighted
            if self.rect.collidepoint(mouse):
                if not self.is_highlighted:
                    self.highlight_on()
            # de-highlight button if it's highlighted and not currently hovered
            if not self.rect.collidepoint(mouse):
                if self.is_highlighted:
                    self.highlight_off()
            # activate button if it's clicked on
            if self.is_pressed():
                if not self.is_activated:
                    return self.activate()
            else:
                return None

    def is_pressed(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.rect.collidepoint(mouse):
            if click[0] == 1:
                return True

    def activate(self):
        self.select_on()
        return self.method(self, self.species)

    # activation is a little convoluted at the moment. can fix when we pick this up again.
    def select_on(self):
        self.is_activated = True
        self.highlight_on()

    def deactivate(self):
        self.is_activated = False
        self.highlight_off()

    def highlight_on(self):
        self.is_highlighted = True
        self.draw_button_highlighted()
        self.draw_sprite()
        self.update_population()
        pygame.display.update()

    def highlight_off(self):
        self.is_highlighted = False
        self.draw_button_normal()
        self.draw_sprite()
        self.update_population()
        pygame.display.update()

    def draw_button_normal(self):
        button = pygame.image.load(os.path.join(buttons_dir, "popbutton" + png_ext))
        screen.blit(button, self.rect)
        pygame.display.update()

    def draw_button_highlighted(self):
        button = pygame.image.load(os.path.join(buttons_dir, "popbuttonselected" + png_ext))
        screen.blit(button, self.rect)
        pygame.display.update()

    def draw_sprite(self):
        sprite = pygame.image.load((os.path.join(sprites_dir, self.species + png_ext)))
        sprite_rect = Rect((self.x + 97, self.y + 2), (24, 24))
        screen.blit(sprite, sprite_rect)
        pygame.display.update()

    def update_population(self):
        font = pygame.font.SysFont("monospace", 22, True, False)
        population = str(len(self.group))

        # generate coordinates and render text
        num_x = 80
        num_y = (self.position * 36) + 15
        label = font.render(population, 1, (0, 0, 0))

        white = pygame.Surface((50, 21))
        white.fill((255, 255, 255))
        screen.blit(white, (num_x - 26, num_y + 2))

        # blit new text
        screen.blit(label, (num_x, num_y))
        pygame.display.update()
