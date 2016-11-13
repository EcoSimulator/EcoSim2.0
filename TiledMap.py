import xml.etree.ElementTree as ElementTree
import pygame.image as pyg_image
from properties import *


class TileType:
    height = 30
    width = 30

    def __init__(self, name, gid):
        self.name = name
        self.gid = int(gid)
        self.loc = "Tiles/" + name + ".png"
        self.image = pyg_image.load(self.loc)

    def __init2__(self, tile):
        self.name = tile.name
        self.gid = tile.gid
        self.loc = tile.loc
        self.image = tile.image


class TileInstance(TileType):
    def __init__(self, tile):
        TileType.__init2__(self, tile)
        self.tile = tile
        self.name = tile.name
        self.gid = tile.gid
        self.loc = tile.loc
        self.image = tile.image
        self.location = None

    def tile_print(self):
        print self.name + ' @ ' + str(self.location)

    def set_location(self, (x, y)):
        self.location = (x, y)


class WorldMap(pygame.Surface):

    def __init__(self, file_name):
        self.screen = screen
        self.file_name = map_path + file_name + tmx_ext
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

    def render_entire_map(self):
        x = 0
        y = 0
        for line in self.tiles:
            for tile in line:
                if tile is not None:
                    self.screen.blit(tile.image, (x * TileType.width, y * TileType.height))
                    tile.set_location((x * TileType.height, y * TileType.width))
                    x += 1
            x = 0
            y += 1
        pygame.display.update()

    def get_surrounding_movable_tiles(self, tile):
        y = tile.location[0] / 30
        x = tile.location[1] / 30
        adjacent = [self.__get_tile_by_index((x, (y + 1))),
                    self.__get_tile_by_index((x, (y - 1))),
                    self.__get_tile_by_index(((x + 1), y)),
                    self.__get_tile_by_index(((x - 1), y))]
        adjacent = filter(None, adjacent)
        return adjacent

    def __get_tile_by_index(self, (x, y)):
        if 0 < x < self.height_t and 0 < y < self.width_t:
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
