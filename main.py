from settings import *
from world import World
from mouse_handler import MouseHandler
from button import Button
from menu import Menu
from menus_builder import build_menus
from texture import Texture
from cell import Cell


class App:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(WIN_RES)
        pg.display.set_caption(NAME)

        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.time = 0

        self.is_running = True
        self.on_init()

    def on_init(self):

        self.world = World(self, scale=70)
        pos = Cell.get_position([0, 0], [self.world.size - 1, self.world.size - 1], self.world.scale)
        self.world.move_for([(WIN_RES[0] - pos[0]) / 2, (WIN_RES[1] - pos[1]) / 2])

        self.mouse_handler = MouseHandler(self)

        self.menus = build_menus(self)

        self.texture = Texture(self)

        self.curr_team = 'none'
        self.render_world = True
        self.selected = None  # self.world.arr[7][7]

    def update(self):
        self.delta_time = self.clock.tick()
        self.time = self.clock.get_time() * 0.001
        pg.display.set_caption(f'FPS: {self.clock.get_fps():.0f}')

    def click_update(self, pos):
        for menu in self.menus:
            menu.click(pos)
        self.world.update(pos)

    def handle_events(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.is_running = False

        self.mouse_handler.update(events)

    def render(self):
        self.screen.fill(BACKGROUND)
        if self.render_world:
            self.world.show()
        for menu in self.menus:
            menu.show()
        #texture = self.texture.texture_0
        #texture = pg.transform.scale(texture, [self.world.scale, self.world.scale])
        #self.screen.blit(texture, [0, 0])
        pg.display.flip()

    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
        pg.quit()
        sys.exit()


if __name__ == '__main__':
    app = App()
    app.render_world = False
    app.run()

# сделать: текстуры, игровую логику
