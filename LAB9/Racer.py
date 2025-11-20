# Imports
import pygame, sys
from pygame.locals import *
import random, time

# Initialzing
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
COIN_SPEED = 3
SCORE = 0

# count of collected coins (each coin picked counts as 1, regardless of weight)
COINS_COLLECTED = 0

# yellow line borders
LEFT_BORDER = 40
RIGHT_BORDER = 360

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
restart_label = font_small.render("Restart", True, (134, 145, 135))

background = pygame.image.load("AnimatedStreet.png")

# Load sounds
coin_sound = pygame.mixer.Sound("coin_sound.mp3")
crash_sound = pygame.mixer.Sound("crash.wav")

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(LEFT_BORDER + 20, RIGHT_BORDER - 20), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            # passage of enemy no longer gives SCORE or coin count
            self.rect.top = 0
            self.rect.center = (random.randint(LEFT_BORDER + 20, RIGHT_BORDER - 20), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > LEFT_BORDER:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < RIGHT_BORDER:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.respawn_new_coin()

    def respawn_new_coin(self):
        # random weight 1–3 (affects points)
        self.weight = random.randint(1, 3)

        base_image = pygame.image.load("coin.png")

        # size based on weight (slightly larger for heavier)
        size = 16 * self.weight + 16   # gives sizes: 32, 48, 64
        self.image = pygame.transform.scale(base_image, (size, size))
        self.rect = self.image.get_rect()

        # ensure spawn x not too close to enemy initial x (simple attempt)
        self.rect.center = (
            random.randint(LEFT_BORDER + 20, RIGHT_BORDER - 20),
            0
        )

    def move(self):
        global SCORE, COINS_COLLECTED, SPEED, COIN_SPEED
        self.rect.move_ip(0, COIN_SPEED)

        # If coin fell beyond screen → respawn (still counts as not collected)
        if self.rect.top > 600:
            self.respawn_new_coin()

        # Collision with player: collect coin
        if pygame.sprite.collide_rect(self, P1):
            coin_sound.play()
            SCORE += self.weight          # score increases by coin weight
            COINS_COLLECTED += 1          # count coins picked (1 per coin)

            # Increase speed every 3 collected coins (coins count, not score)
            if COINS_COLLECTED % 3 == 0:
                # small gradual increase
                SPEED += 0.5
                COIN_SPEED += 0.3

            # respawn a new coin (one coin on screen at a time)
            self.respawn_new_coin()


# Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Gameplay flag
gameplay = True

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if gameplay:
        DISPLAYSURF.blit(background, (0, 0))
        scores = font_small.render(str(SCORE), True, BLACK)
        DISPLAYSURF.blit(scores, (10, 10))

        # move and draw sprites
        for entity in all_sprites:
            entity.move()
            DISPLAYSURF.blit(entity.image, entity.rect)

        # Collision with enemy -> game over
        if pygame.sprite.spritecollideany(P1, enemies):
            crash_sound.play()
            time.sleep(0.5)
            gameplay = False
    else:
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        final_score = font_small.render("Your Score: " + str(SCORE), True, WHITE)
        DISPLAYSURF.blit(final_score, (130, 320))
        # show how many coins collected as well
        coins_text = font_small.render("Coins: " + str(COINS_COLLECTED), True, WHITE)
        DISPLAYSURF.blit(coins_text, (150, 340))

        restart_label_rect = restart_label.get_rect(topleft=(150, 360))
        DISPLAYSURF.blit(restart_label, restart_label_rect)

        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            # reset game state
            SCORE = 0
            COINS_COLLECTED = 0
            SPEED = 5
            COIN_SPEED = 3

            P1.rect.center = (160, 520)
            E1.rect.center = (random.randint(LEFT_BORDER + 20, RIGHT_BORDER - 20), 0)
            C1.respawn_new_coin()

            gameplay = True

    pygame.display.update()
    FramePerSec.tick(FPS)
