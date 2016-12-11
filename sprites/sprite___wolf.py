# Import Packages
import os
import pygame
import vision

''' Import Classes '''
from sprite___animal import AnimalSprite
from health_bar import HealthBar
from properties import sprites_dir


class WolfSprite(AnimalSprite):
    # Constants for the initial state of a DeerSprite
    IMAGE = pygame.image.load(os.path.join(sprites_dir, "wolf.png"))
    HEALTH_BAR = HealthBar(100)
    AVG_SPEED = 0.2
    VISION = 4

    def __init__(self, world_map, GRID_LOCK, coordinates=None):
        """
        Create a WolfSprite object
        :param world_map: WorldMap Object
        :param screen: Pygame surface object
        :param coordinates: Array of coordinates [x,y]
        :param GRID_LOCK: Lock for screen (for threading)
        """

        ''' Take parameters, and Sprite Constants '''
        super(WolfSprite, self).__init__(world_map, WolfSprite.IMAGE,
                                        coordinates, GRID_LOCK, WolfSprite.HEALTH_BAR,
                                        WolfSprite.AVG_SPEED, WolfSprite.VISION)

        self.type = "wolf"
        self.targets = ["deer"]
        self.movable_terrain = []

    def move(self):
        """

        :return:
        """
        visible_tiles = vision.vision(4, self.world_map, self.tile)
        target_tile = vision.find_target(visible_tiles, self.prey)
        if target_tile:
            move_to_tile = vision.approach(self.tile, target_tile, self.world_map)
            if self.is_movable_terrain(self, move_to_tile) and self.not_contains_sprite(self, move_to_tile, self.prey):
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

    sprite = WolfSprite(world_map, [10, 10], GRID_LOCK)

    # Create Thread
    t = Thread(target=sprite.run)
    t.daemon = True

    # Run Sprite
    t.start()

    # Loop until Pygame exits
    done = False
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True

if __name__ == '__main__':
    main()


