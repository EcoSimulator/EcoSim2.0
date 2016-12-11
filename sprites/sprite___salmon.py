import os
import pygame, vision
from sprite___animal import AnimalSprite
from properties import sprites_dir
from health_bar import HealthBar
from properties import screen


class SalmonSprite(AnimalSprite):
    # Constants for the initial state of all SalmonSprites
    IMAGE = pygame.image.load(os.path.join(sprites_dir, "salmon.png"))
    HEALTH_BAR = HealthBar(100)
    AVG_SPEED = 0.2
    VISION = 4

    def __init__(self, world_map, GRID_LOCK, coordinates=None):
        """
        Create a SalmonSprite object
        :param world_map: WorldMap Object
        :param coordinates: Array of coordinates [x,y]
        :param GRID_LOCK: Lock for screen (for threading)
        """

        ''' Take parameters, and Sprite Constants '''
        super(SalmonSprite, self).__init__(world_map, SalmonSprite.IMAGE, GRID_LOCK,
                                        SalmonSprite.HEALTH_BAR, SalmonSprite.AVG_SPEED,
                                        SalmonSprite.VISION, coordinates)

        self.type = "fish"
        self.movable_terrain = world_map.get_all_water_tile_types()


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
    sprite = SalmonSprite(world_map, GRID_LOCK)
    sprite.thread.start()


    # Loop until Pygame exits
    done = False
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True

if __name__ == '__main__':
    main()
