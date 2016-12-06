from sprite import Sprite
import pygame


class DeerSprite(Sprite):
    sprite_image = pygame.image.load("resources/sprites/deer.png")

    def __init__(self, world_map, screen, coordinates, GRID_LOCK, rect_size=None):
        Sprite.__init__(self, world_map, screen, self.sprite_image, coordinates, GRID_LOCK, rect_size)
        self.movable_terrain = world_map.get_all_land_tiles()
