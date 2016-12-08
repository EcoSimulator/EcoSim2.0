from sprite import Sprite
import pygame
import vision
from properties import *


class PlantSprite(Sprite):
    sprite_image = pygame.image.load(os.path.join(sprites_dir, "plant.png"))

    def __init__(self, world_map, screen, coordinates, GRID_LOCK, rect_size=None):
        Sprite.__init__(self, world_map, screen, self.sprite_image, coordinates, GRID_LOCK, rect_size)
        self.type = "plant"
        self.movable_terrain = world_map.get_all_land_tiles()
        self.is_pollinated = False
        self.polinate_timer = 0

    def move(self, target=None):
        """
        :param target: meaningless to plants, just there to suppress warning
        :return: changes plant pollination on a timer right now
        """
        self.polinate_timer += 1
        if self.polinate_timer % 25 == 0:
            self.pollinate()
        self.display(self.image, self.rect)

    def spawn(self):
        """
        :return: puts the sprite on the map
        """
        self.screen.blit(self.image, self.rect)
        pygame.display.update()  # update pygame

    def pollinate(self):
        """
        :return: checks for pollination and either pollinates or de-pollinates accordingly
        """
        if not self.is_pollinated:
            self.image = pygame.image.load(os.path.join(sprites_dir, "plantpollinated.png"))
            self.is_pollinated = True
        elif self.is_pollinated:
            self.image = pygame.image.load(os.path.join(sprites_dir, "plant.png"))
            self.is_pollinated = False
