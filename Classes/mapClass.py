import pygame

from .characterClass import Character


class Map:
    def __init__(self, color):
        self.characters: list[Character] = []
        self.color = color

    def giveCharacters(self, characters):
        self.characters = characters

    def surface(self, windowSize):
        self.container = pygame.Surface((windowSize["w"], windowSize["h"]))
        self.container.fill(pygame.Color(self.color))
        self.drawCharacters()
        return self.container

    def drawCharacters(self):
        for i in range(len(self.characters)):
            self.characters[i].draw(self.container)
