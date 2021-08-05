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

        self.rot = 0
        self.vel = vec(0, 0)
        self.pos = vec(25, 25)

        # control variables
        self.turnDir = 0
        self.turn_steps = 0
        self.moveDir = 0
        self.move_steps = 0

        # player stats
        self.data = PlayerData()
        self.hit_rect = pg.Rect(
            (0, 0),
            (
                self.game.map_size[0] * self.data.size,
                self.game.map_size[1] * self.data.size,
            ),
        )

        self.map_size = 1

    def update(self):
        if self.game.testMode:
            self.get_keys()
        else:
            self.handleMovement()
        self.image, self.rect = self.handleResize()
        self.image, self.rect = self.rotate()
        self.pos += self.vel * self.game.dt
        self.rect.center = self.pos
        self.hit_rect.centerx = self.pos.x
        self.borderCollision("x")
        self.hit_rect.centery = self.pos.y
        self.borderCollision("y")

    def handleMovement(self):
        self.rot_speed = 0
        self.vel = vec(0, 0)
        if self.turn_steps > 0:
            self.rot_speed = self.data.speed * self.turnDir
            self.turn_steps -= 1

        if self.move_steps > 0:
            self.vel = vec(self.data.speed * self.moveDir, 0).rotate(-self.rot)
            self.move_steps -= 1

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
        self.hit_rect.w = int(w * self.data.size)
        self.hit_rect.h = int(h * self.data.size)
        new_rect = new_img.get_rect()
        return new_img, new_rect

    def get_keys(self):
        self.rot_speed = 0
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.rot_speed = self.data.speed
        if keys[pg.K_RIGHT]:
            self.rot_speed = -self.data.speed
        if keys[pg.K_UP]:
            self.vel = vec(self.data.speed, 0).rotate(-self.rot)
        if keys[pg.K_DOWN]:
            self.vel = vec(-self.data.speed, 0).rotate(-self.rot)

    def borderCollision(self, dir):
        if dir == "x":
            hits = pg.sprite.spritecollide(
                self, self.game.borders, False, self.collide_hit_rect
            )
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.hit_rect.width / 2.0
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right + self.hit_rect.width / 2.0
                self.vel.x = 0
                self.hit_rect.centerx = self.pos.x
        if dir == "y":
            hits = pg.sprite.spritecollide(
                self, self.game.borders, False, self.collide_hit_rect
            )
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.hit_rect.height / 2.0
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom + self.hit_rect.height / 2.0
                self.vel.y = 0
                self.hit_rect.centery = self.pos.y
        pass

    def collide_hit_rect(self, one, two):
        return one.hit_rect.colliderect(two.rect)


class PlayerData:
    def __init__(self) -> None:
        self.speed = 100
        self.size = 0.1


class Direction:
    n = [0, -1]
    ne = [1, -1]
    e = [1, 0]
    se = [1, 1]
    s = [0, 1]
    sw = [-1, 1]
    w = [-1, 0]
    nw = [-1, -1]
