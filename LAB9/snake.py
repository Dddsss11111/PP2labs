import pygame as pg
import sys, random
from pygame.math import Vector2

# === Настройки ===
pg.init()
clock = pg.time.Clock()

CELL = 40
GRID = 20
WIDTH, HEIGHT = GRID * CELL, GRID * CELL
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Snake Game")

font = pg.font.Font('freesansbold.ttf', 25)

# === Типы фруктов ===
FOODS = {
    "apple": {"color": (255, 100, 100), "points": 1, "life": 5000},
    "banana": {"color": (255, 230, 120), "points": 2, "life": 4000},
    "grape": {"color": (190, 110, 255), "points": 3, "life": 3000}
}

# === Класс еды ===
class Fruit:
    def __init__(self, snake):
        self.snake = snake
        self.create_new()

    def draw(self):
        rect = pg.Rect(self.pos.x * CELL, self.pos.y * CELL, CELL, CELL)
        pg.draw.rect(screen, self.color, rect)

    def create_new(self):
        while True:
            self.pos = Vector2(random.randint(0, GRID - 1), random.randint(0, GRID - 1))
            if self.pos not in self.snake.parts:
                break
        kind = random.choice(list(FOODS.keys()))
        self.color = FOODS[kind]["color"]
        self.points = FOODS[kind]["points"]
        self.life = FOODS[kind]["life"]
        self.time = pg.time.get_ticks()

    def check_timer(self):
        if pg.time.get_ticks() - self.time > self.life:
            self.create_new()


# === Класс змейки ===
class Snake:
    def __init__(self):
        self.parts = [Vector2(6, 10), Vector2(5, 10), Vector2(4, 10)]
        self.dir = Vector2(1, 0)
        self.grow = False

    def draw(self):
        for cube in self.parts:
            r = pg.Rect(cube.x * CELL, cube.y * CELL, CELL, CELL)
            pg.draw.rect(screen, (60, 110, 255), r)

    def move(self):
        new = self.parts[0] + self.dir
        self.parts.insert(0, new)
        if not self.grow:
            self.parts.pop()
        self.grow = False

    def extend(self):
        self.grow = True

    def restart(self):
        self.parts = [Vector2(6, 10), Vector2(5, 10), Vector2(4, 10)]
        self.dir = Vector2(1, 0)


# === Основная игра ===
class Game:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit(self.snake)
        self.score = 0
        self.level = 1
        self.speed = 200
        self.over = False

    def update(self):
        if not self.over:
            self.snake.move()
            self.check_eat()
            self.check_fail()
            self.fruit.check_timer()

    def draw(self):
        if not self.over:
            self.snake.draw()
            self.fruit.draw()
            self.draw_ui()
        else:
            self.draw_end()

    def check_eat(self):
        if self.snake.parts[0] == self.fruit.pos:
            self.score += self.fruit.points
            self.snake.extend()
            self.fruit.create_new()
            if self.score % 5 == 0:
                self.next_level()

    def next_level(self):
        self.level += 1
        self.speed = max(80, self.speed - 20)
        pg.time.set_timer(SNAKE_MOVE, self.speed)

    def check_fail(self):
        head = self.snake.parts[0]
        if not 0 <= head.x < GRID or not 0 <= head.y < GRID or head in self.snake.parts[1:]:
            self.over = True

    def restart(self):
        self.snake.restart()
        self.fruit.create_new()
        self.score, self.level = 0, 1
        self.speed = 200
        self.over = False
        pg.time.set_timer(SNAKE_MOVE, self.speed)

    def draw_ui(self):
        s_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        l_text = font.render(f"Level: {self.level}", True, (255, 255, 255))
        screen.blit(s_text, (10, 10))
        screen.blit(l_text, (10, 40))

    def draw_end(self):
        screen.fill((25, 30, 40))
        txt1 = font.render("Game Over", True, (255, 60, 60))
        txt2 = font.render("Restart", True, (210, 210, 210))
        rect2 = txt2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40))
        screen.blit(txt1, (WIDTH // 2 - 80, HEIGHT // 2 - 20))
        screen.blit(txt2, rect2)
        if rect2.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
            self.restart()


# === Цикл игры ===
SNAKE_MOVE = pg.USEREVENT
game = Game()
pg.time.set_timer(SNAKE_MOVE, game.speed)

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            pg.quit()
            sys.exit()
        if event.type == SNAKE_MOVE:
            game.update()
        if event.type == pg.KEYDOWN and not game.over:
            if event.key == pg.K_UP and game.snake.dir.y != 1:
                game.snake.dir = Vector2(0, -1)
            elif event.key == pg.K_DOWN and game.snake.dir.y != -1:
                game.snake.dir = Vector2(0, 1)
            elif event.key == pg.K_LEFT and game.snake.dir.x != 1:
                game.snake.dir = Vector2(-1, 0)
            elif event.key == pg.K_RIGHT and game.snake.dir.x != -1:
                game.snake.dir = Vector2(1, 0)

    if not game.over:
        screen.fill((175, 220, 100))
    game.draw()
    pg.display.flip()
    clock.tick(60)
