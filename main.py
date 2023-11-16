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

        self.world.arr[7][7].team = 3
        self.world.arr[7][7].amount = 2

        self.mouse_handler = MouseHandler(self)

        self.menus = build_menus(self)

        self.texture = Texture(self)

        self.curr_team = 3
        self.curr_state = 0
        self.our_team = 3
        self.render_world = False
        self.selected = None  # self.world.arr[7][7]

    def update_logic(self, cell: Cell):
        if self.selected is None:
            if cell.team == self.our_team == self.curr_team:
                self.selected = cell
        elif self.selected is cell:
            self.selected = None
        else:
            pos = cell.pos
            neighbours = [[-1, 0], [0, -1], [-1, 1]]
            for i in range(3):
                if self.world.is_exist([]):
                    pass

    def text(self, pos: list, scale: float, text: str):
        self.screen.blit(pg.font.Font(None, scale).render(text, True, WHITE), pos)

    def update(self):
        self.delta_time = self.clock.tick()
        self.time = self.clock.get_time() * 0.001
        pg.display.set_caption(f'FPS: {self.clock.get_fps():.0f}')

    def click_update(self, pos: list):
        for menu in self.menus:
            menu.click(pos)
        if self.render_world:
            self.world.update(pos)

    def handle_events(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.is_running = False

        self.mouse_handler.update(events)

    def place_texture(self, texture, pos: list):
        self.screen.blit(texture, pos)

    def scale_texture(self, texture, size: float):
        texture = pg.transform.scale(texture, size)

        return texture

    def render(self):
        self.screen.fill(BACKGROUND)
        if self.render_world:
            self.world.show()
        for menu in self.menus:
            menu.show()

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

"""
сделать:
    текстуры:
        базовая работа с текстурой
        текстуру клеток
    игровую логику:
        ходы:
            выбор своей клетки
            распространение сил
            смена команды
        победа:
            подсчет оставшихся клеток
            смэрть команды
        'ии' противника(рандом/алгоритм)
"""
