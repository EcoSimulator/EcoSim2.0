import pygame
import os

screen = pygame.display.set_mode((800, 800))

program_dir = os.path.dirname(os.path.realpath(__file__))

resources_dir = os.path.join(program_dir, "resources")

buttons_dir = os.path.join(resources_dir, "buttons")

infoscreen_dir = os.path.join(resources_dir, "infoscreen")

map_dir = os.path.join(resources_dir, "maps")

sidebar_dir = os.path.join(resources_dir, "sidebar")

sprites_dir = os.path.join(resources_dir, "sprites")

tiles_dir = os.path.join(resources_dir, "tiles")

png_ext = '.png'

tmx_ext = '.tmx'