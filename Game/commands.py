from enum import Enum

class Option:
    def __init__(self) -> None:
        self.option: str = None
        self.values: list = []

    def isOpt(self):
        return self.option is not None


class CommandType(Enum):
    NONE = 0
    PLAYER = 1


class Command:
    def __init__(self) -> None:
        self.argument: str = None
        self.options: list(Option) = []

    def isArg(self):
        return self.argument is not None


def buildCommand(cmdText):
    cmdText.lower()
    cmdText.strip()
    arguments = cmdText.split(" ")
    option = Option()
    command = Command()
    for i in range(len(arguments)):
        # first index is always the first argument
        if i == 0:
            command.argument = arguments[i]
        else:
            if arguments[i][0] == "-":
                # if there was already an option save and initialize that
                if option.isOpt():
                    command.options.append(option)
                    option = Option()
                # Start creating option object
                option.option = arguments[i]
            else:
                # add all values for the option
                if option.isOpt():
                    option.values.append(arguments[i])
    command.options.append(option)
    return command
