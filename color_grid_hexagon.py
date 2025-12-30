import pygame
import pygame.gfxdraw
import random
import sys
import math

pygame.init()

SCREEN_DIM = 800
GRID_SIZE = 5
HEX_SIZE = 40
FPS = 1

screen = pygame.display.set_mode((SCREEN_DIM, SCREEN_DIM))
pygame.display.set_caption("Color Grid Hexagon")
clock = pygame.time.Clock()

def get_hexagon_points(center_x, center_y, size, rotation=0):
    points = []
    for i in range(6):
        angle_deg = 60 * i + rotation
        angle_rad = math.radians(angle_deg)
        x = center_x + size * math.cos(angle_rad)
        y = center_y + size * math.sin(angle_rad)
        points.append((x, y))
    return points

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    center_screen_x = SCREEN_DIM // 2
    center_screen_y = SCREEN_DIM // 2

    grid_radius = GRID_SIZE - 1
    for q in range(-grid_radius, grid_radius + 1):
        r1 = max(-grid_radius, -q - grid_radius)
        r2 = min(grid_radius, -q + grid_radius)
        for r in range(r1, r2 + 1):
            cx = center_screen_x + HEX_SIZE * (math.sqrt(3) * q + (math.sqrt(3)/2) * r)
            cy = center_screen_y + HEX_SIZE * (1.5 * r)
            
            color = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            
            points = get_hexagon_points(cx, cy, HEX_SIZE, rotation=30)
            
            # Convert points to integers for gfxdraw
            gfx_points = [(int(round(x)), int(round(y))) for x, y in points]
            
            pygame.gfxdraw.filled_polygon(screen, gfx_points, color)
            pygame.gfxdraw.aapolygon(screen, gfx_points, color)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
