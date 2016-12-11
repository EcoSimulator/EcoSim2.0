from sprite import Sprite


class AnimalSprite(Sprite):

    def __init__(self, world_map, sprite_image, GRID_LOCK,
                 health_bar, speed, vision, coordinates=None):
        super(AnimalSprite, self).__init__(world_map, sprite_image, coordinates)

        self.health_bar = health_bar
        self.speed = speed
        self.vision = vision

    def decrease_health_bar(self, val):
        """
        Decreases the Sprite's health bar object, by a given value.
        Returns True, if the sprite is still alive,
                False, if the sprite becomes dead.
        :param val: Value to decrease the health by
        :return: True, if the sprite is still alive,
                 False, otherwise
        """
        still_alive = self.health_bar.decrease_health(val)
        # (maybe if dead here, immediately jump to deleting #

        return still_alive

    def increase_health_bar(self, val):
        """
        Increases the health of the health bar object by the
        specified value. It will not go over the max health.
        :param val: Value to increase health
        """
        self.health_bar.increase_health(val)


def main():
    """
    Sprite Implementation Example
    """
    from widgets.widget___tiled_map import WorldMap
    from properties import sprites_dir
    from health_bar import HealthBar
    import pygame
    import os, threading
    from threading import Thread
    pygame.init()

    # Map Setup
    screen = pygame.display.set_mode((800, 800))
    world_map = WorldMap("map2.tmx", (23, 23))
    world_map.render_entire_map()

    # Threading
    GRID_LOCK = threading.Lock()

    # Sprite Setup
    image_path = os.path.join(sprites_dir, "deer.png")
    image = pygame.image.load(image_path)

    # Create Healthbar
    health_bar = HealthBar(15)
    sprite = AnimalSprite(world_map, screen, image, (50, 50), GRID_LOCK,
                          health_bar, 5, 4)

    # Create Thread
    t = Thread(target=sprite.run)
    t.daemon = True

    # Run Sprite
    t.start()

    # Loop until Pygame exits
    done = False
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True

if __name__ == '__main__':
    main()



