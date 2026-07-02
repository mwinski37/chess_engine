

class Piece:
    def __init__(self, color):
        self.color = color
        self.has_moved = False

    def __repr__(self):
        return f"{self.color[0].upper()}{self.__class__.__name__[0]}"

class Pawn(Piece):
    sprite_name = "pawn"
    pass

class Knight(Piece):
    sprite_name = "knight"

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