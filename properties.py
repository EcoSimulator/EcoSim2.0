import pygame
import os

screen = pygame.display.set_mode((800, 800))

program_dir = os.path.dirname(os.path.realpath(__file__))

map_path = os.path.join(program_dir, "resources", "maps")

#map_path = 'resources/maps/'
tmx_ext = '.tmx'