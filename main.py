import pygame
from characterClass import Character
from createAssets import TEST_CHARACTER

# from createAssets import *
from config import WIN_HEIGHT, WIN_WIDTH, FPS

pygame.init()
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("CMD - RPG")

clock = pygame.time.Clock()

# define a variable to control the main loop
run = True
char = Character(50, 50, TEST_CHARACTER)


def redraw_window():
    pygame.display.update()
    char.draw(window)


# main loop
while run:
    clock.tick(FPS)
    redraw_window()
    # event handling, gets all event from the event queue
    for event in pygame.event.get():
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            run = False
