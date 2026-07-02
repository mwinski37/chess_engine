import pygame

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1200
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

LIGHT = (255, 190, 125)
DARK = (169, 169, 169)
clock = pygame.time.Clock()
running = True

class BoardRenderer:
    def __init__(self, screen_width, screen_height, rows=8, cols=8):
        self.rows = rows
        self.cols = cols
        self.tile_size = 150

    def draw(self, screen):
        for i in range(self.rows):
            for j in range(self.cols):
                if (i + j) % 2 == 0:
                    pygame.draw.rect(screen, LIGHT, (j*self.tile_size, i*self.tile_size,
                                                    self.tile_size, self.tile_size))
                else:
                    pygame.draw.rect(screen, DARK , (j*self.tile_size, i*self.tile_size,
                                                    self.tile_size, self.tile_size))
    
board = BoardRenderer(SCREEN_WIDTH, SCREEN_HEIGHT)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False    

    screen.fill("white")

    board.draw(screen)            

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()