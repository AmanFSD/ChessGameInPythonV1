class Piece:
    def __init__(self, color: str, url: str):
        self.__color = color
        self.url = url

    def get_color(self) -> str:
        return self.__color

    def is_legit_move(self, board: 'Board', source: tuple, dest: tuple, log: 'BoardLog') -> bool:
        pass

    def move(self, board: 'Board', source: tuple, dest: tuple, log: 'BoardLog') -> bool:
        r_obj = self.is_legit_move(board=board, source=source, dest=dest, log=log)
        typ = type(r_obj)
        if typ == bool and r_obj is True:
            log.add_log(source=source, dest=dest, piece=self)
            board.move_piece(start=source, stop=dest, piece=self)
            return True
        elif typ in [Queen, Bishop, Knight, Rook]:
            log.add_log(source=source, dest=dest, piece=self)
            board.move_piece(start=source, stop=dest, piece=r_obj)
            return True
        return False

    def __str__(self) -> str:
        return f"Piece(color={self.__color}, url={self.url})"
