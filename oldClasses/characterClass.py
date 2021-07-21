import pygame
from enum import Enum


class Character:
    def __init__(self, x, y, img, charData):
        self.__x = x
        self.__y = y
        self.sizeMultipler = charData.sizeMultipler
        self.steps = 0
        self.direction = Direction.UP
        self.degrees = 0
        self.target_degrees = 0
        self.orgImage = img
        self.__img = pygame.transform.scale(img, (50, 50))
        self.data = charData

    def updateCharSize(self, surface):
        if surface.get_height() > surface.get_width():
            newSize = int(surface.get_width() * self.sizeMultipler)
        else:
            newSize = int(surface.get_height() * self.sizeMultipler)
        self.__img = pygame.transform.scale(self.orgImage, (newSize, newSize))

    def draw(self, surface):
        self.updateCharSize(surface)
        self.handleMove()
        latestImg = self.handleTurn(self.__img)
        surface.blit(latestImg, (self.__x, self.__y))

    def turn(self, direction):
        if direction == Direction.LEFT:
            self.target_degrees = self.degrees + 45
        if direction == Direction.RIGHT:
            self.target_degrees = self.degrees - 45

    def startMove(self, distance):
        if self.steps == 0:
            self.steps = distance

    def handleMove(self):
        if self.steps > 0:
            if self.direction == Direction.UP:
                self.__y -= 1

            if self.direction == Direction.RIGHT_UP:
                self.__y -= 1
                self.__x += 1

            if self.direction == Direction.RIGHT:
                self.__x += 1

            if self.direction == Direction.RIGHT_DOWN:
                self.__y += 1
                self.__x += 1

            if self.direction == Direction.DOWN:
                self.__y += 1

            if self.direction == Direction.LEFT_UP:
                self.__y -= 1
                self.__x -= 1

            if self.direction == Direction.LEFT_DOWN:
                self.__y += 1
                self.__x -= 1

            if self.direction == Direction.LEFT:
                self.__x -= 1

            self.steps -= 1

    def handleTurn(self, img):
        modDegree = self.degrees % 360
        if self.degrees < 0:
            actDegree = modDegree * -1
        else:
            actDegree = modDegree
        if self.target_degrees > self.degrees:
            self.degrees += 1
        if self.target_degrees < self.degrees:
            self.degrees -= 1

        if self.target_degrees == self.degrees:
            try:
                if self.direction != Direction(modDegree):
                    self.direction = Direction(modDegree)
                    print(
                        f"degree: {self.degrees}, actDeg: {actDegree}, modDeg: {modDegree}, Direction: {self.direction.name}"
                    )
            except Exception:
                pass

        orig_rect = img.get_rect()
        rot_img = pygame.transform.rotate(img, self.degrees)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_img.get_rect().center
        rot_img = rot_img.subsurface(rot_rect).copy()
        return rot_img

    def debugCharacter(self):
        return f"Dir:{self.direction.name}, Deg:{self.degrees}/{self.target_degrees}"


class CharacterData:
    def __init__(self, name) -> None:
        self.name = name
        self.sizeMultipler = 0.1


class Direction(Enum):
    UP = 0
    RIGHT_UP = 315
    RIGHT = 270
    RIGHT_DOWN = 225
    DOWN = 180
    LEFT_DOWN = 135
    LEFT = 90
    LEFT_UP = 45
