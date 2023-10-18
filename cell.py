from settings import *


class Cell:
    def __init__(self, app, position=[0, 0], exist=True):
        self.app = app
        self.position = position
        self.exist = exist
        self.connect = [False, False, False, False, False, False]

    def update_connections(self):
        self.connect = [True, True, True, True, True, True]

    def show(self, pos, size):
        if self.exist:
            pg.draw.rect(self.app.screen, WHITE, [*pos, size * SCALE_REDUCTION, size * SCALE_REDUCTION])
            # pos[0]-size[0]/2, pos[1]-size[1]/2
            neighbours = [[-1, 0], [-1, -1], [0, -1], [1, 0], [1, 0], [0, 1]]
            for i in range(6):
                if self.connect[i]:
                    x, y = self.position[0]+neighbours[i][0], self.position[1]+neighbours[i][1]
                    pg.draw.line(self.app.screen, WHITE, self.position, self.app.world.arr[x][y].position)
