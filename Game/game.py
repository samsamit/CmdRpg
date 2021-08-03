import pygame as pg
from os import path
import sys

from .map import Map

from .player import Player


class Game:
    FPS = 60
    ADMIN = True
    SCREEN_MIN_WIDTH = 500
    SCREEN_MIN_HEIGHT = 500
    SCREEN_SPLIT = 0.3
    TITLE = "CMD_RPG"
    BGCOLOR = pg.Color("grey")

    def __init__(self) -> None:
        pg.init()
        self.window_size = {"w": self.SCREEN_MIN_WIDTH, "h": self.SCREEN_MIN_HEIGHT}
        self.map_size = (0, 0)
        self.screen = pg.display.set_mode(
            (self.SCREEN_MIN_WIDTH, self.SCREEN_MIN_HEIGHT), pg.RESIZABLE
        )
        pg.display.set_caption(self.TITLE)
        self.clock = pg.time.Clock()

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.players = pg.sprite.Group()
        self.objects = pg.sprite.Group()
        self.player = Player(self)
        self.players.add(self.player)
        self.gameMap = Map(self)

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(self.FPS) / 1000.0
            self.update()
            self.events()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def draw(self):
        self.screen.fill(self.BGCOLOR)
        # DRAW CONsOLe AND MAP
        gameMap, mapPos = self.gameMap.getMap()
        self.map_size = gameMap.get_size()
        for sprite in self.players:
            pg.draw.rect(gameMap, pg.Color("blue"), sprite.rect)
            pg.draw.line(
                gameMap,
                pg.Color("red"),
                sprite.pos,
                sprite.pos + sprite.vel,
            )
            gameMap.blit(sprite.image, sprite.rect.topleft)
        self.screen.blit(gameMap, mapPos)

        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
            if event.type == pg.VIDEORESIZE:
                if event.h > self.SCREEN_MIN_HEIGHT:
                    self.window_size["h"] = event.h
                else:
                    self.window_size["h"] = self.SCREEN_MIN_HEIGHT
                if event.w > self.SCREEN_MIN_WIDTH:
                    self.window_size["w"] = event.w
                else:
                    self.window_size["w"] = self.SCREEN_MIN_WIDTH
                self.window = pg.display.set_mode(
                    (self.window_size["w"], self.window_size["h"]), pg.RESIZABLE
                )

    def update(self):
        # update portion of the game loop
        self.players.update()
