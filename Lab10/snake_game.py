import pygame as pg
import sys, random
from pygame import Vector2
from snake_database import init_db, find_or_create_player, persist_progress

username = input("Введите имя игрока: ")
init_db()
player_id, stored_score, stored_level = find_or_create_player(username)
print(f"Сохранённый счёт: {stored_score}, уровень: {stored_level}")

pg.init()
CELL = 40
COUNT = 20
screen = pg.display.set_mode((COUNT*CELL, COUNT*CELL))
pg.display.set_caption("Classic Snake")
clock = pg.time.Clock()
font = pg.font.Font('freesansbold.ttf', 25)

FOOD_MAP = {
    "apple": {"color": (211,25,55), "points": 1, "lifetime": 5000},
    "banana": {"color": (255,255,0), "points": 2, "lifetime": 4000},
    "grape": {"color": (138,43,226), "points": 3, "lifetime": 3000}
}

class Fruit:
    def __init__(self, snake):
        self.snake = snake
        self.spawn()

    def draw(self):
        pg.draw.rect(screen, self.color, pg.Rect(int(self.pos.x*CELL), int(self.pos.y*CELL), CELL, CELL))

    def spawn(self):
        while True:
            self.pos = Vector2(random.randint(0, COUNT-1), random.randint(0, COUNT-1))
            if self.pos not in self.snake.body:
                break
        self.kind = random.choice(list(FOOD_MAP.keys()))
        self.color = FOOD_MAP[self.kind]["color"]
        self.points = FOOD_MAP[self.kind]["points"]
        self.lifetime = FOOD_MAP[self.kind]["lifetime"]
        self.t0 = pg.time.get_ticks()

    def expire_check(self):
        if pg.time.get_ticks() - self.t0 > self.lifetime:
            self.spawn()

class Worm:
    def __init__(self):
        self.body = [Vector2(6,10), Vector2(7,10)]
        self.dir = Vector2(1,0)
        self.grow = False

    def draw(self):
        for b in self.body:
            pg.draw.rect(screen, (64,109,228), pg.Rect(b.x*CELL, b.y*CELL, CELL, CELL))

    def step(self):
        self.body.insert(0, self.body[0] + self.dir)
        if not self.grow:
            self.body.pop()
        self.grow = False

    def add_segment(self):
        self.grow = True

class GameManager:
    def __init__(self, score=0, level=1):
        self.worm = Worm()
        self.fruit = Fruit(self.worm)
        self.score = score
        self.level = level
        self.speed = max(50, 150 - (self.level - 1) * 20)
        self.obstacles = self._make_walls(level)

    def _make_walls(self, level):
        if level == 1:
            return [(5,5),(6,5),(7,5)]
        if level == 2:
            return [(3,3),(3,4),(4,4),(5,4)]
        if level == 3:
            return [(2,2),(2,3),(3,3),(4,3),(5,3)]
        if level == 4:
            return [(8,8),(9,8),(10,8),(8,9),(8,10)]
        return [(1,18),(2,18),(3,18),(4,18),(5,18),(6,18)]

    def draw_walls(self):
        for w in self.obstacles:
            pg.draw.rect(screen, (180,40,40), pg.Rect(w[0]*CELL, w[1]*CELL, CELL, CELL))

    def update(self):
        self.worm.step()
        self._check_eat()
        self._check_dead()
        self.fruit.expire_check()

    def draw(self):
        self.worm.draw()
        self.fruit.draw()
        self.draw_walls()
        self._draw_info()

    def _check_eat(self):
        if self.fruit.pos == self.worm.body[0]:
            self.score += self.fruit.points
            self.worm.add_segment()
            self.fruit.spawn()
            if self.score % 5 == 0:
                self._level_up()

    def _level_up(self):
        if self.level < 5:
            self.level += 1
            self.speed = max(50, self.speed - 20)
            pg.time.set_timer(TICK_EVENT, self.speed)
            self.obstacles = self._make_walls(self.level)

    def _check_dead(self):
        head = self.worm.body[0]
        if not 0 <= head.x < COUNT or not 0 <= head.y < COUNT or head in self.worm.body[1:]:
            self._end_game()
        for w in self.obstacles:
            if head == Vector2(w[0], w[1]):
                self._end_game()

    def _end_game(self):
        persist_progress(player_id, self.score, self.level)
        pg.quit()
        print("Игра окончена. Прогресс сохранён.")
        sys.exit()

    def _draw_info(self):
        screen.blit(font.render(f"Score: {self.score}", True, (255,255,255)), (10,10))
        screen.blit(font.render(f"Level: {self.level}", True, (255,255,255)), (10,40))
        screen.blit(font.render("Нажмите стрелку, чтобы начать", True, (255,255,255)), (10,70))

TICK_EVENT = pg.USEREVENT
game = GameManager(score=stored_score, level=stored_level)
pg.time.set_timer(TICK_EVENT, game.speed)

paused = False
running = True
started = False

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            persist_progress(player_id, game.score, game.level)
            pg.quit()
            sys.exit()
        elif event.type == TICK_EVENT and not paused and started:
            game.update()
        elif event.type == pg.KEYDOWN:
            if not started and event.key in [pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT]:
                started = True
            if event.key == pg.K_UP and game.worm.dir.y != 1:
                game.worm.dir = Vector2(0, -1)
            if event.key == pg.K_DOWN and game.worm.dir.y != -1:
                game.worm.dir = Vector2(0, 1)
            if event.key == pg.K_LEFT and game.worm.dir.x != 1:
                game.worm.dir = Vector2(-1, 0)
            if event.key == pg.K_RIGHT and game.worm.dir.x != -1:
                game.worm.dir = Vector2(1, 0)
            if event.key == pg.K_p:
                paused = not paused
                if paused:
                    persist_progress(player_id, game.score, game.level)

    screen.fill((170,215,81))
    game.draw()
    if not started:
        txt = font.render("Нажмите любую стрелку, чтобы начать", True, (0,0,0))
        screen.blit(txt, (COUNT * CELL // 4, COUNT * CELL // 2))
    pg.display.flip()
    clock.tick(60)
