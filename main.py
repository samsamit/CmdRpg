import pygame
from Classes.mapClass import Map
from Classes.consoleClass import Console
from Classes.characterClass import Character
from Assets.createAssets import TEST_CHARACTER

# Constants
FPS = 60
SCREEN_SPLIT = 0.5
SCREEN_MIN_WIDTH = 500
SCREEN_MIN_HEIGHT = 500

# Varibles
window_size = {"w": SCREEN_MIN_WIDTH, "h": SCREEN_MIN_HEIGHT}
characters = []

pygame.init()
pygame.display.set_caption("CMD - RPG")
window = pygame.display.set_mode(
    (SCREEN_MIN_HEIGHT, SCREEN_MIN_WIDTH), pygame.RESIZABLE
)
clock = pygame.time.Clock()

# inits
game_map = Map("red")
console = Console("blue")
player = Character(50, 50, TEST_CHARACTER)
characters.append(player)

# Functions

# main loop
run = True
while run:
    clock.tick(FPS)

    # Update window
    pygame.display.update()
    window.fill((255, 255, 255))

    game_map.giveCharacters(characters)

    # Update surfaces
    window.blit(game_map.surface(window_size), (0, 0))
    window.blit(console.surface(window_size), (0, (window_size["h"] * SCREEN_SPLIT)))

    # event handling, gets all event from the event queue
    for event in pygame.event.get():
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            run = False

        if event.type == pygame.VIDEORESIZE:
            if event.h > SCREEN_MIN_HEIGHT:
                window_size["h"] = event.h
            else:
                window_size["h"] = SCREEN_MIN_HEIGHT
            if event.w > SCREEN_MIN_WIDTH:
                window_size["w"] = event.w
            else:
                window_size["w"] = SCREEN_MIN_WIDTH
            window = pygame.display.set_mode(
                (window_size["w"], window_size["h"]), pygame.RESIZABLE
            )
