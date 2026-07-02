from pieces import Pawn, Knight, Bishop, Rook, Queen, King

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
                    pygame.draw.rect(screen, LIGHT,
                                    (j*self.tile_size, i*self.tile_size,
                                    self.tile_size, self.tile_size))
                else:
                    pygame.draw.rect(screen, DARK,
                                    (j*self.tile_size, i*self.tile_size,
                                    self.tile_size, self.tile_size))
    
board_renderer = BoardRenderer(SCREEN_WIDTH, SCREEN_HEIGHT)

class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_position()


    def setup_position(self):
        back_rank = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]

        for col, piece_class in enumerate(back_rank):
            self.board[0][col] = piece_class("black")
            self.board[7][col] = piece_class("white")

        for col in range(8):
            self.board[1][col] = Pawn("black")
            self.board[6][col] = Pawn("white")

    def print_board(self):
        for row in self.board:
            print(row)

board = Board()

board.print_board()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False    

    screen.fill("white")

    board_renderer.draw(screen)            

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()