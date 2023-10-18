from settings import *
from world import World


class App:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(WIN_RES)
        #pg.display.set_caption(NAME)

        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.time = 0

        self.is_running = True
        self.on_init()

    def on_init(self):
        self.world = World(self, 15)
        self.scale = 50
        self.offset = [10, 20]

    def update(self):
        self.delta_time = self.clock.tick()
        self.time = self.clock.get_time() * 0.001
        pg.display.set_caption(f'FPS: {self.clock.get_fps():.0f}')

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.is_running = False

    def render(self):
        self.screen.fill(BACKGROUND)
        self.world.show(self.offset, self.scale)
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
    app.run()
#сделать: меню, текстуры, зум, перемещение, команды клеток, соседство клеток
