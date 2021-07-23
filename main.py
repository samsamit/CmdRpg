import pygame
from Game.window import Window
from Game.console import Console
from Game.commander import Commander
from Game.map import Map
from Game.playerHandler import PlayerHandler
from Game.player import Player

gameOn = True
pygame.init()
pygame.display.set_caption("CMD - RPG")
clock = pygame.time.Clock()
console = Console()
gameMap = Map()
commander = Commander()
window = Window()
playerHandler = PlayerHandler()

testPlayer = Player()
playerHandler.addPlayer(testPlayer)

while gameOn:
    pygame.display.update()  # update display
    clock.tick(60)  # Set loop run cycle
    
    window.drawMap(gameMap.surface)  # Draw gameMap to display
    window.drawConsole(console.surface)  # Draw console to display
    playerHandler.resizePlayers(gameMap.mapArea.get_height())
    gameMap.update(playerHandler.getSpriteGroup())  # Draw players to game map
    # Handle player sprite resize
    
    for event in pygame.event.get():
        # Handle console and game map resize
        window.resize(event, console.resize, gameMap.resize)
        # Pass kay press events to console
        console.keyPressEvent(event, commander.handleCommand)
        if event.type == pygame.QUIT:
            gameOn = False
