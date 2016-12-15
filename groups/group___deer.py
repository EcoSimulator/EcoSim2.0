import pygame


class DeerGroup(pygame.sprite.Group):
    def __init__(self, *sprites):
        pygame.sprite.Group.__init__(self, sprites)
        self.type = "deer"

    def get_type(self):
        return self.type
