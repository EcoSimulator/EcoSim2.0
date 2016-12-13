# -----------------------------------------------------------------------------
# Author: Jasmine Oliveira
# Author: Matthew Severence
# Date:   12/2016
# -----------------------------------------------------------------------------
# widget___sprite.py
# -----------------------------------------------------------------------------
# Module designed to represent a generic sprite.
#


import pygame
from pygame.locals import *
import random
import time
import threading
from threading import Thread
from properties import *


class Sprite(pygame.sprite.DirtySprite):

    def __init__(self, world_map, sprite_image, GRID_LOCK, coordinates=None, rect_size=None):
        """
        :param world_map: the current map
        :param screen: the current screen
        :param sprite_image: the image to give to the sprite
        :param coordinates: where to create the sprite
        :param GRID_LOCK: thread lock
        :param rect_size: size of the sprite- defaults to (24, 24)
        """
        pygame.sprite.DirtySprite.__init__(self)

        ''' Sprite Attributes '''
        self.type = "sprite"
        self.image = sprite_image

        ''' Map Display Data'''
        self.world_map = world_map
        # set the movable terrain for a default sprites to everything
        self.movable_terrain = world_map.tile_types

        # self.tile = world_map.get_tile_at_pixel(coordinates)
        self.rect_size = (24, 24) if rect_size is None else rect_size

        if coordinates is None:
            self.coordinates = None
            self.tile = None
            self.rect = None  # Rect(self.tile.locationPX, self.rect_size)
        else:
            self.coordinates = coordinates
            self.loc_x = coordinates[0]
            self.loc_y = coordinates[1]
            self.tile = world_map.get_tile_at_pixel(coordinates)
            self.rect = Rect(self.tile.locationPX, self.rect_size)

        ''' Screen Surface Data '''
        self.screen = screen
        self.GRID_LOCK = GRID_LOCK  # Screen GridLOCK (Threading)

        # set the movable terrain for a default sprites to everything
        self.movable_terrain = world_map.tile_types
        # targetable sprite types
        # used to override collision avoidance
        self.predators = []
        self.prey = []
        self.shadow = None
        self.shadow_tile = None
        self.thread = Thread(target=self.run)
        self.thread.daemon = True
        self.is_alive = True

    def run(self):
        """
        :return: Runs the Sprite's thread
        """
        self.spawn()
        while self.is_alive:
            self.move()
            time.sleep(0.2)

    def spawn(self):
        """
        :return: puts the sprite on the map
        """
        if self.coordinates is None:
            possible_spawn_tiles = self.world_map.get_all_tiles_of_types(self.movable_terrain)
            select = random.randint(0, len(possible_spawn_tiles))
            self.tile = possible_spawn_tiles[select]
            self.rect = Rect(self.tile.locationPX, self.rect_size)
        self.tile.set_sprite(self)  # adds the sprite to the current tile
        self.screen.blit(self.image, self.rect)
        pygame.display.update()  # update pygame

    def move(self, target=None):
        """
        :param target: target tile to move to
        :return: moves the sprite to either a target or randomly
        """
        # if the sprite isn't targeting another sprite
        if target is None:
            # Get list of adjacent tiles
            adjacent = self.world_map.get_surrounding_movable_tiles(self.tile)
            adjacent = self.movable_tile_filter(adjacent)

            # do nothing if no movable tiles
            if len(adjacent) != 0:
                index = random.randint(0, len(adjacent) - 1)
                target = adjacent[index]
                self.display(target)
        # if it is targeting another specific tile
        else:
            self.display(target)

    def display(self, target):
        self.tile.set_sprite(None)
        self.GRID_LOCK.acquire()
        self.screen.blit(self.tile.image, self.rect)   # Blit blank tile to surface
        self.tile = target
        self.rect = Rect(self.tile.locationPX, (24, 24))
        # put the sprite in the tile
        if self.shadow is not None and self.shadow_tile is not None:
            self.screen.blit(self.shadow_tile.image, self.shadow_tile.rect)
            self.shadow_tile = self.world_map.get_tile_by_index((self.tile.location_t[1] + 1, self.tile.location_t[0]))
            self.screen.blit(self.shadow, self.shadow_tile.rect)
        self.screen.blit(self.image, self.rect)
        pygame.display.update()
        self.GRID_LOCK.release()
        self.tile.set_sprite(self)

    def die(self):
        """
        :return: None, removes sprite from game
        """
        # blit over the sprite
        # remove it from the tile
        # set it to not alive to end thread
        self.display(self.tile)
        self.tile.set_sprite(None)
        self.is_alive = False
        self.kill()

    def not_contains_sprite(self, tile, exceptions=None):
        """
        :param tile: the tile being check
        :param exceptions: exceptions for sprite collisions
        :return: True if no sprite present
        """
        if tile is not None and (tile.contains_sprite is None or tile.ignore_contents):
            return True
        elif exceptions is not None:
            for exception in exceptions:
                if tile.contains_sprite.type == exception:
                    return True
        else:
            return False

    def is_movable_terrain(self, tile):
        """
        :param tile: tile to check
        :return: True if the tile can be moved to by the sprite, False otherwise
        """
        if tile is not None:
            return tile.tile_type in self.movable_terrain
        else:
            return False

    def movable_tile_filter(self, tiles):
        """
        :param tiles: a list of potential movable tiles
        :return: the tiles filtered of any none movable tiles
        """
        tiles = filter(self.not_contains_sprite, tiles)
        tiles = filter(self.is_movable_terrain, tiles)
        return tiles

    def choose_index(self, max_index):
        """
        Chooses an random index
        :param max_index: Max index to choose random number
        :return: int: random number between 1 and max_index
        """
        return random.randint(0, max_index - 1)

    def update(self):
        self.thread.start()


def main():
    """
    Sprite Implementation Example
    """
    from widgets.widget___tiled_map import WorldMap
    from properties import sprites_dir
    import os, threading
    from threading import Thread
    pygame.init()

    # Map Setup
    screen = pygame.display.set_mode((800, 800))
    world_map = WorldMap("map2.tmx", (23, 23))
    world_map.render_entire_map()

    # Threading
    GRID_LOCK = threading.Lock()

    # Sprite Setup
    image_path = os.path.join(sprites_dir, "deer.png")
    image = pygame.image.load(image_path)

    sprite = Sprite(world_map, image, GRID_LOCK, (50, 50))

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