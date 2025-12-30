import pygame
import random
import sys

pygame.init()

SCREEN_DIM = 700
GRID_SIZE = 5
CELL_SIZE = 100
FPS = 1

START_POS = (SCREEN_DIM - (GRID_SIZE * CELL_SIZE)) // 2

screen = pygame.display.set_mode((SCREEN_DIM, SCREEN_DIM))
pygame.display.set_caption("Color Grid Square")
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x = START_POS + col * CELL_SIZE
            y = START_POS + row * CELL_SIZE

            color = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )

            pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()
