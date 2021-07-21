import pygame
from pygame.sndarray import array


class Window:
    def __init__(self, minWidth, minHeight, screenSplit, bgColor):
        self.screenSplit = screenSplit
        self.minWidth = minWidth
        self.minHeight = minHeight
        self.window_size = {"w": minWidth, "h": minHeight}
        self.window = pygame.display.set_mode((minWidth, minHeight), pygame.RESIZABLE)
        self.window.fill(bgColor)

    def resize(self, event):
        if event.type == pygame.VIDEORESIZE:
            if event.h > self.minHeight:
                self.window_size["h"] = event.h
            else:
                self.window_size["h"] = self.minHeight
            if event.w > self.minWidth:
                self.window_size["w"] = event.w
            else:
                self.window_size["w"] = self.minWidth
            window = pygame.display.set_mode(
                (self.window_size["w"], self.window_size["h"]), pygame.RESIZABLE
            )

    def updateMap(self, gameMap):
        self.window.blit(
            gameMap.surface(
                self.window_size["w"], self.window_size["h"] * self.screenSplit
            ),
            (0, 0),
        )

    def updateConsole(self, console):
        self.window.blit(
            console.surface(
                self.window_size["w"],
                (self.window_size["h"] - (self.window_size["h"] * self.screenSplit)),
            ),
            (0, (self.window_size["h"] * self.screenSplit)),
        )

    def debuggerLine(self, text):
        fontSize = 15
        debugFont = pygame.font.Font(None, fontSize)
        debugline = debugFont.render(text, True, pygame.Color("red"))
        self.window.blit(
            debugline, ((self.window_size["w"] - debugline.get_width()), 0)
        )
