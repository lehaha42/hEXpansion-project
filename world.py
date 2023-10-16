from sell import Sell
from settings import *


class World:
    def __init__(self, app, size=8):
        self.app = app
        self.size = size
        self.arr = [[Sell(self.app, size*1.5-1 > i + j >= size/2-1)
                     for i in range(self.size)]
                    for j in range(self.size)]

    def show(self, offset, scale):
        for i in range(self.size):
            for j in range(self.size):
                self.arr[j][i].show([(i + j/2)*scale + offset[0], j*scale + offset[1]], [scale*SCALE_REDUCTION, scale*SCALE_REDUCTION])
