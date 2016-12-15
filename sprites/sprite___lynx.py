#  Import Packages
import os
import pygame
import vision
import random

''' Import Classes '''
from sprite___animal import AnimalSprite
from health_bar import HealthBar
from properties import sprites_dir


class LynxSprite(AnimalSprite):
    # Constants for the initial state of a DeerSprite
    IMAGE = pygame.image.load(os.path.join(sprites_dir, "lynx.png"))
    HEALTH_BAR = HealthBar(100)
    AVG_SPEED = 0.2
    VISION = 4

    def __init__(self, world_map, GRID_LOCK, coordinates=None):
        """
        Create a LynxSprite object
        :param world_map: WorldMap Object
        :param coordinates: Array of coordinates [x,y]
        :param GRID_LOCK: Lock for screen (for threading)
        """

        ''' Take parameters, and Sprite Constants '''
        super(LynxSprite, self).__init__(world_map, LynxSprite.IMAGE,
                                        GRID_LOCK, LynxSprite.HEALTH_BAR,
                                        LynxSprite.AVG_SPEED, LynxSprite.VISION, coordinates)

        self.type = "lynx"
        self.prey = ["deer", "hare"]
        self.movable_terrain = world_map.get_all_land_tile_types()

    def move(self):
        """
        :return:
        """
        visible_tiles = vision.vision(4, self.world_map, self.tile)
        target_tile = vision.find_target(visible_tiles, self.prey)
        if target_tile:
            move_to_tile = vision.approach(self.tile, target_tile, self.world_map)
            if self.is_movable_terrain(move_to_tile) and self.not_contains_sprite(move_to_tile, self.prey):
                if move_to_tile == target_tile:
                    move_to_tile.contains_sprite.die()
                AnimalSprite.move(self, move_to_tile)
            else:
                AnimalSprite.move(self)
        else:
            AnimalSprite.move(self)

def main():
    """
    Sprite Implementation Example
    """
    from widgets.widget___tiled_map import WorldMap
    import pygame
    import threading
    from threading import Thread
    pygame.init()

    # Map Setup
    screen = pygame.display.set_mode((800, 800))
    world_map = WorldMap("map2.tmx", (23, 23))
    world_map.render_entire_map()

    # Threading
    GRID_LOCK = threading.Lock()

    # Create Thread
    sprite = LynxSprite(world_map, GRID_LOCK)
    sprite.thread.start()


    # Loop until Pygame exits
    done = False
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True

if __name__ == '__main__':
    main()


