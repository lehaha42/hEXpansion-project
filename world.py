from settings import *
from cell import Cell


class World:
    def __init__(self, app, size=8):
        self.app = app
        self.size = size * 2 + 1
        # create basic world
        self.arr = [[Cell(self.app, [i, j], self.size * 1.5 - 1 > i + j >= self.size / 2 - 1)
                     for i in range(self.size)]
                    for j in range(self.size)]

#ПУСТЬ ТАК ОСТАНЕТСЯ
    def show(self, offset, scale):
        for i in range(self.size):
            for j in range(self.size):
                self.arr[j][i].show([(i + j/2)*scale + offset[0], j*scale + offset[1]], scale)
