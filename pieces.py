

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
        else:
            pawn_moves = [(+1,0)]
        if self.color == 'white' and row == 6:
            pawn_moves = [(-1,0),(-2,0)]
        else:
            pawn_moves = [(+1,0)]


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

    def get_moves(self, board, row, col):
        moves = []

        directions = [
            (-1,-1),
            (-1,+1),
            (+1,-1),
            (+1,+1)
        ]

        for row_direction, col_direction in directions:
            new_row = row + row_direction
            new_col = col + col_direction

            while board.in_bounds(new_row, new_col):
                piece = board.get_piece(new_row, new_col)

                if piece is None:
                    moves.append(new_row, new_col)

                else:
                    if piece.color != self.color:
                        moves.append(new_row, new_col)

                    break

                new_row += row_direction
                new_col += col_direction

        return moves
                    


class Rook(Piece):
    sprite_name = "rook"

    def get_moves(self, board, row, col):
        moves = []

        directions = [
            (+1, 0),
            (-1, 0),
            (0, -1),
            (0, -1)
        ] 

        for row_direction, col_direction in directions:
            new_row = row + row_direction
            new_col = col + col_direction

            while board.in_bounds(new_row, new_col):
                piece = board.get_piece(new_row, new_col)

                if piece is None:
                    moves.append(new_row, new_col)

                else:
                    if piece.color != self.color:
                        moves.append(new_row, new_col)

                    break

            new_row = row_direction
            new_col = col_direction

        return moves

class Queen(Piece):
    sprite_name = "queen"

    def get_moves(self, board, row, col):
        moves = []

        directions = [
            (-1,-1),
            (-1,+1),
            (+1,-1),
            (+1,+1),
            (+1, 0),
            (-1, 0),
            (0, -1),
            (0, -1)
        ]

        for row_direction, col_direction in directions:
            new_row = row + row_direction
            new_col = col + col_direction

            while board.in_bounds(new_row, new_col):
                piece = board.get_piece(new_row, new_col)

                if piece is None:
                    moves.append(new_row, new_col)

                else:
                    if piece.color != self.color:
                        moves.append(new_row, new_col)

                    break

            new_row = row_direction
            new_col = col_direction

        return moves

class King(Piece):
    sprite_name = "king"
    def get_moves(self, board, row, col):
        moves = []

        directions = [
            (-1,-1),
            (-1,+1),
            (+1,-1),
            (+1,+1),
            (+1, 0),
            (-1, 0),
            (0, -1),
            (0, -1)
        ]

        for row_direction, col_direction in directions:
            new_row = row + row_direction
            new_col = col + col_direction

            piece = board.get_piece(new_row, new_col)

            if piece is None:
                moves.append(new_row, new_col)

            elif piece.color != self.color:
                moves.append(new_row, new_col)

        return moves