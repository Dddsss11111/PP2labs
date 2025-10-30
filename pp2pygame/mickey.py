import pygame
import sys
import datetime

pygame.init()
WIDTH, HEIGHT = 1440, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")
clock = pygame.time.Clock()

mickey = pygame.image.load("mickey.jpg").convert_alpha()
right_hand = pygame.image.load("right_hand.png").convert_alpha()
left_hand = pygame.image.load("left_hand.png").convert_alpha()

center = (WIDTH // 2, HEIGHT // 2)

def rotate_hand(image, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    rect = rotated_image.get_rect(center=center)
    return rotated_image, rect

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    now = datetime.datetime.now()
    seconds = now.second
    minutes = now.minute

    second_angle = -seconds * 6
    minute_angle = -(minutes * 6 + seconds * 0.1)

    screen.fill((141, 231, 247))
    mickey_rect = mickey.get_rect(center=center)
    screen.blit(mickey, mickey_rect)
    rotated_left, rect_left = rotate_hand(left_hand, second_angle)
    screen.blit(rotated_left, rect_left)
    rotated_right, rect_right = rotate_hand(right_hand, minute_angle)
    screen.blit(rotated_right, rect_right)
    pygame.display.flip()
    clock.tick(60)
