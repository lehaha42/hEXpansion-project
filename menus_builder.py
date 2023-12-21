from settings import *
from menu import Menu
from button import Button


def build_menus(app):

    def f2(ap):
        ap.menus[0].exist = False
        ap.render_world = True

    def setattrs(*args : list):
        for arg in args:
            setattr(*arg)

    def do_things(*args: list):
        for thing in args:
            thing[0](*thing[1:])

    return [
        Menu(app, [
            Button(app, f2, [app],                           pos=[810, 550], size=[300, 75], texture_name='play_button.png'),
            Button(app, setattr, [app, 'is_running', False], pos=[810, 650], size=[300, 75], texture_name='esc_button.png')
        ], pos=[0, 0], size=WIN_RES)
    ]
