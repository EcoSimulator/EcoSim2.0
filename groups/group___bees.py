import pygame


class BeesGroup(pygame.sprite.Group):
    def __init__(self, *sprites):
        pygame.sprite.Group.__init__(self, sprites)
        self.type = "bees"

    def get_type(self):
        return self.type
