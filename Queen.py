from Piece import Piece


class Queen(Piece):
    def __init__(self, color: str, url: str):
        super().__init__(color, url)

    def is_legit_move(self, source: tuple, dest: tuple, board: 'Board', log: 'BoardLog') -> bool:
        board = board.board
        y1, x1 = source
        y2, x2 = dest
        step_y = 0
        step_x = 0

        if x2 > x1:
            step_x = 1
        elif x1 > x2:
            step_x = -1

        if y2 > y1:
            step_y = 1
        elif y1 > y2:
            step_y = -1

        check_x = x1 + step_x
        check_y = y1 + step_y

        if (x1 - x2 != 0 and y1 - y2 == 0) or (x1 - x2 == 0 and y1 - y2 != 0) or (abs(x2 - x1) == abs(y2 - y1)):
            while check_x != x2 or check_y != y2:
                if not board[check_y][check_x].is_empty():
                    return False
                check_x += step_x
                check_y += step_y

            if not board[y2][x2].is_empty():
                if board[y2][x2].get_piece().get_color() == self.get_color():
                    return False
                else:
                    log.add_capture(piece=board[y2][x2].get_piece())
            return True
        return False

    def __str__(self) -> str:
        return f'{self.get_color()[0]}Q'

