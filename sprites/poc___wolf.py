from sprite import Sprite
import pygame
import vision


class WolfSprite(Sprite):
    sprite_image = pygame.image.load("resources/sprites/wolf.png")

    def __init__(self, world_map, screen, coordinates, GRID_LOCK, rect_size=None):
        Sprite.__init__(self, world_map, screen, self.sprite_image, coordinates, GRID_LOCK, rect_size)
        self.movable_terrain = world_map.get_all_land_tiles()

    def move(self):
        visible_tiles = vision.vision(4, self.world_map, self.tile)
        target_tile = vision.find_target(visible_tiles)
        if target_tile:
            move_to_tile = vision.approach(self.tile, target_tile, self.world_map)
            Sprite.move(self, move_to_tile)
        else:
            Sprite.move(self)
