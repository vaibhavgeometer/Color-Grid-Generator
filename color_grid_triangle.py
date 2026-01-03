import pygame
import pygame.gfxdraw
import random
import sys
import math

pygame.init()

SCREEN_DIM = 800
GRID_SIZE = 5
TRIANGLE_HEIGHT = 80
SIDE_LENGTH = TRIANGLE_HEIGHT / (math.sqrt(3) / 2)
FPS = 2

screen = pygame.display.set_mode((SCREEN_DIM, SCREEN_DIM))
pygame.display.set_caption("Color Grid Triangle")
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    total_height = GRID_SIZE * TRIANGLE_HEIGHT
    start_x = SCREEN_DIM // 2
    start_y = (SCREEN_DIM - total_height) // 2

    colors_this_frame = []
    for row in range(GRID_SIZE):
        row_y = start_y + row * TRIANGLE_HEIGHT
        num_triangles = 2 * row + 1
        
        row_half_width = (row + 1) * SIDE_LENGTH / 2
        row_start_x = start_x - row_half_width
        
        for k in range(num_triangles):
            is_up = (k % 2 == 0)
            
            tri_x = row_start_x + k * (SIDE_LENGTH / 2)
            tri_y = row_y
            
            points = []
            if is_up:
                p1 = (tri_x + SIDE_LENGTH / 2, tri_y)
                p2 = (tri_x, tri_y + TRIANGLE_HEIGHT)
                p3 = (tri_x + SIDE_LENGTH, tri_y + TRIANGLE_HEIGHT)
                points = [p1, p2, p3]
            else:
                p1 = (tri_x + SIDE_LENGTH / 2, tri_y + TRIANGLE_HEIGHT)
                p2 = (tri_x, tri_y)
                p3 = (tri_x + SIDE_LENGTH, tri_y)
                points = [p1, p2, p3]
            
            color = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            colors_this_frame.append(color)
            
            pygame.gfxdraw.filled_polygon(screen, points, color)
            pygame.gfxdraw.aapolygon(screen, points, color)



    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
