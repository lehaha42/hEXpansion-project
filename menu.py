from settings import *
from button import Button


class Menu:
    def __init__(self, app, buttons=[], pos=[0, 0], size=[0, 0]):
        self.app = app
        for button in buttons:
            button.set_pos([button.pos[0] + pos[0], button.pos[1] + pos[1]])
        self.buttons = buttons
        self.pos = pos
        self.size = size
        self.exist = True

    def click(self, pos):
        if self.exist:
            for button in self.buttons:
                button.click(pos)

    def show(self):
        if self.exist:
            pg.draw.rect(self.app.screen, WHITE, [*self.pos, *self.size], 3)
            for button in self.buttons:
                button.show()

    def set_exist(self, exist=True):
        self.exist = exist
