import unittest

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

class TestChessPieces(unittest.TestCase):

    def test_piece_color(self):

        piece = Piece('white')
        self.assertEqual(piece.color, 'white')

        piece = Piece('black')
        self.assertEqual(piece.color, 'black')

    def test_rook_color(self):

        rook = Rook('white')
        self.assertEqual(rook.color, 'white')

        rook = Rook('black')
        self.assertEqual(rook.color, 'black')

    def test_pawn_color(self):

        pawn = Pawn('white')
        self.assertEqual(pawn.color, 'white')

        pawn = Pawn('black')
        self.assertEqual(pawn.color, 'black')

if __name__ == '__main__':
    unittest.main()
