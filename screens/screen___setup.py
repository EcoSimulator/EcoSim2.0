import pygame

from screen___game import GameScreen
from widgets import widget___tiled_map
from widgets.widget___sidebar import SideBar
from widgets.widget___setup_sidebar import *
from widgets.widget___button import *
import threading
from properties import *
from widgets import widget___tiled_map
from threading import Thread
from sprites.sprite import Sprite
from sprites.poc___bear import BearSprite
from sprites.poc___bees import BeesSprite
from sprites.sprite___deer import DeerSprite
from sprites.sprite____eagle import EagleSprite
from sprites.poc___fish import FishSprite
from sprites.sprite___hare import HareSprite
from sprites.sprite___lynx import LynxSprite
from sprites.poc___plant import PlantSprite
from sprites.sprite___ticks import TickSprite
from sprites.sprite___wolf import WolfSprite
from groups.group___all_sprites import AllSpritesGroup
from groups.group___bear import BearGroup
from groups.group___bees import BeesGroup
from groups.group___deer import DeerGroup
from groups.group____fish import FishGroup
from groups.group___plant import PlantGroup
from groups.group____wolf import WolfGroup


# We'll need to pass a map param.
class SetupScreen:
    def __init__(self, map_name):
        self.world_map = widget___tiled_map.WorldMap(map_name + tmx_ext, (154, 0))
        self.sprites = None
        self.sprites_list = []
        self.GRID_LOCK = threading.Lock()
        self.world_map.render_entire_map()

        self.create_sprite_groups()
        self.set_placement_mode("bear")

        self.sb = SetupSideBar(self.world_map.heightPX, self.sprites, self.GRID_LOCK, self.set_placement_mode, self.start_game)
        self.sb.draw()

        self.run()

    def run(self):
        #probably don't need these for setup.
        #self.sprites.thread.start()
        #self.sb.thread.start()

        self.done = False
        while not self.done:
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

    def set_placement_mode(self, species):
        acceptable_species = ["bear", "bees", "deer", "eagle", "hare", "lynx", "plant", "salmon", "fish", "ticks", "wolf"]
        if species in acceptable_species:
            self.placement_mode = species

    # Need to make this figure out which sprite you've selected.
    def place_sprite(self):
        mode = self.placement_mode
        map = self.world_map
        mouse = pygame.mouse.get_pos()
        # First, create the sprite itself.
        tile = self.world_map.get_tile_at_pixel(mouse)
        if tile.contains_sprite is None:
            #literally no better ideas than this right now.
            if mode == "bear":
                sprite = BearSprite(self.world_map, self.GRID_LOCK, (mouse[1], mouse[0] - 154)) #no clue why this is necessary, but coordinates are flipped or something.
                self.bear_group.add(sprite)
            if mode == "bees":
                sprite = BeesSprite(self.world_map, self.GRID_LOCK, (mouse[1], mouse[0] - 154))
                self.bees_group.add(sprite)
            if mode == "deer":
                sprite = DeerSprite(self.world_map, self.GRID_LOCK, (mouse[1], mouse[0] - 154))
                self.deer_group.add(sprite)
            if mode == "eagle":
                sprite = EagleSprite(self.world_map, self.GRID_LOCK, (mouse[1], mouse[0] - 154))
            if mode == "hare":
                sprite = HareSprite(self.world_map, self.GRID_LOCK, (mouse[1], mouse[0] - 154))
            if mode == "lynx":
                sprite = LynxSprite(self.world_map, self.GRID_LOCK, (mouse[1], mouse[0] - 154))
            if mode == "plant":
                sprite = PlantSprite(self.world_map, self.GRID_LOCK, (mouse[1], mouse[0] - 154))
                self.plant_group.add(sprite)
            if mode == "salmon" or mode == "fish":
                sprite = FishSprite(self.world_map, self.GRID_LOCK, (mouse[1], mouse[0] - 154))
                self.fish_group.add(sprite)
            if mode == "ticks":
                sprite = TickSprite(self.world_map, self.GRID_LOCK, (mouse[1], mouse[0] - 154))
            if mode == "wolf":
                sprite = WolfSprite(self.world_map, self.GRID_LOCK, (mouse[1], mouse[0] - 154))
                self.wolf_group.add(sprite)

            self.sprites_list.append(sprite)
            tile.set_sprite(sprite)
            sprite.spawn()

    def start_game(self):
        self.done = True
        new_groups = []
        #only pass in groups with sprites
        for group in self.group_list:
            if len(group) > 0:
                new_groups.append(group)
        game = GameScreen(self.world_map, new_groups, self.sprites_list, self.GRID_LOCK)

    def create_sprite_groups(self):
        self.fish_group = FishGroup()
        self.bear_group = BearGroup()
        self.bees_group = BeesGroup()
        self.wolf_group = WolfGroup()
        self.deer_group = DeerGroup()
        self.plant_group = PlantGroup()
        self.group_list = [self.fish_group, self.bear_group, self.bees_group, self.wolf_group, self.deer_group, self.plant_group]
        self.sprites = AllSpritesGroup([self.fish_group, self.bear_group, self.bees_group, self.wolf_group, self.deer_group, self.plant_group], self.GRID_LOCK)
