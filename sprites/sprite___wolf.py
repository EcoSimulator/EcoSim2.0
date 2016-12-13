# Import Packages
import os
import pygame
import vision
import random

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
        :param coordinates: Array of coordinates [x,y]
        :param GRID_LOCK: Lock for screen (for threading)
        """

        ''' Take parameters, and Sprite Constants '''
        super(WolfSprite, self).__init__(world_map, WolfSprite.IMAGE,
                                        GRID_LOCK, WolfSprite.HEALTH_BAR,
                                        WolfSprite.AVG_SPEED, WolfSprite.VISION, coordinates)

        self.type = "wolf"
        self.prey = ["deer"]
        self.movable_terrain = world_map.get_all_land_tile_types()
        self.is_leader = False

    def move(self, target=None):
        """
        :return:
        """
        visible_tiles = vision.vision(10, self.world_map, self.tile)
        target_tile = vision.find_target(visible_tiles, self.prey)
        if target_tile:
            move_to_tile = vision.approach(self.tile, target_tile, self.world_map)
            if self.is_movable_terrain(move_to_tile) and self.not_contains_sprite(move_to_tile, self.prey):
                if move_to_tile == target_tile:
                    move_to_tile.contains_sprite.die()
                AnimalSprite.move(self, move_to_tile)
            elif not self.is_leader:
                leader_tile = self.find_leader()
                if leader_tile:
                    move_to_tile = vision.approach(self.tile, leader_tile, self.world_map)
                    if self.is_movable_terrain(move_to_tile) and self.not_contains_sprite(move_to_tile, self.prey):
                        AnimalSprite.move(self, move_to_tile)
                else:
                    AnimalSprite.move(self)
            else:
                AnimalSprite.move(self)
        elif not self.is_leader:
            leader_tile = self.find_leader()
            if leader_tile:
                chance = random.randint(0, 10)
                if chance == 0:
                    AnimalSprite.move(self)
                else:
                    move_to_tile = vision.approach(self.tile, leader_tile, self.world_map)
                    if self.is_movable_terrain(move_to_tile) and self.not_contains_sprite(move_to_tile, self.prey):
                        AnimalSprite.move(self, move_to_tile)
            else:
                AnimalSprite.move(self)
        else:
            AnimalSprite.move(self)

    def find_leader(self):
        for row in self.world_map.tiles:
            for tile in row:
                sprite = tile.contains_sprite
                if sprite is not None:
                    if sprite.type == "wolf" and sprite.is_leader:
                        tiles = self.world_map.get_surrounding_movable_tiles(tile)
                        index = random.randint(0, len(tiles) - 1)
                        return tiles[index]
        return False


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
    sprite = WolfSprite(world_map, [10, 10], GRID_LOCK)
    sprite.thread.start()


    # Loop until Pygame exits
    done = False
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True

if __name__ == '__main__':
    main()


