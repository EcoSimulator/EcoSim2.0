import pygame
import os
from properties import *
from pygame.locals import *


class Button:
    # Important: When you create a button, make sure to append it to a list, or monitor it continuously.
    # *args is of variable length. Pass the method name in without parentheses,
    # then pass as many arguments as necessary, separated by commas.
    def __init__(self, location, image, highlight_image, method, *args):
        self.location = location
        self.image = image
        self.highlight_image = highlight_image
        self.method = method
        self.args = args
        self.rect = Rect((0, 0), (0, 0))
        self.is_hovered = False

    # At the moment, buttons are all a standard size. We can change this if necessary.
    def draw(self):
        self.rect = Rect((self.location[0], self.location[1]), (90, 27))
        img = pygame.image.load(os.path.join(buttons_dir, self.image + png_ext))
        screen.blit(img, self.rect)
        pygame.display.update()

    def monitor(self):
        mouse = pygame.mouse.get_pos()
        # highlight button if it's hovered and not currently highlighted
        if self.rect.collidepoint(mouse):
            if not self.is_hovered:
                self.hover_on()
        # de-highlight button if it's highlighted and not currently hovered
        if not self.rect.collidepoint(mouse):
            if self.is_hovered:
                self.hover_off()
        # activate button if it's clicked on
        if self.is_pressed():
            self.activate()

    def is_pressed(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.rect.collidepoint(mouse):
            if click[0] == 1:
                self.activate()

    def activate(self):
        result = self.method(*self.args)
        return result

    # highlight on hover
    def hover_on(self):
        self.is_hovered = True
        img = pygame.image.load(os.path.join(buttons_dir, self.highlight_image + png_ext))
        screen.blit(img, self.rect)
        pygame.display.update()

    def hover_off(self):
        self.is_hovered = False
        img = pygame.image.load(os.path.join(buttons_dir, self.image + png_ext))
        screen.blit(img, self.rect)
        pygame.display.update()