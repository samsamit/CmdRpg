import pygame


class Character:
    width, height = 50, 50

    def __init__(self, x, y, img):
        self.__x = x
        self.__y = y
        self.__img = pygame.transform.scale(img, (self.width, self.height))

    def draw(self, surface):
        surface.blit(self.__img, (self.__x, self.__y))
