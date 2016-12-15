import pygame


class FishGroup(pygame.sprite.Group):
    def __init__(self, *sprites):
        pygame.sprite.Group.__init__(self, sprites)
        self.type = "fish"

    # need to return "salmon"
    def get_type(self):
        #return self.type
        return "salmon"
