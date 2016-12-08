import xml.etree.ElementTree as ElementTree
import pygame.image as pyg_image
import os
from properties import *


class TileType:
    """
    Class representing a type of a tile.
    """
    height = 30
    width = 30

    def __init__(self, name, gid):
        """
        :param name: file name
        :param gid: gid from the tmx file
        """
        self.name = name
        self.gid = int(gid)
        self.loc = os.path.join(tiles_dir, name + ".png")
        self.image = pyg_image.load(self.loc)


class TileInstance(TileType):
    """
    An instance of a tile.
    Includes a tile type and a location
    """
    def __init__(self, tile_type):
        """
        :param tile_type: The tile type
        """
        self.tile_type = tile_type
        self.name = tile_type.name
        self.gid = tile_type.gid
        self.loc = tile_type.loc
        self.image = tile_type.image
        self.locationPX = None
        self.location_t = None
        self.contains_sprite = None
        self.ignore_contents = False

    def tile_print(self):
        """
        :return: prints a tiles name and location
        """
        if self.contains_sprite:
            print self.name + ' @ ' + str(self.locationPX) + " with " + self.contains_sprite.type
        else:
            print self.name + ' @ ' + str(self.locationPX)

    def set_location(self, (x, y)):
        """
        :param (x, y): the location to set
        :return: sets the location of the tile
        """
        self.locationPX = (x, y)
        self.location_t = (x/30, y/30)

    def set_sprite(self, sprite):
        self.contains_sprite = sprite


class WorldMap(pygame.Surface):

    def __init__(self, file_name, (loc_x, loc_y)):
        """
        :param file_name: the name of the tmx map
        :param (loc_x, loc_y): the placement of the top left corner of the map
        """
        self.screen = screen
        self.file_name = os.path.join(map_dir, file_name)
        xml_file = ElementTree.parse(self.file_name)
        self.root = xml_file.getroot()
        self.tile_types = self.__create_tile_list()
        layer = self.root.find("layer")
        self.name = layer.attrib['name']
        self.width_t = int(layer.attrib['width'])
        self.height_t = int(layer.attrib['height'])
        self.widthPX = self.width_t * TileType.width
        self.heightPX = self.height_t * TileType.height
        numbers = layer.find("data").text
        self.tiles = self.__make_tile_matrix(numbers)
        self.loc_x = loc_x
        self.loc_y = loc_y

    def render_entire_map(self):
        """
        :return: renders the entire map to the screen
        """
        x = 0
        y = 0
        for line in self.tiles:
            for tile in line:
                if tile is not None:
                    self.screen.blit(tile.image, (x * TileType.width + self.loc_x, y * TileType.height + self.loc_y))
                    tile.set_location((x * TileType.width + self.loc_x, y * TileType.height + self.loc_y))
                    x += 1
            x = 0
            y += 1
        pygame.display.update()

    def get_surrounding_movable_tiles(self, tile):
        """
        :param tile: the tile a sprite is actually on
        :return: a list of movable tiles that the sprite could move to
        """
        y = tile.locationPX[0] / 30
        x = tile.locationPX[1] / 30
        adjacent = [self.get_tile_by_index((x, (y + 1))),
                    self.get_tile_by_index((x, (y - 1))),
                    self.get_tile_by_index(((x + 1), y)),
                    self.get_tile_by_index(((x - 1), y))]
        adjacent = filter(None, adjacent)
        return adjacent

    def get_tile_by_index(self, (x, y)):
        if 0 <= x < self.height_t and 0 <= y < self.width_t:
            return self.tiles[x][y]
        else:
            return None

    def get_tile_at_pixel(self, (x, y)):
        return self.tiles[x/30][y/30]

    def set_tile(self, (x, y), tile_rep):
        self.tiles[x/30][y/30] = tile_rep

    def get_tile_by_gid(self, gid):
        for tile in self.tile_types:
            if gid != '' and tile.gid == int(gid):
                return tile
        else:
            "Error, tile with gid: " + gid + " not found!"

    def __create_tile_list(self):
        """
        :return: the list of tile types
        """
        temp_tiles = []

        for entry in self.root.findall("tileset"):
            attrib = entry.attrib
            if attrib['name'].startswith('grass'):
                grass_tile = TileType(attrib['name'], attrib['firstgid'])
                temp_tiles.insert(grass_tile.gid, grass_tile)
            elif attrib['name'].startswith('soil'):
                soil_tile = TileType(attrib['name'], attrib['firstgid'])
                temp_tiles.insert(soil_tile.gid, soil_tile)
            elif attrib['name'].startswith('veg'):
                veg_tile = TileType(attrib['name'], attrib['firstgid'])
                temp_tiles.insert(veg_tile.gid, veg_tile)
            elif attrib['name'].startswith('water'):
                water_tile = TileType(attrib['name'], attrib['firstgid'])
                temp_tiles.insert(water_tile.gid, water_tile)
        return temp_tiles

    def get_tile_type(self, tile_name):
        for tile in self.tile_types:
            if tile.name.startswith(tile_name):
                return tile

    def get_all_land_tile_types(self):
        """
        :return: returns a list of the land tile types
        """
        land_tiles = []
        land_tile_names = ["grass", "veg", "soil"]
        for tile in self.tile_types:
            for name in land_tile_names:
                if tile.name.startswith(name):
                    land_tiles.append(tile)
                    break
        return land_tiles

    def get_all_water_tile_types(self):
        """
        :return: a list of the water tile types
        """
        water_tiles = []
        water_tile_names = ["water"]
        for tile in self.tile_types:
            for name in water_tile_names:
                if tile.name.startswith(name):
                    water_tiles.append(tile)
                    break
        return water_tiles

    def get_all_tiles_of_types(self, types):
        all_tiles_of_types = []
        for row in self.tiles:
            for tile in row:
                for tile_type in types:
                    if tile.tile_type == tile_type:
                        all_tiles_of_types.append(tile)
        return all_tiles_of_types

    def __make_tile_matrix(self, num_matrix):
        matrix = num_matrix.split("\n")
        for line in matrix:
            matrix[matrix.index(line)] = line.split(",")
        for line in matrix:
            for item in line:
                if item is not '':
                    line[line.index(item)] = TileInstance(self.get_tile_by_gid(item))
                else:
                    line.remove(item)
        matrix.remove([])
        matrix.remove([])
        return matrix
