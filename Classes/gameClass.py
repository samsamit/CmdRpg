import pygame

from .consoleClass import Console
from .mapClass import Map


class Game:
    def __init__(self, min_w, min_h, screen_split):
        self.screen_split = screen_split
        self.window_min_h = min_h
        self.window_min_w = min_w
        self.window_h = min_h
        self.window_w = min_w
        self.window = pygame.display.set_mode(
            (self.window_min_h, self.window_min_w), pygame.RESIZABLE
        )
        self.width = 500
        self.height = 500
        self.clock = pygame.time.Clock()
        self.map = Map(screen_split, self.getWindowSize())
        self.console = Console(screen_split, self.getWindowSize())

    def redraw(self):
        pygame.display.update()
        self.window.fill((255, 255, 255))

        self.console.redreaw(self.getWindowSize())
        self.window.blit(self.map.container, (0, 0))
        self.window.blit(self.console.container, (0, self.console.start_h))

    def resize(self, w, h):
        self.window_h = self.window_min_h
        self.window_w = self.window_min_w
        # There's some code to add back window content here.
        if h > self.window_min_h:
            self.window_h = h
        if w > self.window_min_w:
            self.window_w = w
        self.window = pygame.display.set_mode(
            (self.window_w, self.window_h), pygame.RESIZABLE
        )

    def getWindowSize(self):
        return {"w": self.width, "h": self.height}
