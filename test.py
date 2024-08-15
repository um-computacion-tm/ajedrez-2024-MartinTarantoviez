import unittest
from board import Board,Rook
class TestBoard(unittest.TestCase):
    
    def test_initial_positions(self):
        board = Board()

        # Verificar las posiciones iniciales de las torres
        self.assertIsInstance(board.positions[7][7], Rook)
        self.assertIsInstance(board.positions[7][0], Rook)
        self.assertIsInstance(board.positions[0][0], Rook)
        self.assertIsInstance(board.positions[0][7], Rook)

        # Verificar los colores de las torres
        self.assertEqual(board.positions[7][7].color, "WHITE")
        self.assertEqual(board.positions[7][0].color, "WHITE")
        self.assertEqual(board.positions[0][0].color, "BLACK")
        self.assertEqual(board.positions[0][7].color, "BLACK")

        # Verificar que el resto de las posiciones estén vacías
        for i in range(8):
            for j in range(8):
                if (i, j) not in [(7, 7), (7, 0), (0, 0), (0, 7)]:
                    self.assertIsNone(board.positions[i][j])

if __name__ == '__main__':
    unittest.main()
