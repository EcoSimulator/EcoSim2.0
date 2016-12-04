import pygame
import os

screen = pygame.display.set_mode((800, 800))

program_dir = os.path.dirname(os.path.realpath(__file__))

resources_dir = os.path.join(program_dir, "resources")

map_dir = os.path.join(resources_dir, "maps")

tiles_dir = os.path.join(resources_dir, "tiles")

tmx_ext = '.tmx'