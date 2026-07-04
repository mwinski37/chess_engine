

class Piece:
    def __init__(self, color):
        self.color = color
        self.has_moved = False

    def __repr__(self):
        return f"{self.color[0].upper()}{self.__class__.__name__[0]}"

class Pawn(Piece):
    sprite_name = "pawn"
    def get_moves(self, board, row, col):

        moves = []

        if self.color == 'black' and row == 1:
            pawn_moves = [(+1,0),(+2,0)]
        elif self.color == 'white' and row == 6:
            pawn_moves = [(-1,0),(-2,0)]


        for move in pawn_moves:
            new_row = row + move[0]
            new_col = col + move[1]

            if board.in_bounds(new_row, new_col):
                piece = board.get_piece(new_row, new_col)
                if piece is None:
                    moves.append((new_row, new_col))
                elif piece.color != self.color:
                    moves.append(new_row, new_col)

        return moves

class Knight(Piece):
    sprite_name = "knight"
    def get_moves(self, board, row, col):

        moves = []

        knight_moves = [(-2,-1),(-2,+1),(-1,-2),(-1,+2),(+1,-2),(+1,+2),(+2,-1),(+2,+1)]

        for move in knight_moves:
            new_row = row + move[0]
            new_col = col + move[1]

            if board.in_bounds(new_row, new_col):
                piece = board.get_piece(new_row, new_col)
                if piece is None:
                    moves.append((new_row, new_col))
                elif piece.color != self.color:
                    moves.append((new_row, new_col))
                            
        return moves


class Bishop(Piece):
    sprite_name = "bishop"
    pass

class Rook(Piece):
    sprite_name = "rook"
    pass

class Queen(Piece):
    sprite_name = "queen"
    pass

class King(Piece):
    sprite_name = "king"
    pass