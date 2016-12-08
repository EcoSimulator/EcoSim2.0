import pygame


class AllSpritesGroup(pygame.sprite.Group):
    def __init__(self, *sprites):
        pygame.sprite.Group.__init__(self, sprites)

    def add(self, sprite):
        pygame.sprite.Group.add(self, sprite)

    def remove(self, sprite):
        pygame.sprite.Group.remove(self, sprite)