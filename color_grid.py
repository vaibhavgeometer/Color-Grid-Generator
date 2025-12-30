import pygame, random
pygame.init()
screen_dim = 700
screen = pygame.display.set_mode((screen_dim, screen_dim))
clock = pygame.time.Clock()
running = True
dimensions = 500

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    surfs = []
    for x in range(100, 100+dimensions, 100):
        for y in range(100, 100+dimensions, 100):
            surfs.append(pygame.surface.Surface((100,100)))
            a = random.randint(0,255)
            b = random.randint(0,255)
            c = random.randint(0,255)
            surfs[-1].fill((a,b,c))
            screen.blit(surfs[-1],(x,y))

    pygame.display.flip()

    clock.tick(1)

pygame.quit()
