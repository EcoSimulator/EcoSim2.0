import os
import pygame, vision
from sprite___animal import AnimalSprite
from properties import sprites_dir
from health_bar import HealthBar
from properties import screen


class BeesSprite(AnimalSprite):
    # Constants for the initial state of all BeesSprites
    IMAGE = pygame.image.load(os.path.join(sprites_dir, "bees.png"))
    HEALTH_BAR = HealthBar(100)
    AVG_SPEED = 0.2
    VISION = 4

    def __init__(self, world_map, GRID_LOCK, coordinates=None):
        """
        Create a BeesSprite object
        :param world_map: WorldMap Object
        :param coordinates: Array of coordinates [x,y]
        :param GRID_LOCK: Lock for screen (for threading)
        """

        ''' Take parameters, and Sprite Constants '''
        super(BeesSprite, self).__init__(world_map, BeesSprite.IMAGE, GRID_LOCK,
                                        BeesSprite.HEALTH_BAR, BeesSprite.AVG_SPEED,
                                        BeesSprite.VISION, coordinates)

        self.type = "bees"
        self.prey = ["plant"]

    def move(self, target=None):
        """
        @Override
            Move sprite to a specified target tile (target).
            Otherwise, moves sprite to a random adjacent tile.
        :param target: Target tile to move sprite.
        """
        visible_tiles = vision.vision(15, self.world_map, self.tile)
        visible_tiles = filter(BeesSprite.pollinated_filter, visible_tiles)
        target_tile = vision.find_target(visible_tiles, self.prey)
        if target_tile:
            move_to_tile = vision.approach(self.tile, target_tile, self.world_map)
            if self.is_movable_terrain(move_to_tile) and \
                    self.not_contains_sprite(move_to_tile, self.prey):
                if move_to_tile == target_tile:
                    move_to_tile.contains_sprite.pollinate()
                AnimalSprite.move(self, move_to_tile)
            else:
                AnimalSprite.move(self)
        else:
            AnimalSprite.move(self)

    @staticmethod
    def pollinated_filter(tile):
        """
        Determines if there is an unpollinated plant sprite on the given tile
        :param tile: Given tile in WorldMap object
        :return: False: if plant is pollinated
                 True: if plant is not pollinated
        """
        current_sprite = tile.contains_sprite
        if current_sprite and current_sprite.type == "plant" and current_sprite.is_pollinated:
            return False
        else:
            return True


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
    sprite = BeesSprite(world_map, GRID_LOCK, [10,10])
    sprite.thread.start()


    # Loop until Pygame exits
    done = False
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True

if __name__ == '__main__':
    main()
