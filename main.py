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

        self.world.arr[7][14].team = 3
        self.world.arr[7][14].amount = 3
        self.world.arr[0][7].team = 2
        self.world.arr[0][7].amount = 3
        self.world.arr[14][0].team = 1
        self.world.arr[14][0].amount = 3

        self.mouse_handler = MouseHandler(self)

        self.menus = build_menus(self)

        self.texture = Texture(self)

        self.curr_team = 3
        self.our_team = 3
        self.logic_state = 0
        self.team_power = 0
        self.render_world = False
        self.selected = None  # self.world.arr[7][7]

    def update_logic(self, cell: Cell):
        if self.logic_state == 0:
            if self.selected is None:
                if cell.team == self.curr_team:
                    self.selected = cell
            elif self.selected is cell:
                self.selected = None
            else:
                x, y = cell.pos
                neigh = [[1, 0], [0, 1], [1, -1]]
                for i in range(len(neigh)):
                    if self.world.is_exist([x + neigh[i][0], y + neigh[i][1]]):
                        if self.selected.pos == [x + neigh[i][0], y + neigh[i][1]] and \
                                cell.connect[i]:
                            self.attack_logic(cell)
                    if self.world.is_exist([x - neigh[i][0], y - neigh[i][1]]):
                        if self.selected.pos == [x - neigh[i][0], y - neigh[i][1]] and \
                                self.selected.connect[i]:
                            self.attack_logic(cell)
            if self.world.done_team(self.curr_team):
                self.team_power = self.world.count_cells(self.curr_team)
                self.logic_state = 1
                self.selected = None
        else:
            if self.team_power > 0:
                if cell.team == self.curr_team:
                    if cell.amount < cell.limit:
                        cell.amount += 1
                        self.team_power += -1
                    if self.team_power == 0:
                        self.logic_state = 0
                        self.curr_team = self.curr_team % 3 + 1
            else:
                self.logic_state = 0
                self.curr_team = self.curr_team % 3 + 1

    def attack_logic(self, cell: Cell):
        if self.selected.amount > 1:
            if cell.team == 0:
                cell.amount = self.selected.amount - 1
                cell.team = self.curr_team
                self.selected.amount = 1
                self.selected = cell
            elif cell.team != self.curr_team:
                if self.selected.amount > cell.amount:
                    cell.amount = self.selected.amount - cell.amount
                    cell.team = self.curr_team
                    self.selected.amount = 1
                    self.selected = cell
                elif self.selected.amount == cell.amount:
                    cell.amount = 1
                    self.selected.amount = 1
                else:
                    cell.amount = cell.amount - self.selected.amount
                    self.selected.amount = 1

    def skip_team(self):
        if self.logic_state == 0:
            self.selected = None
            self.team_power = self.world.count_cells(self.curr_team)
            self.logic_state = 1

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
            teams = self.world.count_teams()
            if sum(teams) != 0:
                p1 = (teams[0] / sum(teams)) * WIN_RES[0]
                p2 = (teams[1] / sum(teams)) * WIN_RES[0]
                pg.draw.rect(self.screen, TEAMS[1], [0, WIN_RES[1] - 20, p1, 20])
                pg.draw.rect(self.screen, TEAMS[2], [p1, WIN_RES[1] - 20, p2, 20])
                pg.draw.rect(self.screen, TEAMS[3], [p1 + p2, WIN_RES[1] - 20, WIN_RES[0] - p2 - p1, 20])
            pg.draw.rect(self.screen, TEAMS[self.curr_team], [50, 50, 430, 100])
            if self.logic_state:
                pg.draw.rect(self.screen, WHITE, [50, 50, 430, 100], 2)
                self.text([60, 60], 40, 'распределите силу по клеткам')
                self.text([60, 100], 40, 'силы осталось: ' + str(self.team_power))
            else:
                self.text([60, 60], 40, 'атакуйте соседние клетки')
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
сделать:        -in progress
    текстуры:        -in progress
        базовая работа с текстурой     -done
        текстуру клеток
    игровую логику:        -in progress
        ходы: -in progress
            выбор своей клетки     -done
            распространение сил     -done
            команда игрока        -in progress
        победа:        -in progress
            подсчет оставшихся клеток     -done
            смэрть команды
        'ии' противника(рандом/алгоритм)
"""
