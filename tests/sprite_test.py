import pygame

from sprites import sprite___poc
from widgets import widget___tiled_map


def sprite_test():
    pygame.init()

    screen = pygame.display.set_mode((800, 800))

    world_map = widget___tiled_map.WorldMap("map2", (23, 23))

    world_map.render_entire_map()

    sprite = sprite___poc.Sprite(world_map)
    s2 = sprite___poc.Sprite(world_map)

    sprite.spawn(screen)
    s2.spawn(screen)
    pygame.display.update()

    while True:
        pygame.time.delay(1000)
        sprite.move(world_map, screen)
        s2.move(world_map, screen)
        pygame.display.update()
        #pygame.event.pump()

sprite_test()