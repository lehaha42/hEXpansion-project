from settings import *


class Button:
    def __init__(self, app, func=lambda : None, args=[], pos=[0, 0], size=[0, 0], texture_name='None'):
        self.app = app
        self.pos = pos
        self.size = size
        self.func = func
        self.func_args = args
        self.exist = True
        self.texture = self.app.texture.get_texture(texture_name)

    def click(self, pos: list):
        if 0 < pos[0] - self.pos[0] < self.size[0] and 0 < pos[1] - self.pos[1] < self.size[1] and self.exist:
            self.func(*self.func_args)

    def show(self):
        if self.exist:
            if self.texture:
                self.app.place_texture(self.app.scale_texture(self.texture, self.size), self.pos)
            pg.draw.rect(self.app.screen, WHITE, [*self.pos, *self.size], 3)

    def set_exist(self, val: bool):
        self.exist = val
