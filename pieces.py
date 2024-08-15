class Piece:
    def __init__(self, color):
        self.__color__ = color  

    @property
    def color(self):
        return self.__color__

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
