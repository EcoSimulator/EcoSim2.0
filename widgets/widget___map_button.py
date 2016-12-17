import pygame
import os
from properties import *
from pygame.locals import *


class MapButton:
    # Important: When you create a button, make sure to append it to a list, or monitor it continuously.
    # *args is of variable length. Pass the method name in without parentheses,
    # then pass as many arguments as necessary, separated by commas.
    def __init__(self, location, map, method):
        self.location = location
        self.map = map
        self.method = method
        self.rect = Rect((0, 0), (0, 0))
        self.is_hovered = False

    # At the moment, buttons are all a standard size. We can change this if necessary.
    def draw(self):
        # map preview image
        self.prev_rect = Rect((self.location[0] + 6, self.location[1] + 6), (120, 120))
        map_img = pygame.image.load(os.path.join(map_preview_dir, self.map + png_ext))
        # scale to fit in the button
        map_scale = pygame.transform.scale(map_img, (120, 120))

        # button frame (provides hover feedback)
        self.rect = Rect(self.location, (132, 132))
        frame_img = pygame.image.load(os.path.join(map_preview_dir, "map_btn_black" + png_ext))

        screen.blit(map_scale, self.prev_rect)
        screen.blit(frame_img, self.rect)
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
                return True

    def activate(self):
        result = self.method(self.map)
        return result

    # highlight on hover
    def hover_on(self):
        self.is_hovered = True
        img = pygame.image.load(os.path.join(map_preview_dir, "map_btn_white" + png_ext))
        screen.blit(img, self.rect)
        pygame.display.update()

    def hover_off(self):
        self.is_hovered = False
        img = pygame.image.load(os.path.join(map_preview_dir, "map_btn_black" + png_ext))
        screen.blit(img, self.rect)
        pygame.display.update()