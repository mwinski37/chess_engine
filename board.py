import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 1200))
clock = pygame.time.Clock()
running = True

class Board:
    def __init__(self):
        self.rows = 8
        self.cols = 8
        self.tile_size = 150

    def draw(self, screen):
        for i in range(self.rows):
            for j in range(self.cols):
                if (i + j) % 2 == 0:
                    pygame.draw.rect(screen, "gray", (j*self.tile_size, i*self.tile_size,
                                                    self.tile_size, self.tile_size))
                else:
                    pygame.draw.rect(screen, "white", (j*self.tile_size, i*self.tile_size,
                                                    self.tile_size, self.tile_size))
    
board = Board()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False    

    screen.fill("white")

    board.draw(screen)            

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()