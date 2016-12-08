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
from sprites.poc___bear import BearSprite
from groups.group___all_sprites import AllSpritesGroup


def sprite_test():
    pygame.init()

    world_map = widget___tiled_map.WorldMap("map2.tmx", (23, 23))

    world_map.render_entire_map()

    GRID_LOCK = threading.Lock()

    world_map.get_all_land_tile_types()
    s1 = PlantSprite(world_map, GRID_LOCK)
    s2 = DeerSprite(world_map, GRID_LOCK, (50, 50))

    sprites_a = AllSpritesGroup(s1, s2)
    sprites_b = AllSpritesGroup()
    s3 = WolfSprite(world_map, GRID_LOCK)
    s4 = BeesSprite(world_map, GRID_LOCK)
    s5 = FishSprite(world_map, GRID_LOCK)
    s6 = BearSprite(world_map, GRID_LOCK)

    sprites_a.add(s3)
    sprites_b.add(s4)
    sprites_b.add(s5)
    sprites_b.add(s6)

    sprites_a.update()
    sprites_b.update()

    while True:
        pass


sprite_test()
