from enum import Enum
import pygame


from .commands import buildCommand


class HistoryType(Enum):
    CMD = pygame.Color("green")
    MSG = pygame.Color("red")


class HistoryObj:
    def __init__(self, txt: str, type: HistoryType) -> None:
        self.txt = txt
        self.type = type


class Console:
    borderWidth = 5
    textStart = ">> "
    fontColor = pygame.Color("green")
    consoleColor = pygame.Color("black")
    textMargin = 10
    fontSize = 15
    textHeight = fontSize + textMargin

    def __init__(self, game) -> None:
        super().__init__()
        self.game = game
        # command variables

        self.historySelect = 0

        #
        self.window_size = self.game.window_size
        self.surface = pygame.Surface(
            (
                self.game.SCREEN_MIN_WIDTH,
                int(self.game.SCREEN_MIN_HEIGHT * self.game.SCREEN_SPLIT),
            )
        )
        self.surface.fill(pygame.Color("green"))
        self.console_font = pygame.font.SysFont("lucidaconsole", self.fontSize)
        self.commandText = ""

    def getConsole(self):
        self.surface = pygame.transform.scale(
            self.surface,
            (
                self.window_size["w"],
                int(self.window_size["h"] * self.game.SCREEN_SPLIT),
            ),
        )
        input_box = self.inputBox()
        self.surface.blit(
            input_box,
            (0, (self.surface.get_height() - input_box.get_height())),
        )
        self.surface.blit(self.commandHistory(), (0, 0))
        return self.surface

    def keyPressEvent(self, event, readyCallback):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if self.commandText == "":
                    return
                command = buildCommand(self.commandText)
                self.addToHistory(self.commandText, HistoryType.CMD)
                readyCallback(command)
                self.historySelect = 0
                self.commandText = ""
            elif event.key == pygame.K_BACKSPACE:
                self.commandText = self.commandText[:-1]
            elif event.key == pygame.K_UP:
                if len(self.game.history) > self.historySelect:
                    self.historySelect += 1
                    if (
                        self.game.history[self.historySelect - 1].type
                        == HistoryType.CMD
                    ):
                        self.commandText = self.game.history[self.historySelect - 1].txt
            elif event.key == pygame.K_DOWN:
                if self.historySelect > 0:
                    self.historySelect -= 1
                    if (
                        self.game.history[self.historySelect - 1].type
                        == HistoryType.CMD
                    ):
                        self.commandText = self.game.history[self.historySelect - 1].txt
            else:
                self.commandText += event.unicode

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
        for i in range(len(self.game.history)):
            targetHeight = textListHeight - (self.fontSize * (i + 1))
            if targetHeight >= 0:
                textList.blit(
                    self.console_font.render(
                        self.textStart + str(self.game.history[i].txt),
                        True,
                        self.game.history[i].type.value,
                    ),
                    (0, targetHeight),
                )

        return textList

    def addToHistory(self, text: str, msgType: HistoryType):
        newHistoryObj = HistoryObj(text, msgType)
        self.game.history.appendleft(newHistoryObj)
        if len(self.game.history) > 10:
            self.game.history.pop()
