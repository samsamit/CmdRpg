from .commands import Command
from collections import deque


class Commander:
    consoleCommads = ["clear"]

    def __init__(self, game) -> None:
        self.game = game
        pass

    def launchCommand(self, command: Command):
        arg = command.argument
        if arg == "clear" or arg == "c":
            return self.clearConsole()

        if arg == "test" or arg == "t":
            return self.toggleTestMode()

    # Console commands
    def clearConsole(self):
        self.game.history.clear()
        return

    def toggleTestMode(self):
        self.game.testMode = not self.game.testMode
        return f"Test mode is now {self.game.testMode}"
