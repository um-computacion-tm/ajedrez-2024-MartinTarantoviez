import unittest
from pieces import Piece,Rook,Pawn

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
