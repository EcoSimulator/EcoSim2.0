import os
import pygame, vision, time
from sprite___animal import AnimalSprite
from properties import sprites_dir
from health_bar import HealthBar
from properties import screen


class BearSprite(AnimalSprite):
    # Constants for the initial state of all BearSprites
    IMAGE = pygame.image.load(os.path.join(sprites_dir, "bear.png"))
    HEALTH_BAR = HealthBar(100)
    AVG_SPEED = 0.2
    VISION = 4
    PREY = ["fish"]

    def __init__(self, world_map, GRID_LOCK, coordinates=None):
        """
        Create a BearSprite object
        :param world_map: WorldMap Object
        :param coordinates: Array of coordinates [x,y]
        :param GRID_LOCK: Lock for screen (for threading)
        """

        ''' Take parameters, and Sprite Constants '''
        super(BearSprite, self).__init__(world_map, BearSprite.IMAGE, GRID_LOCK,
                                         BearSprite.HEALTH_BAR, BearSprite.AVG_SPEED,
                                         BearSprite.VISION, coordinates)

        self.type = "bear"
        self.prey = ["fish"]
        self.movable_terrain = world_map.get_all_land_tile_types()

    def move(self, target=None):
        """
        @Override
            Move sprite to a specified target tile (target).
            Otherwise, moves sprite to a random adjacent tile.
        :param target: Target tile to move sprite.
        """
        visible_tiles = vision.vision(8, self.world_map, self.tile)
        target_tile = vision.find_target(visible_tiles, self.prey)
        if target_tile:
            move_to_tile = vision.approach(self.tile, target_tile, self.world_map)
            if self.is_movable_terrain(move_to_tile) and self.not_contains_AnimalSprite(move_to_tile, self.prey):
                if move_to_tile == target_tile:
                    move_to_tile.contains_AnimalSprite.die()
                AnimalSprite.move(self, move_to_tile)
            else:
                AnimalSprite.move(self)
        else:
            AnimalSprite.move(self)

    def run(self):
        """
        @Override
            Runs the BearSprites's thread
        """
        self.spawn()
        while self.is_alive:
            self.move()
            if self.tile.name.startswith("water"):
                time.sleep(self.speed * 2)
            else:
                time.sleep(self.speed)


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
    sprite = BearSprite(world_map, GRID_LOCK, [10,10])
    sprite.thread.start()

    # Loop until Pygame exits
    done = False
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True

if __name__ == '__main__':
    main()
