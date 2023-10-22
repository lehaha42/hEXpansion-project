from settings import *
from menu import Menu
from button import Button


def build_menus(app):

    def f(app, val):
        app.render_world = val

    button1 = Button(app, f, [app, False], pos=[10, 10], size=[50, 50])
    button2 = Button(app, f, [app, True], pos=[70, 10], size=[50, 50])
    menu1 = Menu(app, [button1, button2], pos=[10, 100], size=[130, 70])

    menus = [menu1]
    return menus
