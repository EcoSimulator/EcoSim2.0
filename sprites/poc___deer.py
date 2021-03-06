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
        self.predators = ["wolf"]
        self.prey = ["plant"]

    def move(self, target=None):
        visible_tiles = vision.vision(4, self.world_map, self.tile)
        flight_tile = vision.find_target(visible_tiles, self.predators)
        target_tile = vision.find_target(visible_tiles, self.prey)
        if flight_tile:
            move_to_tile = vision.flee(self.tile, flight_tile, self.world_map)
            if Sprite.is_movable_terrain(self, move_to_tile) and self.not_contains_sprite(move_to_tile):
                Sprite.move(self, move_to_tile)
            else:
                Sprite.move(self)
        elif target_tile:
            move_to_tile = vision.approach(self.tile, target_tile, self.world_map)
            if Sprite.is_movable_terrain(self, move_to_tile) and Sprite.not_contains_sprite(self, move_to_tile,
                                                                                            self.prey):
                if move_to_tile == target_tile:
                    move_to_tile.contains_sprite.die()
                Sprite.move(self, move_to_tile)
            else:
                Sprite.move(self)
        else:
            Sprite.move(self)
