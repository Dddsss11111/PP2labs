import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Music Player")
clock = pygame.time.Clock()

playlist = ["track1.mp3", "track2.mp3", "track3.mp3"]
index = 0
state = "stopped"

def play():
    global state
    pygame.mixer.music.load(playlist[index])
    pygame.mixer.music.play()
    state = "playing"
    print("Playing:", playlist[index])

def stop():
    global state
    pygame.mixer.music.stop()
    state = "stopped"
    print("Stopped")

def pause_toggle():
    global state
    if state == "playing":
        pygame.mixer.music.pause()
        state = "paused"
        print("Paused")
    elif state == "paused":
        pygame.mixer.music.unpause()
        state = "playing"
        print("Resumed")
    elif state == "stopped":
        play()

def next_song():
    global index
    index = (index + 1) % len(playlist)
    play()

def prev_song():
    global index
    index = (index - 1 + len(playlist)) % len(playlist)
    play()

play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                pause_toggle()
            elif event.key == pygame.K_s:
                stop()
            elif event.key == pygame.K_RIGHT:
                next_song()
            elif event.key == pygame.K_LEFT:
                prev_song()
    if state == "playing" and not pygame.mixer.music.get_busy():
        next_song()
    screen.fill((141, 231, 247))
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
