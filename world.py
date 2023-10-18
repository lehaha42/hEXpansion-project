from settings import *
from cell import Cell


class World:
    def __init__(self, app, size=8, scale=100, offset=[0, 0]):
        self.app = app
        self.size = size
        self.scale = scale
        self.offset = offset
        self.arr = [[Cell(self.app, size * 1.5 - 1 > i + j >= size / 2 - 1)
                     for i in range(self.size)]
                    for j in range(self.size)]

    def set(self, offset=self.offset, scale=self.scale):
        self.offset = offset
        self.scale = scale

    def show(self):
        for i in range(self.size):
            for j in range(self.size):
                self.arr[j][i].show([(i + j/2)*self.scale + self.offset[0], j*self.scale + self.offset[1]], [self.scale*SCALE_REDUCTION, self.scale*SCALE_REDUCTION])
