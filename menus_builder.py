from settings import *
from menu import Menu
from button import Button


def build_menus(app):

    def f2(app):
        app.menus[0].exist = False
        app.render_world = True

    def setattrs(*args : tuple):
        """
        multiple settatr()
        :param args: tuple
        :return:
        """
        for arg in args:
            setattr(*arg)

    setattrs()

    return [
        Menu(app, [
            Button(app, f2, [app], pos=[810, 500], size=[300, 75]),
            Button(app, pos=[810, 625], size=[300, 75]),
            Button(app, pos=[810, 750], size=[300, 75]),
            Button(app, setattr, [app, 'is_running', False], pos=[810, 875], size=[300, 75]),
            Button(app, pos=[660, 300], size=[600, 175])
        ], pos=[0, 0], size=WIN_RES)
    ]
