from board import Board, BoardRenderer
from pieces import Piece

class Game:
    def __init__(self, screen_width, screen_height):
        self.board = Board()
        self.board_renderer = BoardRenderer(screen_width, screen_height)

        self.selected_square = None
        self.selected_piece = None
        self.possible_moves = []
        self.turn = "white"

    def draw(self, screen):
        self.board_renderer.draw(screen, self.board, self.selected_square)
        self.board_renderer.draw_possible_moves(screen, self.possible_moves)

    def on_click(self, pos):
        mouse_x, mouse_y = pos

        col = mouse_x // self.board_renderer.tile_size
        row = mouse_y // self.board_renderer.tile_size

        piece = self.board.get_piece(row, col)

        self.possible_moves = piece.get_moves(self.board, row, col)

        if piece:
            self.selected_square = (row, col)
            self.selected_piece = piece
            print(f"Kliknięto{self.selected_square}{self.selected_piece}")
        else:
            print("Puste pole")