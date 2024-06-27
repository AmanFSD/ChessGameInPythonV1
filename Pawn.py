from Piece import Piece
from Queen import Queen
from Rook import Rook
from Knight import Knight
from Bishop import Bishop

class Pawn(Piece):
    def __init__(self, color: str, url: str):
        super().__init__(color, url)

    def is_legit_move(self, source: tuple, dest: tuple, board: 'Board', log: 'BoardLog') -> bool:
        y1, x1 = source
        y2, x2 = dest
        direction = -1 if self.get_color() == 'white' else 1
        start_row = 6 if self.get_color() == 'white' else 1
        end_row = 0 if self.get_color() == 'white' else 7

        # Forward move
        if x1 == x2:
            # Single step forward
            if y2 == y1 + direction and board.board[y2][x2].is_empty():
                if y2 == end_row:
                    self.promote(source, dest, board, log)
                return True
            # Double step from start row
            if y1 == start_row and y2 == y1 + 2 * direction and board.board[y2][x2].is_empty() and \
                    board.board[y1 + direction][x1].is_empty():
                return True

        # Captures
        if abs(x2 - x1) == 1 and y2 == y1 + direction:
            if not board.board[y2][x2].is_empty() and board.board[y2][
                x2].get_piece().get_color() != self.get_color():
                if y2 == end_row:
                    self.promote(source, dest, board, log)
                return True

        return False

    def promote(self, source: tuple, dest: tuple, board: 'Board', log: 'BoardLog') -> None:
        # Automatic promotion to a queen for simplicity, adjust as needed
        promotion_piece = Queen(color=self.get_color(), url=f'images/{self.get_color()}-queen.png')
        board.set_piece(dest, promotion_piece)
        log.add_promotion(self, promotion_piece, dest)

    def can_be_promoted(self, dest: tuple, board: 'Board', log: 'BoardLog') -> bool:
        y, x = dest
        if (y == 7 and self.get_color() == 'black') or (y == 0 and self.get_color() == 'white'):
            piece_choice = input('Enter Piece Choice: ')
            if piece_choice == 'queen':
                p = Queen(color=self.get_color(), url=f'images/{self.get_color()}-queen.png')
            elif piece_choice == 'knight':
                p = Knight(color=self.get_color(), url=f'images/{self.get_color()}-knight.png')
            elif piece_choice == 'bishop':
                p = Bishop(color=self.get_color(), url=f'images/{self.get_color()}-bishop.png')
            elif piece_choice == 'rook':
                p = Rook(color=self.get_color(), url=f'images/{self.get_color()}-rook.png')
            else:
                return False
            log.add_promotion(piece=board[y][x].get_piece(), cord=dest, new_piece=p)
            return p
        return False

    def can_en_passent(self) -> bool:
        # Implement en passant logic here
        pass

    def __str__(self) -> str:
        return f'{self.get_color()[0]}P'

