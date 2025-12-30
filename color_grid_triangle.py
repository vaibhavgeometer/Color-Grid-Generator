import pygame
import pygame.gfxdraw
import random
import math

pygame.init()

SCREEN_DIM = 800
SCREEN = pygame.display.set_mode((SCREEN_DIM, SCREEN_DIM))
pygame.display.set_caption("Premium Triangle Color Grid")
CLOCK = pygame.time.Clock()
FPS = 1
ROWS = 5
TRIANGLE_Height = 80
SIDE_LENGTH = TRIANGLE_Height / (math.sqrt(3) / 2)

def get_vibrant_color():
    return (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    SCREEN.fill((15, 15, 20))

    total_height = ROWS * TRIANGLE_Height
    base_width = ROWS * SIDE_LENGTH
    
    start_x = SCREEN_DIM // 2
    start_y = (SCREEN_DIM - total_height) // 2

    for row in range(ROWS):
        row_y = start_y + row * TRIANGLE_Height
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
                p2 = (tri_x, tri_y + TRIANGLE_Height)
                p3 = (tri_x + SIDE_LENGTH, tri_y + TRIANGLE_Height)
                points = [p1, p2, p3]
            else:
                p1 = (tri_x + SIDE_LENGTH / 2, tri_y + TRIANGLE_Height)
                p2 = (tri_x, tri_y)
                p3 = (tri_x + SIDE_LENGTH, tri_y)
                points = [p1, p2, p3]
            
            color = get_vibrant_color()
            
            pygame.gfxdraw.filled_polygon(SCREEN, points, color)
            pygame.gfxdraw.aapolygon(SCREEN, points, color)

    pygame.display.flip()
    CLOCK.tick(FPS)

pygame.quit()
