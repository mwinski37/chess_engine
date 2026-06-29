import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    pygame.draw.rect(screen, "red", (50,100,50,50), width=0, border_radius=0)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()