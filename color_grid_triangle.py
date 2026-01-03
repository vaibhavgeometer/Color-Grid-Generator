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
TRIANGLE_HEIGHT = 80
SIDE_LENGTH = TRIANGLE_HEIGHT / (math.sqrt(3) / 2)
FPS = 5

screen = pygame.display.set_mode((SCREEN_DIM, SCREEN_DIM))
pygame.display.set_caption("Color Grid Triangle")
clock = pygame.time.Clock()

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

    sound = generate_color_sound(colors_this_frame, 1.0 / FPS)
    if sound:
        sound.play()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()

