import pygame
from .player import Player


class PlayerHandler:
    def __init__(self) -> None:
        self.players = []

    def addPlayer(self, newPlayer: Player):
        self.players.append(newPlayer)

    def getSpriteGroup(self):
        playerSprites = pygame.sprite.Group()
        for player in self.players:
            playerSprites.add(player)
        return playerSprites

    def resizePlayers(self, mapSize):
        for player in self.players:
            player.image = pygame.transform.scale(
                player.orgImage,
                (int(mapSize * player.data.size), int(mapSize * player.data.size)),
            )

    def testPlayerMovement(self):
        for player in self.players:
            player.movepos[0] += 1
