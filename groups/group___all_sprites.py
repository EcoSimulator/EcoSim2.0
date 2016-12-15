import pygame
from threading import Thread


class AllSpritesGroup(pygame.sprite.Group):
    def __init__(self, subgroups, GRID_LOCK, *sprites):
        self.subgroups = subgroups
        self.GRID_LOCK = GRID_LOCK
        self.thread = Thread(target=self.run)
        self.thread.daemon = True
        self.is_alive = True
        self.paused = False

        for sprite in sprites:
            for group in subgroups:
                if sprite.type == group.type:
                    group.add(sprite)
        pygame.sprite.Group.__init__(self, sprites)

    def add_to_correct_group(self, sprite):
        for group in self.subgroups:
            if sprite.type == group.type:
                group.add(sprite)
        pygame.sprite.Group.add(self, sprite)

    def remove(self, sprite):
        pygame.sprite.Group.remove(self, sprite)

    def get_subgroups(self):
        return self.subgroups

    def run(self):
        pygame.sprite.Group.update(self)

    def pause(self):
        self.paused = True
        while self.paused:
            pass

    def unpause(self):
        self.paused = False
