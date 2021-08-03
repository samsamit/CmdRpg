import os
import pygame as pg
from .utils import load_png

vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        pg.sprite.Sprite.__init__(self)
        loaded_img = pg.image.load(os.path.join("Assets", "TestChar.png"))
        self.orgImage = pg.transform.rotate(loaded_img, -90)
        self.image = self.orgImage
        self.rect = self.image.get_rect()
        self.data = PlayerData()
        self.rot = 0
        self.turn_steps = 0
        self.move_steps = 0
        self.vel = vec(0, 0)
        self.pos = vec(25, 25)

        self.map_size = 1

    def update(self):
        self.get_keys()
        self.image, self.rect = self.handleResize()
        self.image, self.rect = self.rotate()
        self.pos += self.vel * self.game.dt
        self.rect.center = self.pos

    def rotate(self):
        self.rot = (self.rot + self.rot_speed * self.game.dt) % 360
        rot_image = pg.transform.rotate(self.image, self.rot)
        rot_rect = rot_image.get_rect(center=self.image.get_rect().center)
        return rot_image, rot_rect

    def handleResize(self):
        w, h = self.game.map_size
        if self.map_size == 0 and w != 0:
            self.map_size = w
        if w != self.map_size:
            diffMultipler = 1 + (w - self.map_size) / self.map_size
            if diffMultipler > 0:
                self.pos.x = int(self.pos.x * diffMultipler)
                self.pos.y = int(self.pos.y * diffMultipler)
            self.map_size = w

        new_img = pg.transform.scale(
            self.orgImage,
            (
                int(w * self.data.size),
                int(h * self.data.size),
            ),
        )
        new_rect = new_img.get_rect()
        return new_img, new_rect

    def get_keys(self):
        self.rot_speed = 0
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.rot_speed = self.data.speed
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.rot_speed = -self.data.speed
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel = vec(self.data.speed, 0).rotate(-self.rot)
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel = vec(-self.data.speed, 0).rotate(-self.rot)


class PlayerData:
    speed = 100
    size = 0.1


class Direction:
    n = [0, -1]
    ne = [1, -1]
    e = [1, 0]
    se = [1, 1]
    s = [0, 1]
    sw = [-1, 1]
    w = [-1, 0]
    nw = [-1, -1]
