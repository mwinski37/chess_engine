from pieces import Pawn, Knight, Bishop, Rook, Queen, King

import pygame

LIGHT = (255, 190, 125)
DARK = (169, 169, 169)



class BoardRenderer:
    def __init__(self, screen_width, screen_height, rows=8, cols=8):
        self.rows = rows
        self.cols = cols
        self.tile_size = screen_height // cols
        self.images = {
            ("white", "pawn"): pygame.image.load("assets/white_pawn"),
            ("black", "pawn"): pygame.image.load("assets/black_pawn"),
            ("white", "rook"): pygame.image.load("assets/white_rook"),
            ("black", "rook"): pygame.image.load("assets/black_rook"),
            ("black", "knight"): pygame.image.load("assets/black_knight"),
            ("white", "knight"): pygame.image.load("assets/white_knight"),
            ("black", "bishop"): pygame.image.load("assets/black_bishop"),
            ("white", "bishop"): pygame.image.load("assets/white_bishop"),
            ("black", "queen"): pygame.image.load("assets/black_queen"),
            ("white", "queen"): pygame.image.load("assets/white_queen"),
            ("black", "king"): pygame.image.load("assets/black_king"),
            ("white", "king"): pygame.image.load("assets/white_king"),
        }

    def draw(self, screen, board, selected_square):
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
        for row in range(8):
            for col in range(8):
                piece = board.get_piece(row, col)
                if piece:
                    image = self.images[(piece.color, piece.sprite_name)]
                    image = pygame.transform.scale(image, (int(self.tile_size), int(self.tile_size)))

                    x = col * self.tile_size 
                    y = row * self.tile_size 

                    screen.blit(image, (x, y))

        for row in range(self.rows):
            for col in range(self.cols):
                if selected_square == (row, col):
                    pygame.draw.rect(screen, 'green', 
                                    (col*self.tile_size, row*self.tile_size,
                                    self.tile_size, self.tile_size), 3)
                    
    def draw_possible_moves(self, screen, moves):
        if not moves:
            return
        for row, col in moves:
            x = col * self.tile_size + self.tile_size // 2
            y = row * self.tile_size + self.tile_size // 2

            pygame.draw.circle(screen, 'green', (x, y), 12)

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

    def get_piece(self, row, col):
        return self.board[row][col]
    
    def in_bounds(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def print_board(self):
        for row in self.board:
            print(row)
