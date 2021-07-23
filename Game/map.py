from Game.game import GameData
import pygame


class Map(GameData):
    def __init__(self) -> None:
        super().__init__()
        self.surface = pygame.Surface(
            (
                self.SCREEN_MIN_WIDTH,
                (self.SCREEN_MIN_HEIGHT * (1.0 - self.SCREEN_SPLIT)),
            )
        )
        self.surface.fill(pygame.Color("white"))
        self.mapArea = pygame.Surface((0, 0))
        self.mapArea.fill(pygame.Color("blue"))
        self.resizeGameArea(self.surface.get_size())
        self.window_size = {"w": self.SCREEN_MIN_WIDTH, "h": self.SCREEN_MIN_HEIGHT}

    def update(self, playerSprites):
        self.surface = pygame.Surface(
            (
                self.window_size["w"],
                int(self.window_size["h"] * (1.0 - self.SCREEN_SPLIT)),
            )
        )
        playerSprites.update()
        self.surface.fill(pygame.Color("white"))
        self.mapArea, mapAreaLocation = self.resizeGameArea(self.surface.get_size())
        playerSprites.draw(self.mapArea)
        self.surface.blit(self.mapArea, mapAreaLocation)

    def resize(self, window_size):
        self.window_size = window_size

    def resizeGameArea(self, size):
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
        newMapArea.fill(pygame.Color("blue"))
        return newMapArea, (x, y)
