from settings import *
from button import Button


SCALE = 0.6


class Cell:
    def __init__(self, app, pos: list, offset: list, scale: float, exist=True):
        self.app = app
        self.exist = exist
        self.team = 0
        self.connect = [False, False, False]
        self.selected = False
        self.button = Button(self.app, setattr, [self, 'team', 3],
                             pos=[self.get_position(offset, pos, scale)[0] - scale*SCALE/2,
                                  self.get_position(offset, pos, scale)[1] - scale*SCALE/2],
                             size=[scale*SCALE, scale*SCALE])

    def update_connections(self, connects):
        self.connect = connects

    @staticmethod
    def get_position(offset: list, pos: list, scale: float):
        i, j = pos
        return [(i + j/2)*scale + offset[0], j*scale + offset[1]]

    def update(self, pos: list):
        self.button.click(pos)

    def show(self, offset: list, pos: list, size: float):
        if self.exist:
            cell_pos = self.get_position(offset, pos, size)
            neighbours = [[1, 0], [0, 1], [1, -1]]
            for i in range(3):
                if self.connect[i]:
                    neigh_pos = self.get_position(offset, [pos[0] + neighbours[i][0], pos[1] + neighbours[i][1]], size)
                    if self.app.world.is_exist([pos[0] + neighbours[i][0], pos[1] + neighbours[i][1]]):
                        pg.draw.line(self.app.screen, GRAY, cell_pos, neigh_pos, int(0.1 * size) + 1)
            pg.draw.rect(self.app.screen, TEAMS.get(self.team, GRAY), [cell_pos[0] - size * SCALE / 2 + 1,
                                                                       cell_pos[1] - size * SCALE / 2 + 1,
                                                                       size * SCALE, size * SCALE])
            if self.app.selected == self:
                pg.draw.rect(self.app.screen, WHITE, [cell_pos[0] - size / 2 + 1,
                                                      cell_pos[1] - size / 2 + 1,
                                                      size, size], 2)
            self.button.pos = [self.get_position(offset, pos, size)[0] - size*SCALE/2,
                               self.get_position(offset, pos, size)[1] - size*SCALE/2]
            self.button.size = [size*SCALE, size*SCALE]
