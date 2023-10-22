from settings import *
from button import Button


SCALE = 0.6

teams = {
    'red': RED,
    'blue': BLUE,
    'green': GREEN,
    'none': GRAY
}


class Cell:
    def __init__(self, app, pos, offset, scale, exist=True):
        self.app = app
        self.exist = exist
        self.team = 'none'
        self.connect = [False, False, False]
        self.selected = False
        self.button = Button(self.app, self.atack, [],
                             pos=[self.get_position(offset, pos, scale)[0] - scale*SCALE/2,
                                  self.get_position(offset, pos, scale)[1] - scale*SCALE/2],
                             size=[scale*SCALE, scale*SCALE])

    def update_connections(self, connects):
        self.connect = connects

    @staticmethod
    def get_position(offset, pos, scale):
        i, j = pos
        return [(i + j/2)*scale + offset[0], j*scale + offset[1]]

    def atack(self):
        self.team = 'green'

    def update(self, pos):
        self.button.click(pos)

    def show(self, offset, pos, size):
        if self.exist:
            cell_pos = self.get_position(offset, pos, size)
            neighbours = [[1, 0], [0, 1], [1, -1]]
            for i in range(3):
                if self.connect[i]:
                    neigh_pos = self.get_position(offset, [pos[0] + neighbours[i][0], pos[1] + neighbours[i][1]], size)
                    if self.app.world.is_exist([pos[0] + neighbours[i][0], pos[1] + neighbours[i][1]]):
                        pg.draw.line(self.app.screen, GRAY, cell_pos, neigh_pos, int(0.1 * size) + 1)
            pg.draw.rect(self.app.screen, teams.get(self.team, GRAY), [cell_pos[0] - size * SCALE / 2 + 1,
                                                                       cell_pos[1] - size * SCALE / 2 + 1,
                                                                       size * SCALE, size * SCALE])
            self.button.set_pos(new_pos=[self.get_position(offset, pos, size)[0] - size*SCALE/2,
                                         self.get_position(offset, pos, size)[1] - size*SCALE/2])
