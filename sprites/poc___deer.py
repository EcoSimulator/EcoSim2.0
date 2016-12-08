from sprite import Sprite
import pygame
import vision
from properties import *


class DeerSprite(Sprite):
    sprite_image = pygame.image.load(os.path.join(sprites_dir, "deer.png"))

    def __init__(self, world_map, GRID_LOCK, coordinates=None):
        Sprite.__init__(self, world_map, self.sprite_image, GRID_LOCK, coordinates)
        self.type = "deer"
        self.movable_terrain = world_map.get_all_land_tile_types()
        self.targets = ["wolf"]

    def move(self, target=None):
        visible_tiles = vision.vision(4, self.world_map, self.tile)
        target_tile = vision.find_target(visible_tiles, self.targets)
        if target_tile:
            move_to_tile = vision.flee(self.tile, target_tile, self.world_map)
            if Sprite.is_movable_terrain(self, move_to_tile) and Sprite.not_contains_sprite(self, move_to_tile):
                Sprite.move(self, move_to_tile)
            else:
                Sprite.move(self)
        else:
            Sprite.move(self)
