from collections import deque
import pygame
from Game.game import GameData


class Console(GameData):
    borderWidth = 5
    textStart = ">> "
    fontColor = pygame.Color("green")
    consoleColor = pygame.Color("black")
    textMargin = 10
    fontSize = 15
    textHeight = fontSize + textMargin

    def __init__(self) -> None:
        super().__init__()
        # command variables
        self.history = deque([])
        self.historySelect = 0

        #
        self.window_size = {"w": self.SCREEN_MIN_WIDTH, "h": self.SCREEN_MIN_HEIGHT}
        self.surface = pygame.Surface(
            (self.SCREEN_MIN_WIDTH, int(self.SCREEN_MIN_HEIGHT * self.SCREEN_SPLIT))
        )
        self.surface.fill(pygame.Color("green"))
        self.console_font = pygame.font.SysFont("lucidaconsole", self.fontSize)
        self.commandText = ""
        self.update()

    def resize(self, window_size):
        self.window_size = window_size
        self.update()

    def update(self):
        self.surface = pygame.transform.scale(
            self.surface,
            (self.window_size["w"], int(self.window_size["h"] * self.SCREEN_SPLIT)),
        )
        input_box = self.inputBox()
        self.surface.blit(
            input_box,
            (0, (self.surface.get_height() - input_box.get_height())),
        )
        self.surface.blit(self.commandHistory(), (0, 0))

    def keyPressEvent(self, event, readyCallback):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                readyCallback(self.commandText)
                self.addToHistory(self.commandText)
                self.historySelect = 0
                if self.commandText == "clear":
                    self.history = deque([])
                self.commandText = ""
            elif event.key == pygame.K_BACKSPACE:
                self.commandText = self.commandText[:-1]
            elif event.key == pygame.K_UP:
                if len(self.history) > self.historySelect:
                    self.historySelect += 1
                    self.commandText = self.history[self.historySelect - 1]
            elif event.key == pygame.K_DOWN:
                if self.historySelect > 0:
                    self.historySelect -= 1
                    self.commandText = self.history[self.historySelect - 1]
            else:
                self.commandText += event.unicode
            self.update()

    def inputBox(self):
        input_box = pygame.Surface((self.window_size["w"], self.textHeight))
        input_box.fill(self.consoleColor)
        input_box.blit(
            self.console_font.render(
                self.textStart + self.commandText, True, self.fontColor
            ),
            (0, (self.textMargin / 2)),
        )
        return input_box

    def commandHistory(self):
        textListHeight = self.surface.get_height() - self.textHeight
        textList = pygame.Surface((self.window_size["w"], textListHeight))
        textList.fill(self.consoleColor)
        for i in range(len(self.history)):
            targetHeight = textListHeight - (self.fontSize * (i + 1))
            if targetHeight >= 0:
                textList.blit(
                    self.console_font.render(
                        self.textStart + self.history[i], True, self.fontColor
                    ),
                    (0, targetHeight),
                )

        return textList

    def addToHistory(self, text):
        self.history.appendleft(text)
        if len(self.history) > 10:
            self.history.pop()
