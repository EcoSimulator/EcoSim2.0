# Author: Jasmine Oliveira
import os
import pygame, vision
from sprite___animal import AnimalSprite
from properties import sprites_dir
from health_bar import HealthBar
from properties import screen


class HareSprite(AnimalSprite):
    # Constants for the initial state of all HareSprites
    IMAGE = pygame.image.load(os.path.join(sprites_dir, "hare.png"))
    HEALTH_BAR = HealthBar(100)
    AVG_SPEED = 0.1
    VISION = 2

    def __init__(self, world_map, GRID_LOCK, coordinates=None):
        """
        Create a HareSprite object
        :param world_map: WorldMap Object
        :param coordinates: Array of coordinates [x,y]
        :param GRID_LOCK: Lock for screen (for threading)
        """

        ''' Take parameters, and Sprite Constants '''
        super(HareSprite, self).__init__(world_map, HareSprite.IMAGE, GRID_LOCK,
                                         HareSprite.HEALTH_BAR, HareSprite.AVG_SPEED,
                                         HareSprite.VISION, coordinates)

        self.type = "hare"
        self.predators = ["wolf", "lynx"]
        self.prey = ["plant"]
        self.movable_terrain = world_map.get_all_land_tile_types()

    def move(self, target=None):
        visible_tiles = vision.vision(4, self.world_map, self.tile)
        flight_tile = vision.find_target(visible_tiles, self.predators)
        target_tile = vision.find_target(visible_tiles, self.prey)
        if flight_tile:
            move_to_tile = vision.flee(self.tile, flight_tile, self.world_map)
            if self.is_movable_terrain(move_to_tile) and self.not_contains_sprite(move_to_tile):
                AnimalSprite.move(self, move_to_tile)
            else:
                AnimalSprite.move(self)
        elif target_tile:
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
    sprite = HareSprite(world_map, GRID_LOCK)
    sprite.thread.start()

    # Loop until Pygame exits
    done = False
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True


if __name__ == '__main__':
    main()