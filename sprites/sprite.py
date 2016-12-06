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


class Sprite(pygame.sprite.DirtySprite):

    def __init__(self, world_map, screen, sprite_image, coordinates, GRID_LOCK, rect_size=None):

        pygame.sprite.DirtySprite.__init__(self)

        ''' Sprite Attributes '''
        self.image = sprite_image
        self.loc_x = coordinates[0]
        self.loc_y = coordinates[1]

        ''' Map Display Data'''
        self.world_map = world_map
        self.tile = world_map.get_tile_at_pixel(coordinates)
        self.rect_size = (24, 24) if rect_size is None else rect_size
        self.rect = Rect(self.tile.locationPX, self.rect_size)

        ''' Screen Surface Data '''
        self.screen = screen
        self.GRID_LOCK = GRID_LOCK  # Screen GridLOCK (Threading)

        # set the movable terrain for a default sprites to everything
        self.movable_terrain = world_map.tile_types

    def run(self):
        """
        Runs the Sprite
        """
        self.spawn()
        while True:
            self.move()
            time.sleep(0.5)

    def spawn(self):
        self.tile.set_sprite(self)
        self.screen.blit(self.image, self.rect)
        pygame.display.update()  # update pygame

    def move(self, target=None):
        if target is None:
            # Get list of adjacent tiles
            adjacent = self.world_map.get_surrounding_movable_tiles(self.tile)
            adjacent = self.movable_tile_filter(adjacent)

            # do nothing if no movable tiles
            if len(adjacent) != 0:
                # Blit a fresh tile in current position
                self.display(self.tile.image, self.rect)
                # removes the sprite from the tile
                self.tile.set_sprite(None)
                # move to one of the adjacent tiles randomly
                index = random.randint(0, len(adjacent) - 1)
                self.tile = adjacent[index]
                self.rect = Rect(self.tile.locationPX, (24, 24))
                # put the sprite in the tile
                self.tile.set_sprite(self)
                # Blit sprite to screen
                self.display(self.image, self.rect)
        else:
            self.display(self.tile.image, self.rect)
            # removes the sprite from the tile
            self.tile.set_sprite(None)
            # move to one of the adjacent tiles randomly
            self.tile = target
            self.rect = Rect(self.tile.locationPX, (24, 24))
            # put the sprite in the tile
            self.tile.set_sprite(self)
            # Blit sprite to screen
            self.display(self.image, self.rect)

    def __contains_sprite(self, tile):
        """
        :param tile: the tile being check
        :return: True if no
        """
        if tile.contains_sprite is None:
            return True
        else:
            return False

    def __is_movable_terrain(self, tile):
        var = tile.tile_type in self.movable_terrain
        return var

    def movable_tile_filter(self, tiles):
        tiles = filter(self.__contains_sprite, tiles)
        tiles = filter(self.__is_movable_terrain, tiles)
        return tiles

    def display(self, image, rect):
        self.GRID_LOCK.acquire()        # Lock
        self.screen.blit(image, rect)   # Blit to surface
        pygame.display.update()         # Update pygame
        self.GRID_LOCK.release()        # Release Lock

    def choose_index(self, max_index):
        """
        Chooses an random index
        :param max_index: Max index to choose random number
        :return: int: random number between 1 and max_index
        """
        return random.randint(0, max_index - 1)


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

    sprite = Sprite(world_map, screen, image, (50, 50), GRID_LOCK)

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