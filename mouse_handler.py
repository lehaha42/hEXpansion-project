from settings import *


class MouseHandler:
    def __init__(self, app):
        self.app = app
        self.pressed = False
        self.pos = [0, 0]
        self.prev_pos = [0, 0]

    def update(self, events):
        self.prev_pos = (self.pos[0], self.pos[1])
        self.pos = pg.mouse.get_pos()
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pass
                if event.button == 3:
                    self.pressed = True
                if event.button == 4:
                    self.app.world.zoom('in', self.pos)
                if event.button == 5:
                    self.app.world.zoom('out', self.pos)
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 3:
                    self.pressed = False

        if self.pressed:
            rel_pos = [self.pos[0] - self.prev_pos[0], self.pos[1] - self.prev_pos[1]]
            self.app.world.move_for(rel_pos)


