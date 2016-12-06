import pygame
import os
from properties import *
from pygame.locals import *


class Button:
    def __init__(self, x, y, image, function):
        self.x = x
        self.y = y
        self.image = image
        self.function = function
        self.rect = Rect((0, 0), (0, 0))

    def draw(self):
        self.rect = Rect((self.x, self.y), (90, 27))
        img = pygame.image.load(os.path.join(buttons_dir, self.image + png_ext))
        #will need code to add to a universal button collection

    def is_pressed(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.rect.right > mouse[0] > self.rect.left and self.rect.top > mouse[1] > self.rect.bottom:
            return click[0] == 1

    def get_function(self):
        return self.function
