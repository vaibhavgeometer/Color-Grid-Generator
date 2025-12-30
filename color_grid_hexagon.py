import pygame
import random
import math

pygame.init()

SCREEN_DIM = 800
SCREEN = pygame.display.set_mode((SCREEN_DIM, SCREEN_DIM))
pygame.display.set_caption("Premium Hexagon Color Grid")
CLOCK = pygame.time.Clock()
FPS = 1
HEX_RADIUS = 3
SIZE = 40

def get_vibrant_color():
    return (random.randint(60, 255), random.randint(60, 255), random.randint(60, 255))

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

    SCREEN.fill((10, 10, 15))

    hex_width = math.sqrt(3) * SIZE
    hex_height = 2 * SIZE
    vert_spacing = 1.5 * SIZE
    horiz_spacing = hex_width
    
    center_screen_x = SCREEN_DIM // 2
    center_screen_y = SCREEN_DIM // 2

    for q in range(-HEX_RADIUS, HEX_RADIUS + 1):
        r1 = max(-HEX_RADIUS, -q - HEX_RADIUS)
        r2 = min(HEX_RADIUS, -q + HEX_RADIUS)
        for r in range(r1, r2 + 1):
            cx = center_screen_x + SIZE * (math.sqrt(3) * q + (math.sqrt(3)/2) * r)
            cy = center_screen_y + SIZE * (1.5 * r)
            
            color = get_vibrant_color()
            
            points = get_hexagon_points(cx, cy, SIZE - 2, rotation=30)
            
            pygame.draw.polygon(SCREEN, color, points)
            pygame.draw.polygon(SCREEN, (255, 255, 255), points, 2)
            
            inner_points = get_hexagon_points(cx, cy, SIZE * 0.6, rotation=30)
            pygame.draw.polygon(SCREEN, (max(0, color[0]-40), max(0, color[1]-40), max(0, color[2]-40)), inner_points)

    pygame.display.flip()
    CLOCK.tick(FPS)

pygame.quit()
