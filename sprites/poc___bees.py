from sprite import Sprite
import pygame
import vision
import os
from properties import *


class BeesSprite(Sprite):
    sprite_image = pygame.image.load(os.path.join(sprites_dir, "bees.png"))

    def __init__(self, world_map, GRID_LOCK, coordinates=None):
        Sprite.__init__(self, world_map, self.sprite_image, GRID_LOCK, coordinates)
        self.type = "bees"
        self.targets = ["plant"]

    def move(self, target=None):
        visible_tiles = vision.vision(15, self.world_map, self.tile)
        visible_tiles = filter(BeesSprite.pollinated_filter, visible_tiles)
        target_tile = vision.find_target(visible_tiles, self.targets)
        if target_tile:
            move_to_tile = vision.approach(self.tile, target_tile, self.world_map)
            if Sprite.is_movable_terrain(self, move_to_tile) and \
                    Sprite.not_contains_sprite(self, move_to_tile, self.targets):
                if move_to_tile == target_tile:
                    move_to_tile.contains_sprite.pollinate()
                Sprite.move(self, move_to_tile)
            else:
                Sprite.move(self)
        else:
            Sprite.move(self)

    @staticmethod
    def pollinated_filter(tile):
        current_sprite = tile.contains_sprite
        if current_sprite and current_sprite.type == "plant" and current_sprite.is_pollinated:
            return False
        else:
            return True
