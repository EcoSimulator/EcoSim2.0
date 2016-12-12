import os
import pygame
from sprite___animal import AnimalSprite
from properties import sprites_dir
from health_bar import HealthBar


class PlantSprite(AnimalSprite):
    # Constants for the initial state of all PlantSprites
    IMAGE = pygame.image.load(os.path.join(sprites_dir, "plant.png"))
    HEALTH_BAR = HealthBar(100)
    AVG_SPEED = 0.2
    VISION = 4

    def __init__(self, world_map, GRID_LOCK, coordinates=None):
        """
        Create a PlantSprite object
        :param world_map: WorldMap Object
        :param coordinates: Array of coordinates [x,y]
        :param GRID_LOCK: Lock for screen (for threading)
        """

        ''' Take parameters, and Sprite Constants '''
        super(PlantSprite, self).__init__(world_map, PlantSprite.IMAGE, GRID_LOCK,
                                        PlantSprite.HEALTH_BAR, PlantSprite.AVG_SPEED,
                                        PlantSprite.VISION, coordinates)

        self.type = "plant"
        self.movable_terrain = world_map.get_all_land_tile_types()
        self.is_pollinated = False
        self.pollinate_timer = 0

    def spawn(self):
        """
        @Override
        :return:
        """
        AnimalSprite.spawn(self)
        self.tile.ignore_contents = True

    def move(self, target=None):
        """
        @Override
        Plants do not move, move changes plant pollination.
        :param target: meaningless to plants, just there to suppress warning
        :return: changes plant pollination on a timer right now
        """
        self.pollinate_timer += 1
        if self.pollinate_timer % 25 == 0:
            self.pollinate()
        self.tile.set_sprite(self)
        self.tile.ignore_contents = True
        self.display(self.tile)

    def pollinate(self):
        """
        Checks for pollination and either pollinates or de-pollinates accordingly
        """
        if not self.is_pollinated:
            self.image = pygame.image.load(os.path.join(sprites_dir, "plantpollinated.png"))
            self.is_pollinated = True
        elif self.is_pollinated:
            self.image = pygame.image.load(os.path.join(sprites_dir, "plant.png"))
            self.is_pollinated = False


def main():
    """
    Sprite Implementation Example
    """
    from widgets.widget___tiled_map import WorldMap
    import pygame
    import threading
    from threading import Thread
    pygame.init()

    # Map Setup
    screen = pygame.display.set_mode((800, 800))
    world_map = WorldMap("map2.tmx", (23, 23))
    world_map.render_entire_map()

    # Threading
    GRID_LOCK = threading.Lock()

    # Create Thread
    sprite = PlantSprite(world_map, GRID_LOCK)
    sprite.thread.start()


    # Loop until Pygame exits
    done = False
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True

if __name__ == '__main__':
    main()

