import pygame

from widgets import widget___tiled_map
from widgets.widget___sidebar import SideBar
from widgets.widget___setup_sidebar import *
from widgets.widget___button import *
import threading
from properties import *
from widgets import widget___tiled_map
from threading import Thread
from sprites.sprite import Sprite
from sprites.sprite___deer import DeerSprite
from sprites.sprite___wolf import WolfSprite
from sprites.sprite____eagle import EagleSprite
from sprites.poc___plant import PlantSprite
from sprites.poc___bees import BeesSprite
from sprites.sprite___hare import HareSprite
from sprites.sprite___lynx import LynxSprite
from sprites.sprite___ticks import TickSprite
from sprites.poc___fish import FishSprite
from sprites.poc___bear import BearSprite
from groups.group___all_sprites import AllSpritesGroup
from groups.group____fish import FishGroup
from groups.group____wolf import WolfGroup
from groups.group___bear import BearGroup
from groups.group___bees import BeesGroup
from groups.group___deer import DeerGroup
from groups.group___plant import PlantGroup


# We'll need to pass a map param.
class SetupScreen:
    def __init__(self, map_name):
        self.world_map = widget___tiled_map.WorldMap(map_name + tmx_ext, (154, 0))
        self.sprites = None
        self.GRID_LOCK = threading.Lock()
        self.world_map.render_entire_map()

        self.create_sprite_groups()

        self.sb = SetupSideBar(self.world_map.heightPX, self.sprites, self.GRID_LOCK)
        self.sb.draw()

        self.run()

    def run(self):
        #self.sprites.thread.start()
        #self.sb.thread.start()

        done = False
        while not done:
            map = self.world_map
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if (map.loc_x < mouse[0] < map.widthPX and map.loc_y < mouse[1] < map.heightPX):
                if click[0] == 1:
                    self.place_sprite()
            self.sb.monitor_buttons()
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    quit()

    # Need to make this figure out which sprite you've selected.
    def place_sprite(self):
        map = self.world_map
        mouse = pygame.mouse.get_pos()
        # First, create the sprite itself.
        tile = self.world_map.get_tile_at_pixel(mouse)
        if tile.contains_sprite is None:
            sprite = WolfSprite(self.world_map, self.GRID_LOCK, (mouse[1], mouse[0] - 154)) #no clue why this is necessary, but coordinates are flipped or something.
            tile.set_sprite(sprite)
            self.wolf_group.add(sprite)
            sprite.spawn()

    def create_sprite_groups(self):
        self.fish_group = FishGroup()
        self.bear_group = BearGroup()
        self.bees_group = BeesGroup()
        self.wolf_group = WolfGroup()
        self.deer_group = DeerGroup()
        self.plant_group = PlantGroup()
        self.sprites = AllSpritesGroup([self.fish_group, self.bear_group, self.bees_group, self.wolf_group, self.deer_group, self.plant_group], self.GRID_LOCK)

    # temporary
    def start_new_map(self):
        GRID_LOCK = self.GRID_LOCK
        fish_group = FishGroup()
        bear_group = BearGroup()
        bees_group = BeesGroup()
        wolf_group = WolfGroup()
        deer_group = DeerGroup()
        plant_group = PlantGroup()

        s5 = WolfSprite(self.world_map, GRID_LOCK, (0, 0))
        s6 = WolfSprite(self.world_map, GRID_LOCK, (31, 31))
        s7 = WolfSprite(self.world_map, GRID_LOCK, (0, 31))
        s8 = WolfSprite(self.world_map, GRID_LOCK, (31, 0))

        s1 = DeerSprite(self.world_map, GRID_LOCK)
        s2 = DeerSprite(self.world_map, GRID_LOCK)
        s3 = DeerSprite(self.world_map, GRID_LOCK)
        s4 = DeerSprite(self.world_map, GRID_LOCK)

        s9 = BearSprite(self.world_map, GRID_LOCK)
        s10 = BearSprite(self.world_map, GRID_LOCK)

        s11 = FishSprite(self.world_map, GRID_LOCK)
        s12 = FishSprite(self.world_map, GRID_LOCK)
        s13 = FishSprite(self.world_map, GRID_LOCK)

        s14 = PlantSprite(self.world_map, GRID_LOCK)
        s15 = PlantSprite(self.world_map, GRID_LOCK)
        s16 = PlantSprite(self.world_map, GRID_LOCK)
        s17 = PlantSprite(self.world_map, GRID_LOCK)

        s18 = LynxSprite(self.world_map, GRID_LOCK)
        s19 = LynxSprite(self.world_map, GRID_LOCK)

        s20 = BeesSprite(self.world_map, GRID_LOCK)
        s21 = BeesSprite(self.world_map, GRID_LOCK)

        s22 = HareSprite(self.world_map, GRID_LOCK)
        s23 = HareSprite(self.world_map, GRID_LOCK)
        s24 = HareSprite(self.world_map, GRID_LOCK)

        s25 = TickSprite(self.world_map, GRID_LOCK)
        s26 = TickSprite(self.world_map, GRID_LOCK)

        self.sprites = AllSpritesGroup([fish_group, bear_group, bees_group, wolf_group, deer_group, plant_group],
                                       GRID_LOCK,
                                       s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17,
                                       s18, s19, s20, s21, s22, s23, s24, s25, s26)

        wolf_group.determine_pack_leader()
