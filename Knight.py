from Piece import Piece


class Knight(Piece):
    def __init__(self, color: str, url: str):
        super().__init__(color, url)

    def is_legit_move(self, source: tuple, dest: tuple, board: 'Board', log: 'BoardLog') -> bool:
        y1, x1 = source
        y2, x2 = dest
        if (abs(x1 - x2) == 2 and abs(y1 - y2) == 1) or (abs(x1 - x2) == 1 and abs(y1 - y2) == 2):
            if not board.board[y2][x2].is_empty():
                if board.board[y2][x2].get_piece().get_color() == self.get_color():
                    return False
                else:
                    log.add_capture(piece=board.board[y2][x2].get_piece())
            return True
        return False

    def __str__(self) -> str:
        return f'{self.get_color()[0]}N'


