import pygame
import TiledMap
from Sprite import SpritePOC

def sprite_test():
    pygame.init()

    screen = pygame.display.set_mode((800, 800))

    world_map = TiledMap.WorldMap("Map2")

    world_map.render_entire_map()

    sprite = SpritePOC.Sprite(world_map)
    s2 = SpritePOC.Sprite(world_map)

    sprite.spawn(screen)
    s2.spawn(screen)
    pygame.display.update()

    while True:
        pygame.time.delay(1000)
        sprite.move(world_map, screen)
        s2.move(world_map, screen)
        pygame.display.update()

sprite_test()