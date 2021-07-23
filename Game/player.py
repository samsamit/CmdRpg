import pygame
from .utils import load_png


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png("TestChar.png")
        self.orgImage = self.image
        self.targetDirection: Direction = None
        self.steps = 0
        self.currentRotation = 0
        self.targetRotation = 180
        self.data = PlayerData()
        self.mapSize = 0

    def update(self):
        self.move()

        self.image = pygame.transform.scale(
            self.orgImage,
            (int(self.mapSize * self.data.size), int(self.mapSize * self.data.size)),
        )
        self.image, self.rect = self.rotate()

    def move(self):
        # handle movement
        if self.targetDirection is not None and self.steps > 0:
            self.rect = self.rect.move(self.targetDirection["move"])
            self.steps -= 1

    def rotate(self):
        if self.currentRotation != self.targetRotation:
            if self.targetRotation > self.currentRotation:
                self.currentRotation += 30
            else:
                self.currentRotation -= 30

        orig_rect = self.image.get_rect()
        rot_img = pygame.transform.rotate(self.image, self.currentRotation)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_img.get_rect().center
        rot_img = rot_img.subsurface(rot_rect).copy()
        return rot_img, rot_rect


class PlayerData:
    size = 0.1


class Direction:
    n = [0, -1]
    ne = [1, -1]
    e = [1, 0]
    se = [1, 1]
    s = [0, 1]
    sw = [-1, 1]
    w = [-1, 0]
    nw = [-1, -1]
