class Commander:
    def __init__(self) -> None:
        self.latestCommand = None
        pass

    def handleCommand(self, commandString):
        self.latestCommand = self.parseCommand(commandString)

    def parseCommand(self, commandString):
        commandString.strip()
        commandString.lower()
        commandPieces = commandString.split(" ")
        print(commandPieces)
        return commandPieces
