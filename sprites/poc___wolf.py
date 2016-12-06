from sprite import Sprite
import pygame
import vision


class WolfSprite(Sprite):
    sprite_image = pygame.image.load("resources/sprites/wolf.png")

    def __init__(self, world_map, screen, coordinates, GRID_LOCK, rect_size=None):
        Sprite.__init__(self, world_map, screen, self.sprite_image, coordinates, GRID_LOCK, rect_size)
        self.movable_terrain = world_map.get_all_land_tiles()

    def move(self):
        visible_tiles = vision.vision(2, self.world_map, self.tile)
        for tile in visible_tiles:
            if tile.contains_sprite is not None:
                print "I see something! " + " at " + str( tile.name) + str(tile.location_t) + \
                " from " + str(self.tile.name) + str(self.tile.location_t)
        Sprite.move(self)
