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
            Button(app, f2, [app], pos=[810, 600], size=[300, 75]),
            Button(app,            pos=[660, 300], size=[600, 175])
        ], pos=[0, 0], size=WIN_RES),

    ]
