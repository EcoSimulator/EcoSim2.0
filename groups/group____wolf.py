import pygame
import random
import os
from properties import *

class WolfGroup(pygame.sprite.Group):
    def __init__(self, *sprites):
        pygame.sprite.Group.__init__(self, sprites)
        self.type = "wolf"

    def determine_pack_leader(self):
        index = random.randint(0, len(self) - 1)
        self.sprites()[index].is_leader = True
