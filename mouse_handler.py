from settings import *


class MouseHandler:
    def __init__(self, app):
        self.app = app

    def update(self, events):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print('1')
                if event.button == 2:
                    print('2')
                if event.button == 3:
                    print('3')
                if event.button == 4:
                    print('4')
                if event.button == 5:
                    print('5')
