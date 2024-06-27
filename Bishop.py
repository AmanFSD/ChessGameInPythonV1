from Piece import Piece


class Bishop(Piece):
    def __init__(self, color, url):
        super().__init__(color, url)

    def is_legit_move(self, source, dest, board, log):
        board = board.board
        y1, x1 = source
        y2, x2 = dest
        step_x = 0
        step_y = 0
        if x2 > x1:
            step_x = 1
        elif x1 > x2:
            step_x = -1
        else:
            step_x = 0

        if y2 > y1:
            step_y = 1
        elif y1 > y2:
            step_y = -1
        else:
            step_y = 0
        check_x = x1 + step_x
        check_y = y1 + step_y
        if abs(x2 - x1) == abs(y2 - y1):
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

    def __str__(self):
        return f'{self.get_color()[0]}B'

