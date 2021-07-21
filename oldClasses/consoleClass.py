import pygame
from collections import deque

from .commandsClass import Commands


class Console:
    textStart = "#//>"
    commandToRun = None

    def __init__(self, color, fontSize, fontColor):
        self.fontColor = fontColor
        self.color = color
        self.font = pygame.font.Font(None, fontSize)
        self.inputHeight = self.font.get_height() + 5
        self.commandText = ""
        self.history = deque([])
        self.historySelect = 0

    def surface(self, w, h):
        container = pygame.Surface((w, h))
        container.blit(self.getTextList(w, h), (0, 0)),
        container.blit(self.getInputBox(w), (0, h - self.inputHeight))
        return container

    def keyEvent(self, event, commander):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.addToHistory(self.commandText)
                self.historySelect = 0
                commander.run()
                if self.commandText == "clear":
                    self.history = deque([])
                self.commandText = ""
            elif event.key == pygame.K_BACKSPACE:
                self.commandText = self.commandText[:-1]
            elif event.key == pygame.K_UP:
                if len(self.history) >= self.historySelect:
                    self.historySelect += 1
                    self.commandText = self.history[self.historySelect - 1]
                    commander.monitor(self.commandText)
            elif event.key == pygame.K_DOWN:
                if self.historySelect > 0:
                    self.historySelect -= 1
                    self.commandText = self.history[self.historySelect - 1]
                    commander.monitor(self.commandText)
            else:
                self.commandText += event.unicode
                commander.monitor(self.commandText)

    def getTextList(self, w, h):
        height = h - self.inputHeight
        textList = pygame.Surface((w, height))
        textList.fill(pygame.Color("green"))
        for i in range(len(self.history)):
            targetHeight = height - (self.inputHeight * (i + 1))
            if targetHeight >= 0:
                textList.blit(
                    self.font.render(
                        self.textStart + self.history[i], True, self.fontColor
                    ),
                    (0, targetHeight),
                )

        return textList

    def getInputBox(self, w):
        input_box = pygame.Surface((w, self.inputHeight))
        input_box.fill(pygame.Color("red"))
        input_box.blit(
            self.font.render(self.textStart + self.commandText, True, self.fontColor),
            (0, 0),
        )
        return input_box

    def addToHistory(self, text):
        self.history.appendleft(text)
        if len(self.history) > 10:
            self.history.pop()
