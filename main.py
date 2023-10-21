from settings import *
from world import World
from mouse_handler import MouseHandler
from button import Button


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
        self.world = World(self)
        self.mouse_handler = MouseHandler(self)
        self.curr_team = 'none'
        self.render_world = True

        def a(app):
            app.render_world = not app.render_world

        self.button = Button(self, a, args=[self], pos=[10, 10], size=[100, 100])

    def update(self):
        self.delta_time = self.clock.tick()
        self.time = self.clock.get_time() * 0.001
        pg.display.set_caption(f'FPS: {self.clock.get_fps():.0f}')

    def click_update(self, pos):
        self.button.click(pos)

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
        self.button.show()
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
    app.render_world = False  # test
    app.run()
# сделать: меню, текстуры, зум, атаку клеток
