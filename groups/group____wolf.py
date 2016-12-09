import pygame


class WolfGroup(pygame.sprite.Group):
    def __init__(self, *sprites):
        pygame.sprite.Group.__init__(self, sprites)
        self.type = "wolf"
