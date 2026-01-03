import pygame
import pygame.gfxdraw
import random
import sys
import math
import numpy as np

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=1)

SCREEN_DIM = 800
GRID_SIZE = 5
HEX_SIZE = 40
FPS = 5

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

def generate_color_sound(colors, duration):
    if not colors:
        return None
    
    avg_r = sum(c[0] for c in colors) / len(colors)
    avg_g = sum(c[1] for c in colors) / len(colors)
    avg_b = sum(c[2] for c in colors) / len(colors)
    
    freq_r = 100 + (avg_r / 255) * 100
    freq_g = 300 + (avg_g / 255) * 200
    freq_b = 600 + (avg_b / 255) * 400
    
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    
    tone_r = np.sin(freq_r * 2 * np.pi * t)
    tone_g = np.sin(freq_g * 2 * np.pi * t)
    tone_b = np.sin(freq_b * 2 * np.pi * t)
    
    mixed = (tone_r + tone_g + tone_b) / 3
    fade_len = int(sample_rate * 0.05)
    if fade_len < len(mixed):
        fade_out = np.linspace(1., 0., fade_len)
        mixed[-fade_len:] *= fade_out

    audio = (mixed * 32767).astype(np.int16)

    # Ensure array matches mixer channels
    mixer_info = pygame.mixer.get_init()
    if mixer_info:
        channels = mixer_info[2]
        if channels == 2:
            audio = np.column_stack((audio, audio))

    return pygame.sndarray.make_sound(audio)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    center_screen_x = SCREEN_DIM // 2
    center_screen_y = SCREEN_DIM // 2

    colors_this_frame = []
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
            colors_this_frame.append(color)
            
            points = get_hexagon_points(cx, cy, HEX_SIZE, rotation=30)
            gfx_points = [(int(round(x)), int(round(y))) for x, y in points]
            
            pygame.gfxdraw.filled_polygon(screen, gfx_points, color)
            pygame.gfxdraw.aapolygon(screen, gfx_points, color)

    sound = generate_color_sound(colors_this_frame, 1.0 / FPS)
    if sound:
        sound.play()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()

