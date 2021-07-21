import pygame

from .utils import load_png


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png("TestChar.png")
        self.orgImage = self.image
        self.movepos = [0, 0]
        self.data = PlayerData()

    def update(self):
        self.rect = self.rect.move(self.movepos)


class PlayerData:
    size = 0.1
