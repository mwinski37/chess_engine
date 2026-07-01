import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 1200))
clock = pygame.time.Clock()
running = True

tiles = []
tile = pygame.Rect(0,0,120,120)

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            tiles.append('0')
        else:
            tiles.append('1')
    

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False    

    screen.fill("white")

    x = 0
    y = 0

    for i in tiles:
        if i == '1':
            pygame.draw.rect(screen, "gray", (x, y, 150, 150))

        x += 150
        if x == 8 * 150:
            x = 0
            y += 150

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()