from settings import *
from menu import Menu
from button import Button


def build_menus(app):

    def f(app, val):
        app.is_running = val

    def f2(app):
        app.menus[0].set_exist(False)
        app.render_world = True

    button1 = Button(app, f2, [app], pos=[810, 500], size=[300, 75])
    button2 = Button(app, lambda : None, pos=[810, 625], size=[300, 75])
    button3 = Button(app, lambda : None, pos=[810, 750], size=[300, 75])
    button4 = Button(app, f, [app, False], pos=[810, 875], size=[300, 75])
    title = Button(app, lambda : None, pos=[660, 300], size=[600, 175])
    menu1 = Menu(app, [button1, button2, button3, button4, title], pos=[0, 0], size=WIN_RES)
    menus = [menu1]
    return menus
