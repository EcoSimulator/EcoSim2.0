import pygame
import threading
#from sprites import sprite___poc
from widgets import widget___tiled_map
from threading import Thread
from sprites.sprite___poc import Sprite

def sprite_test():
    pygame.init()

    screen = pygame.display.set_mode((800, 800))

    world_map = widget___tiled_map.WorldMap("map2.tmx", (23, 23))

    world_map.render_entire_map()

    GRID_LOCK = threading.Lock()

    sprite = Sprite(world_map, screen)
    s2 = Sprite(world_map, screen)
    s3 = Sprite(world_map, screen)
    s4 = Sprite(world_map, screen)

    sprite.spawn(screen)
    s2.spawn(screen)
    s3.spawn(screen)
    s4.spawn(screen)
    pygame.display.update()

    one = Thread(target=sprite.move_octopus)
    one.daemon = True

    two = Thread(target=s2.move_octopus)
    two.daemon = True

    three = Thread(target=s3.move_octopus)
    three.daemon = True

    four = Thread(target=s4.move_octopus)
    four.daemon = True

    one.start()
    two.start()
    three.start()
    four.start()
    while True:
        pass
    #     pygame.time.delay(1000)
    #     sprite.move(world_map, screen)
    #     s2.move(world_map, screen)
    #     pygame.display.update()

sprite_test()
