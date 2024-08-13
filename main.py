from chess import Chess
def main ():
        chess = Chess()

        try:
            from_row = int(input("From row : "))

            from_col = int(input("From column: "))

            to_row = int(input("TO row: "))

            to_col  =  int(input("to column : "))
            chess.move(
                from_row,
                 from_col,
                 to_col,
                 to_row,
            )
        except Exception as e:
            print("Error")

