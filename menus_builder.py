from settings import *
from menu import Menu
from button import Button


def build_menus(app):

    def f(app, val):
        app.is_running = val

    button = Button(app, f, [app, False], pos=[10, 10], size=[50, 50])
    menu1 = Menu(app, [button], pos=[10, 10], size=[100, 100])
    menus = [menu1]
    return menus
