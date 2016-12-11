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

    def __init__(self, world_map, GRID_LOCK, coordinates=None):
        """
        Create a DeerSprite object
        :param world_map: WorldMap Object
        :param coordinates: Array of coordinates [x,y]
        :param GRID_LOCK: Lock for screen (for threading)
        """

        ''' Take parameters, and Sprite Constants '''
        super(DeerSprite, self).__init__(world_map, DeerSprite.IMAGE, GRID_LOCK,
                                        DeerSprite.HEALTH_BAR, DeerSprite.AVG_SPEED,
                                        DeerSprite.VISION, coordinates)

        self.type = "deer"
        self.targets = ["wolf"]
        self.movable_terrain = world_map.get_all_land_tile_types()

    def move(self):
        """
        @Override
            Move sprite to a specified target tile (target).
            Otherwise, moves sprite to a random adjacent tile.
        :param target: Target tile to move sprite.
        """
        visible_tiles = vision.vision(self.vision, self.world_map, self.tile)
        target_tile = vision.find_target(visible_tiles, self.targets)
        if target_tile:
            move_to_tile = vision.flee(self.tile, target_tile, self.world_map)
            if self.is_movable_terrain(move_to_tile) and self.not_contains_sprite(move_to_tile):
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
    sprite = DeerSprite(world_map, GRID_LOCK, [10,10])
    sprite.thread.start()


    # Loop until Pygame exits
    done = False
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True

if __name__ == '__main__':
    main()

