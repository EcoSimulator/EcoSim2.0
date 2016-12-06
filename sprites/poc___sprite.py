import pygame
from pygame.locals import *
import random
import time


class Sprite(pygame.sprite.DirtySprite):
    def __init__(self, map, screen):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = pygame.image.load("resources/sprites/octopus.png")
        self.tile = map.get_tile_at_pixel((random.randint(600, 700), random.randint(600, 700)))
        self.rect = Rect(self.tile.location, (24, 24))
        self.tile.set_sprite(self)
        self.map = map
        self.screen = screen
        print self.__class__

    # map is just a parameter for ease of testing here
    # should be a globally accessible variable
    def spawn(self, screen):
        screen.blit(self.image, self.rect)

    def move_octopus(self):
        while True:
            self.screen.blit(self.tile.image, self.rect)
            self.tile.set_sprite(None)
            adjacent = self.map.get_surrounding_movable_tiles(self.tile)
            if len(adjacent) != 0:
                index = random.randint(0, len(adjacent) - 1)
                self.tile = adjacent[index]
                self.rect = Rect(self.tile.location, (24, 24))
                self.screen.blit(self.image, self.rect)
                self.tile.set_sprite(self)
                pygame.display.update()
                time.sleep(0.5)

    def is_water(self, tile):
        if tile.name.startswith('water'):
            return True
        else:
            return False
