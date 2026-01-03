import pygame
import random
import sys
import numpy as np

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=1)

SCREEN_DIM = 800
GRID_SIZE = 5
CELL_SIZE = 100
FPS = 5
RGB_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

START_POS = (SCREEN_DIM - (GRID_SIZE * CELL_SIZE)) // 2

screen = pygame.display.set_mode((SCREEN_DIM, SCREEN_DIM))
pygame.display.set_caption("Color Grid Square")
clock = pygame.time.Clock()

def generate_color_sound(colors, duration):
    if not colors:
        return None
    
    avg_r = sum(c[0] for c in colors) / len(colors)
    avg_g = sum(c[1] for c in colors) / len(colors)
    avg_b = sum(c[2] for c in colors) / len(colors)
    
    # Map avg R, G, B to frequencies (Pentatonic-ish ranges)
    freq_r = 100 + (avg_r / 255) * 100  # Bass
    freq_g = 300 + (avg_g / 255) * 200  # Mids
    freq_b = 600 + (avg_b / 255) * 400  # Highs
    
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    
    # Generate and mix sine waves
    tone_r = np.sin(freq_r * 2 * np.pi * t)
    tone_g = np.sin(freq_g * 2 * np.pi * t)
    tone_b = np.sin(freq_b * 2 * np.pi * t)
    
    mixed = (tone_r + tone_g + tone_b) / 3
    
    # Apply a small fade out to avoid clicks
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

    colors_this_frame = []
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x = START_POS + col * CELL_SIZE
            y = START_POS + row * CELL_SIZE

            color = random.choice(RGB_COLORS)
            colors_this_frame.append(color)

            pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))

    # Generate and play sound matching the colors
    sound = generate_color_sound(colors_this_frame, 1.0 / FPS)
    if sound:
        sound.play()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()

