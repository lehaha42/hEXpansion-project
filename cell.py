from settings import *


class Cell:
    def __init__(self, app, exist=True):
        self.app = app
        self.exist = exist
        self.connect = [False, False, False, False, False, False]

    def show(self, pos, size):
        if self.exist:
            pg.draw.rect(self.app.screen, WHITE, [*pos, *size])
            # pos[0]-size[0]/2, pos[1]-size[1]/2
