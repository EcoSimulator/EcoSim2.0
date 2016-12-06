import pygame
import os
import threading
from properties import *
from widgets import widget___tiled_map
from threading import Thread
from sprites.sprite import Sprite
from sprites.poc___wolf import WolfSprite
from sprites.poc___deer import DeerSprite


def sprite_test():
    pygame.init()

    screen = pygame.display.set_mode((800, 800))

    world_map = widget___tiled_map.WorldMap("map1.tmx", (23, 23))

    world_map.render_entire_map()

    GRID_LOCK = threading.Lock()
    image = pygame.image.load(os.path.join(sprites_dir, "octopus.png"))

    world_map.get_all_land_tiles()

    s1 = WolfSprite(world_map, screen, (1, 1), GRID_LOCK)
    s2 = WolfSprite(world_map, screen, (35, 35), GRID_LOCK)
    s3 = DeerSprite(world_map, screen, (65, 65), GRID_LOCK)
    s4 = DeerSprite(world_map, screen, (95, 95), GRID_LOCK)

    s1.spawn()
    s2.spawn()
    s3.spawn()
    s4.spawn()
    pygame.display.update()

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
    while True:
        pass


sprite_test()
