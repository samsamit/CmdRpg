import pygame


class Console:
    def __init__(self, color):
        self.color = color

    def surface(self, windowSize):
        container = pygame.Surface((windowSize["w"], windowSize["h"]))
        container.fill(pygame.Color(self.color))
        return container
