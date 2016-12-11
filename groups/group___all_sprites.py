import pygame


class AllSpritesGroup(pygame.sprite.Group):
    def __init__(self, subgroups, *sprites):
        self.subgroups = subgroups
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