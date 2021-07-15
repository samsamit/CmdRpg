from .characterClass import Character, Direction


class Commands:
    availableCommands = ["move", "turn"]
    adminCommands = ["m", "t"]
    targetIndex = 0
    commandIndex = 1

    def __init__(self, admin) -> None:
        self.__admin = admin
        self.target: Character = None
        self.action = None
        self.commandPieces = []
        self.characters = []

    def giveCharacters(self, characters):
        if len(self.characters) > 0:
            oldChars = self.characters
        else:
            oldChars = characters
        self.characters = characters
        return oldChars

    def monitor(self, commandLine):
        commandLine.strip()  # Removee whitespace from start and end
        commandLine.lower()  # make everything lowercase
        self.commandPieces = commandLine.split(" ")

        if self.__admin:
            self.handleAdmin()
        else:
            if len(self.commandPieces) >= 1:
                self.findTarget()
            if len(self.commandPieces) >= 2:
                self.findAction()

    def run(self):
        if len(self.commandPieces) >= 3:
            if self.action == "move":
                try:
                    self.target.startMove(int(self.commandPieces[2]))
                except ValueError:
                    print("move value not number")
                    self.target.steps = 0

            if self.action == "turn":
                try:
                    self.target.turn(Direction[self.commandPieces[2].upper()])
                except KeyError:
                    print(
                        "turn direction not correct: " + self.commandPieces[2].upper()
                    )
                    self.target.target__direction = self.target.direction
            self.target: Character = None
            self.action = None

    def findTarget(self):
        for character in self.characters:
            if character.data.name.lower() == self.commandPieces[0]:
                self.target = character
            else:
                self.target = None

    def findAction(self):
        if self.commandPieces[1] in self.availableCommands:
            self.action = self.commandPieces[1]
        else:
            self.action = None

    def handleAdmin(self):
        pcsLen = len(self.commandPieces)
        if pcsLen > 1:
            if self.commandPieces[0] in self.adminCommands:
                self.target = self.characters[0]
                if self.commandPieces[0] == "m":
                    self.action = "move"
                elif self.commandPieces[0] == "t":
                    self.action = "turn"
                else:
                    self.action = None
                self.commandPieces.append(self.commandPieces[1])
            else:
                self.findTarget()
