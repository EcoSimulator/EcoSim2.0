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
from groups.group____fish import FishGroup
from groups.group____wolf import WolfGroup
from groups.group___bear import BearGroup
from groups.group___bees import BeesGroup
from groups.group___deer import DeerGroup
from groups.group___plant import PlantGroup


def sprite_test():
    pygame.init()

    world_map = widget___tiled_map.WorldMap("map2.tmx", (23, 23))

    world_map.render_entire_map()

    GRID_LOCK = threading.Lock()

    fish_group = FishGroup()
    bear_group = BearGroup()
    bees_group = BeesGroup()
    wolf_group = WolfGroup()
    deer_group = DeerGroup()
    plant_group = PlantGroup()

    s1 = PlantSprite(world_map, GRID_LOCK)
    s2 = DeerSprite(world_map, GRID_LOCK, (50, 50))
    s3 = WolfSprite(world_map, GRID_LOCK)

    s4 = BeesSprite(world_map, GRID_LOCK)
    s5 = FishSprite(world_map, GRID_LOCK)
    s6 = BearSprite(world_map, GRID_LOCK)

    # s1.update()
    # s2.update()
    # s3.update()
    # s4.update()
    # s5.update()
    # s6.update()
    sprites = AllSpritesGroup([fish_group, bear_group, bees_group, wolf_group, deer_group, plant_group], s1, s2, s3)
    sprites.add_to_correct_group(s4)
    sprites.add_to_correct_group(s5)
    sprites.add_to_correct_group(s6)

    fish_group.update()
    bear_group.update()
    bees_group.update()
    wolf_group.update()
    deer_group.update()
    plant_group.update()
    # sprites.update()


    done = False
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True

sprite_test()
