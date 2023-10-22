from settings import *
from cell import Cell


class World:
    def __init__(self, app, size=7, scale=50, offset=[50, 50]):
        self.scale = scale
        self.offset = offset
        self.app = app
        self.size = size * 2 + 1
        # create basic world
        self.arr = [[Cell(self.app, [i, j], offset, scale, self.basic_rule([i, j]))
                     for i in range(self.size)]
                    for j in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                self.arr[i][j].update_connections([1, 1, 1])

    def basic_rule(self, pos):
        i, j = pos
        return self.size * 1.5 - 1 > i + j >= self.size / 2 - 1

    def is_exist(self, pos):
        return self.basic_rule(pos) and 0 <= pos[0] < self.size and 0 <= pos[1] < self.size

    def move_for(self, pos):
        self.offset = [self.offset[0] + pos[0], self.offset[1] + pos[1]]

    def zoom(self, direct, pos):
        prev_scale = self.scale

        if direct == 'in':
            self.scale = min(self.scale + 2, 100)
        else:
            self.scale = max(self.scale - 2, 20)

        dif_pos = [self.offset[0] - pos[0], self.offset[1] - pos[1]]
        move_pos = [dif_pos[0] * (self.scale / prev_scale - 1), dif_pos[1] * (self.scale / prev_scale - 1)]

        self.move_for(move_pos)

    def show(self):
        for i in range(self.size):
            for j in range(self.size):
                self.arr[j][i].show(self.offset, [i, j], self.scale)

    def update(self, pos):
        for i in range(self.size):
            for j in range(self.size):
                self.arr[j][i].update(pos)
