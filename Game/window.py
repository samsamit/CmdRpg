import pygame
from .game import GameData
from .console import Console
from .map import Map


class Window(GameData):
    def __init__(self) -> None:
        super().__init__()
        self.window_size = {"w": self.SCREEN_MIN_WIDTH, "h": self.SCREEN_MIN_HEIGHT}
        self.window = pygame.display.set_mode(
            (self.SCREEN_MIN_WIDTH, self.SCREEN_MIN_HEIGHT), pygame.RESIZABLE
        )

    def resize(self, event, consoleResize, mapResize):
        if event.type == pygame.VIDEORESIZE:
            if event.h > self.SCREEN_MIN_HEIGHT:
                self.window_size["h"] = event.h
            else:
                self.window_size["h"] = self.SCREEN_MIN_HEIGHT
            if event.w > self.SCREEN_MIN_WIDTH:
                self.window_size["w"] = event.w
            else:
                self.window_size["w"] = self.SCREEN_MIN_WIDTH
            self.window = pygame.display.set_mode(
                (self.window_size["w"], self.window_size["h"]), pygame.RESIZABLE
            )
            consoleResize(self.window_size)
            mapResize(self.window_size)

    def drawConsole(self, consoleSurface):
        self.window.blit(
            consoleSurface, (0, self.window_size["h"] * (1.0 - self.SCREEN_SPLIT))
        )

    def drawMap(self, mapSurface):
        self.window.blit(mapSurface, (0, 0))
