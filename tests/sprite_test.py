import pygame
import os
import threading
from properties import *
from widgets import widget___tiled_map
from threading import Thread
from sprites.sprite import Sprite
from sprites.poc___wolf import WolfSprite
from sprites.poc___deer import DeerSprite
from sprites.poc___plant import PlantSprite
from sprites.poc___bees import BeesSprite
from sprites.poc___fish import FishSprite


def sprite_test():
    pygame.init()

    screen = pygame.display.set_mode((800, 800))

    world_map = widget___tiled_map.WorldMap("map2.tmx", (23, 23))

    world_map.render_entire_map()

    GRID_LOCK = threading.Lock()
    image = pygame.image.load(os.path.join(sprites_dir, "octopus.png"))

    world_map.get_all_land_tile_types()

    s1 = PlantSprite(world_map, GRID_LOCK, (0, 0))
    s2 = DeerSprite(world_map, GRID_LOCK, (50, 50))
    s3 = DeerSprite(world_map, GRID_LOCK)
    s4 = BeesSprite(world_map, GRID_LOCK)
    s5 = FishSprite(world_map, GRID_LOCK)
    # s1.spawn()
    # s2.spawn()
    # s3.spawn()
    # s4.spawn()
    # pygame.display.update()

    # one = Thread(target=s1.run)
    # one.daemon = True
    #
    # two = Thread(target=s2.run)
    # two.daemon = True
    #
    # three = Thread(target=s3.run)
    # three.daemon = True
    #
    # four = Thread(target=s4.run)
    # four.daemon = True

    s1.thread.start()
    s2.thread.start()
    s3.thread.start()
    s4.thread.start()
    s5.thread.start()
    while True:
        pass


sprite_test()
