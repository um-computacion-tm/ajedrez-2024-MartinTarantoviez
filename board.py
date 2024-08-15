from pieces import Rook
class Board:
    def __init__(self):
        self.positions = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        
        self.__positions__[7][7] = Rook("WHITE") #Rook White
        self.__positions__[7][0] = Rook("WHITE") #Rook2 White
        self.__positions__[0][0] = Rook("BLACK")  #Rook Black
        self.__positions__[0][7] = Rook("BLACK")  #Rook2 Black
