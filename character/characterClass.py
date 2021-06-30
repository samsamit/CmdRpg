import pygame


class Character:
    def __init__(self, x, y, img):
        self.__x = x
        self.__y = y
        self.__img = img

    def draw(self, window):
        pygame.draw.rect(window, self.__img, (self.__x, self.__y, 50, 50))
