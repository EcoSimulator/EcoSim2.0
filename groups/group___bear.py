import pygame


class BearGroup(pygame.sprite.Group):
    def __init__(self, *sprites):
        pygame.sprite.Group.__init__(self, sprites)
        self.type = "bear"
