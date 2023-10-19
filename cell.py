from settings import *


SCALE = 0.6

teams = {
    'red': RED,
    'blue': BLUE,
    'green': GREEN,
    'none': GRAY
}


class Cell:
    def __init__(self, app, exist=True):
        self.app = app
        self.exist = exist
        self.team = 'red'
        self.connect = [False, False, False]

    def update_connections(self, connects):
        self.connect = connects

    @staticmethod
    def get_position(offset, pos, scale):
        i, j = pos
        return [(i + j/2)*scale + offset[0], j*scale + offset[1]]

    def show(self, offset, pos, size):
        if self.exist:
            cell_pos = self.get_position(offset, pos, size)
            neighbours = [[1, 0], [0, 1], [1, -1]]
            for i in range(3):
                if self.connect[i]:
                    neigh_pos = self.get_position(offset, [pos[0] + neighbours[i][0], pos[1] + neighbours[i][1]], size)
                    if self.app.world.is_exist([pos[0] + neighbours[i][0], pos[1] + neighbours[i][1]]):
                        pg.draw.line(self.app.screen, GRAY, cell_pos, neigh_pos, 4)
            pg.draw.rect(self.app.screen, teams[self.team], [cell_pos[0] - size * SCALE / 2 + 2,
                                                             cell_pos[1] - size * SCALE / 2 + 2,
                                                             size * SCALE, size * SCALE])
