import pygame
from pygame.locals import *

from widgets import widget___info_display


def make_monitor(screen, itr, species):
    # We need a few different elements:
    # 1. White capsule to hold the sprite and population counter
    # 2. Population counter
    # 3. sprites
    # 4. Appropriate warning symbol

    monitor = []
    start_x = 12
    start_y = 14 + (itr*36)

    #warning symbol
    warning = pygame.image.load("resources/sidebar/warningoff.png")
    warning_rect = Rect((start_x+0, start_y+1), (27, 24))

    #button
    button = pygame.image.load("resources/sidebar/popbutton.png")
    button_rect = Rect((start_x+36, start_y+0), (90, 27))

    #sprite
    getSprite = ("resources/sprites/" + species + ".png")
    sprite = pygame.image.load(getSprite)
    sprite_rect = Rect((start_x+97, start_y+2), (24, 24))

    # make a button out of the capsule and its rectangle
    monitor.append((button, button_rect))
    # put the sprite on top of it
    monitor.append((sprite, sprite_rect))
    # put the warning symbol next to it
    monitor.append((warning, warning_rect))

    for tuple in monitor:
        screen.blit(tuple[0], tuple[1])
    pygame.display.flip()

    return monitor


def monitor_buttons(screen):
    species = ["wolf", "deer", "bees", "plant"]
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    dist = 36
    x1 = 12+36
    x2 = x1+90+36
    y1 = 14
    y2 = y1+27
    for item in species:
        if x2 > mouse[0] > x1 and y2 > mouse[1] > y1:
            if click[0] == 1:
                widget___info_display.display_info(screen, item)
        y1 += dist
        y2 += dist


def confirm(screen, species):
    sprite = pygame.image.load("resources/sprites/" +species+ ".png")
    sprite_rect = Rect((200, 200), (24, 24))
    screen.blit(sprite, sprite_rect)
    pygame.display.flip()


def update_population(screen, itr, species):
    font = pygame.font.SysFont("monospace", 22, True, False)
    population = str(len(species))

    # generate coordinates and render text
    num_x = 80
    num_y = (itr * 36) + 15
    label = font.render(population, 1, (0, 0, 0))

    # draw a white rectangle
    white = pygame.image.load("resources/sidebar/whiterect.png")
    white_rect = Rect((num_x - 30, num_y + 3), (60, 21))
    screen.blit(white, white_rect)
    # blit new text
    screen.blit(label, (num_x, num_y))
    pygame.display.flip()
