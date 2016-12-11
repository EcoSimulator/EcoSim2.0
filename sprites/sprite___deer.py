import os
import pygame, vision
from sprite___animal import AnimalSprite
from properties import sprites_dir
from health_bar import HealthBar
from properties import screen


class DeerSprite(AnimalSprite):
    # Constants for the initial state of all DeerSprites
    IMAGE = pygame.image.load(os.path.join(sprites_dir, "deer.png"))
    HEALTH_BAR = HealthBar(100)
    AVG_SPEED = 0.2
    VISION = 4

    def __init__(self, world_map, coordinates, GRID_LOCK):
        """

        :param world_map:
        :param coordinates:
        :param GRID_LOCK:
        """

        ''' Take parameters, and Sprite Constants '''
        super(DeerSprite, self).__init__(world_map, screen, DeerSprite.IMAGE,
                                        coordinates, GRID_LOCK, DeerSprite.HEALTH_BAR,
                                        DeerSprite.HEALTH_BAR, DeerSprite.AVG_SPEED,
                                        DeerSprite.VISION)

        self.type = "deer"
        self.targets = ["wolf"]
        self.movable_terrain = world_map.get_all_land_tile_types()

    def move(self):
        """

        :return:
        """
        visible_tiles = vision.vision(self.vision, self.world_map, self.tile)
        target_tile = vision.find_target(visible_tiles, self.targets)
        if target_tile:
            move_to_tile = vision.flee(self.tile, target_tile, self.world_map)
            if self.is_movable_terrain(self, move_to_tile) and self.not_contains_sprite(self, move_to_tile):
                AnimalSprite.move(self, move_to_tile)
            else:
                AnimalSprite.move(self)
        else:
            AnimalSprite.move(self)

