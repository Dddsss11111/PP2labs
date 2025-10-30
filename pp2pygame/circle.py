import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Red Ball Move")
clock = pygame.time.Clock()

R = 25
STEP = 20
x, y = WIDTH // 2, HEIGHT // 2
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            nx, ny = x, y
            if event.key == pygame.K_LEFT:
                nx -= STEP
            elif event.key == pygame.K_RIGHT:
                nx += STEP
            elif event.key == pygame.K_UP:
                ny -= STEP
            elif event.key == pygame.K_DOWN:
                ny += STEP
            if nx - R >= 0 and nx + R <= WIDTH and ny - R >= 0 and ny + R <= HEIGHT:
                x, y = nx, ny

    screen.fill((141, 247, 226))
    pygame.draw.circle(screen, (245, 141, 0), (x, y), R)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
