from board import Board

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"
        
    def move(
        from_row,
        from_col,
        to_row,
        to_col,
    ):
        piece = self.board.get
        self.change_turn()
        
    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"