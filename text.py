from settings import *


class Text:

    points = [[0, 0], [1, 0],
              [0, 1], [1, 1],
              [0, 2], [1, 2]]

    chars = {
        '1': [[2, 1], [1, 5]],
        '2': [[0, 1], [1, 3], [3, 4], [4, 5]],
        '3': [[0, 1], [1, 2], [2, 3], [3, 4]],
        '4': [[0, 2], [2, 3], [1, 5]],
        '5': [[1, 0], [0, 2], [2, 3], [3, 5], [5, 4]],
        '6': [[1, 2], [2, 3], [3, 5], [5, 4], [4, 2]],
        '7': [[0, 1], [1, 4]],
        '8': [[0, 1], [2, 3], [4, 5], [0, 4], [1, 5]],
        '9': [[0, 1], [1, 3], [3, 2], [2, 0], [3, 4]],
        '0': [[1, 0], [0, 4], [4, 5], [5, 1]],

    }

    def __init__(self, screen):
        self.screen = screen

    def char(self, pos, size, n):
        pairs = self.chars.get(n, [[]])
        for pair in pairs:
            if pair:
                n1, n2 = pair
                pg.draw.line(self.screen, WHITE,
                             [self.points[n1][0] * size + pos[0],
                              self.points[n1][1] * size + pos[1]],
                             [self.points[n2][0] * size + pos[0],
                              self.points[n2][1] * size + pos[1]], 2)

    def text(self, pos, size, s):
        l = int((WIN_RES[0] - pos[0]) / (size * 1.2))
        max_l = l * int((WIN_RES[1] - pos[1]) / (size * 2.4))
        for i in range(min(len(s), max_l)):
            self.char([pos[0] + i % l * size * 1.2,
                       pos[1] + i // l * size * 2.4], size, s[i])
