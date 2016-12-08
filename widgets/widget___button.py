import pygame
import os
from properties import *
from pygame.locals import *


class Button:
    # Important: When you create a button, make sure to append it to a list, or monitor it continuously.
    # *args is of variable length. Pass the method name in without parentheses,
    # then pass as many arguments as necessary, separated by commas.
    def __init__(self, screen, location, image, method, *args):
        self.screen = screen
        self.location = location
        self.image = image
        self.method = method
        self.args = args
        self.rect = Rect((0, 0), (0, 0))

    # At the moment, buttons are all a standard size. We can change this if necessary.
    def draw(self):
        self.rect = Rect((self.location[0], self.location[1]), (90, 27))
        img = pygame.image.load(os.path.join(buttons_dir, self.image + png_ext))
        self.screen.blit(img, self.rect)
        pygame.display.update()

    def monitor(self):
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
