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

class Sprite(pygame.sprite.DirtySprite):

    def __init__(self,world_map, surface, sprite_image, coordinates, GRID_LOCK, rect_size=None):

        pygame.sprite.DirtySprite.__init__(self)

        ''' Sprite Attributes '''
        self.image = sprite_image
        self.loc_x = coordinates[0]
        self.loc_y = coordinates[1]

        ''' Map Display Data'''
        self.map = world_map
        self.tile = world_map.get_tile_at_pixel(coordinates)
        #self.tile.tile_print()
        self.rect_size = (24, 24) if rect_size is None else rect_size
        self.rect = Rect(self.tile.location, self.rect_size)

        ''' Screen Surface Data '''
        self.surface = surface
        self.GRID_LOCK = GRID_LOCK  # Screen GridLOCK (Threading)

    def run(self):
        """
        Runs the Sprite
        """
        self.spawn()
        while True:
            self.move()

    def spawn(self):
        self.surface.blit(self.image, self.rect)
        pygame.display.flip()  # update pygame

    def move(self):

        # Blit a fresh tile in current position #
        self.display(self.tile.image, self.rect)

        # Get list of adjacent tiles #
        adjacent = self.map.get_surrounding_movable_tiles(self.tile)

        # Move to random tile #
        next_tile_index = self.choose_index(len(adjacent))
        self.tile = adjacent[next_tile_index]

        # Save associated Rect
        self.rect = Rect(self.tile.location, self.rect_size)

        # Blit sprite to screen
        self.display(self.image, self.rect)

    def display(self, image, rect):
        self.GRID_LOCK.acquire()        # Lock
        self.surface.blit(image, rect)  # Blit to surface
        pygame.display.flip()           # Update pygame
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