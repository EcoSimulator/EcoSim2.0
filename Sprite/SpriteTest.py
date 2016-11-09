import pygame
from pygame.locals import *
import random


class Sprite(pygame.sprite.DirtySprite):
    def __init__(self, map):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = pygame.image.load("../Resources/sprites/octopus.png")
        self.tile = map.get_tile_at_pixel((random.randint(600, 700), random.randint(600, 700)))
        self.rect = Rect(self.tile.location, (24, 24))

    # map is just a parameter for ease of testing here
    # should be a globally accessible variable
    def spawn(self, screen):
        screen.blit(self.image, self.rect)

    def move(self, map, screen):
        screen.blit(self.tile.image, self.rect)
        adjacent = filter(self.is_water, map.get_surrounding_moveable_tiles(self.tile))
        index = random.randint(0, len(adjacent) - 1)
        self.tile = adjacent[index]
        self.rect = Rect(self.tile.location, (24, 24))
        screen.blit(self.image, self.rect)

    def is_water(self, tile):
        if tile.name.startswith('water'):
            return True
        else:
            return False
