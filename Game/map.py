import pygame


class Map:
    def __init__(self, game) -> None:
        super().__init__()
        self.game = game
        self.window_size = self.game.window_size
        self.surface, self.location = self.getGameArea(
            (
                self.game.SCREEN_MIN_WIDTH,
                int(self.game.SCREEN_MIN_HEIGHT * (1.0 - self.game.SCREEN_SPLIT)),
            )
        )

    def getMap(self):
        self.surface, self.location = self.getGameArea(
            (
                self.window_size["w"],
                int(self.window_size["h"] * (1.0 - self.game.SCREEN_SPLIT)),
            )
        )
        return self.surface, self.location

    def getGameArea(self, size):
        w, h = size
        if w > h:
            areaSize = h
            x = (w - h) / 2
            y = 0
        else:
            x = 0
            y = (h - w) / 2
            areaSize = w
        newMapArea = pygame.Surface((areaSize, areaSize))
        newMapArea.fill(pygame.Color("white"))
        return newMapArea, (x, y)
