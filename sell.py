import pygame as pg
from settings import *


class Sell:
    def __init__(self, app, exist=True):
        self.app = app
        self.exist = exist

    def show(self, pos, size):
        if self.exist:
            pg.draw.rect(self.app.screen, WHITE, [*pos, *size])
