import pygame
import math
import sys

pygame.init()

# --- Настройки окна ---
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w - 100, info.current_h - 100
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Painter")
clock = pygame.time.Clock()

# --- Цвета ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 30, 30)
GREEN = (50, 200, 70)
BLUE = (40, 90, 250)
YELLOW = (240, 220, 40)

# --- Начальные параметры ---
cur_color = BLACK
pen_size = 10
is_drawing = False
figure = None
start_point = None
last_point = None

win.fill(WHITE)


def draw_figure(surface, start, end, figure_type, color, width):
    """Рисует заданную фигуру"""
    x1, y1 = start
    x2, y2 = end

    if figure_type == "rect":
        rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
        pygame.draw.rect(surface, color, rect, width)

    elif figure_type == "square":
        side = min(abs(x2 - x1), abs(y2 - y1))
        rect = pygame.Rect(x1, y1, side, side)
        pygame.draw.rect(surface, color, rect, width)

    elif figure_type == "circle":
        radius = int(math.hypot(x2 - x1, y2 - y1))
        pygame.draw.circle(surface, color, start, radius, width)

    elif figure_type == "triangle":
        points = [(x1, y2), ((x1 + x2) // 2, y1), (x2, y2)]
        pygame.draw.polygon(surface, color, points, width)

    elif figure_type == "rhomb":
        mid_x, mid_y = (x1 + x2) // 2, (y1 + y2) // 2
        points = [(mid_x, y1), (x2, mid_y), (mid_x, y2), (x1, mid_y)]
        pygame.draw.polygon(surface, color, points, width)


# --- Главный цикл ---
while True:
    keys = pygame.key.get_pressed()
    eraser_active = keys[pygame.K_e]  # E — ластик

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            is_drawing = True
            start_point = event.pos
            last_point = event.pos

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if is_drawing:
                if figure:
                    draw_figure(win, start_point, event.pos, figure, cur_color, 3)
                    figure = None
                is_drawing = False
                last_point = None

        elif event.type == pygame.KEYDOWN:
            # --- Выход ---
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            # --- Очистка ---
            elif event.key == pygame.K_l:
                win.fill(WHITE)

            # --- Смена цвета ---
            elif event.key == pygame.K_k:
                cur_color = BLACK
            elif event.key == pygame.K_r:
                cur_color = RED
            elif event.key == pygame.K_g:
                cur_color = GREEN
            elif event.key == pygame.K_b:
                cur_color = BLUE
            elif event.key == pygame.K_y:
                cur_color = YELLOW

            # --- Выбор фигуры ---
            elif event.key == pygame.K_f:
                figure = "rect"
            elif event.key == pygame.K_s:
                figure = "square"
            elif event.key == pygame.K_c:
                figure = "circle"
            elif event.key == pygame.K_t:
                figure = "triangle"
            elif event.key == pygame.K_h:
                figure = "rhomb"

            # --- Изменение толщины кисти по цифрам 1–9 ---
            elif pygame.K_1 <= event.key <= pygame.K_9:
                pen_size = (event.key - pygame.K_0) * 2  # от 2 до 18 пикселей

    # --- Рисование ---
    if is_drawing and not figure:
        mouse_pos = pygame.mouse.get_pos()
        if last_point:
            draw_col = WHITE if eraser_active else cur_color
            pygame.draw.line(win, draw_col, last_point, mouse_pos, pen_size)
        last_point = mouse_pos

    pygame.display.flip()
    clock.tick(120)
