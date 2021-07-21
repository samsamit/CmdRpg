import pygame
from Classes.windowClass import Window
from Classes.mapClass import Map
from Classes.consoleClass import Console
from Classes.characterClass import Character, CharacterData
from Assets.createAssets import TEST_CHARACTER
from Classes.commandsClass import Commands

# Constants
FPS = 60
SCREEN_SPLIT = 0.5
SCREEN_MIN_WIDTH = 500
SCREEN_MIN_HEIGHT = 500
ADMIN = True

# Varibles
window_size = {"w": SCREEN_MIN_WIDTH, "h": SCREEN_MIN_HEIGHT}
characters = []
mainCharacter = CharacterData("Jörgen")

pygame.init()
pygame.display.set_caption("CMD - RPG")
window = Window(
    SCREEN_MIN_WIDTH, SCREEN_MIN_HEIGHT, SCREEN_SPLIT, pygame.Color("white")
)
clock = pygame.time.Clock()

# inits
game_map = Map("grey")
console = Console("blue", 32, "black")
player = Character(50, 50, TEST_CHARACTER, mainCharacter)
characters.append(player)
commander = Commands(ADMIN)

# main loop
run = True
while run:
    clock.tick(FPS)

    # Handle window
    pygame.display.update()

    # Give characterss to classes
    game_map.giveCharacters(characters)
    characters = commander.giveCharacters(characters)

    # Update surfaces
    window.updateMap(game_map)
    window.updateConsole(console)

    # Debugging
    window.debuggerLine(characters[0].debugCharacter())

    # event handling, gets all event from the event queue
    for event in pygame.event.get():
        window.resize(event)
        console.keyEvent(event, commander)
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            run = False
