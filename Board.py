from Bishop import Bishop
from King import King
from Knight import Knight
from Pawn import Pawn
from Queen import Queen
from Rook import Rook
from Square import Square


class Board:
    def __init__(self):
        self.board = [[Square() for _ in range(8)] for _ in range(8)]

    def initialize_board(self):
        for x in range(8):
            for y in range(8):
                self.board[x][y].set_piece(None)

        for i in range(8):
            b_pawn = Pawn(color='black', url='images/black-pawn.png')
            w_pawn = Pawn(color='white', url='images/white-pawn.png')

            self.board[1][i].set_piece(b_pawn)
            self.board[6][i].set_piece(w_pawn)

        b_rook1 = Rook(color='black', url='images/black-rook.png')
        b_rook2 = Rook(color='black', url='images/black-rook.png')
        w_rook1 = Rook(color='white', url='images/white-rook.png')
        w_rook2 = Rook(color='white', url='images/white-rook.png')

        self.board[0][0].set_piece(b_rook1)
        self.board[0][7].set_piece(b_rook2)
        self.board[7][0].set_piece(w_rook1)
        self.board[7][7].set_piece(w_rook2)

        b_bishop1 = Bishop(color='black', url='images/black-bishop.png')
        b_bishop2 = Bishop(color='black', url='images/black-bishop.png')
        w_bishop1 = Bishop(color='white', url='images/white-bishop.png')
        w_bishop2 = Bishop(color='white', url='images/white-bishop.png')

        self.board[0][2].set_piece(b_bishop1)
        self.board[0][5].set_piece(b_bishop2)
        self.board[7][2].set_piece(w_bishop1)
        self.board[7][5].set_piece(w_bishop2)

        b_knight1 = Knight(color='black', url='images/black-knight.png')
        b_knight2 = Knight(color='black', url='images/black-knight.png')
        w_knight1 = Knight(color='white', url='images/white-knight.png')
        w_knight2 = Knight(color='white', url='images/white-knight.png')

        self.board[0][1].set_piece(b_knight1)
        self.board[0][6].set_piece(b_knight2)
        self.board[7][1].set_piece(w_knight1)
        self.board[7][6].set_piece(w_knight2)

        b_queen = Queen(color='black', url='images/black-queen.png')
        w_queen = Queen(color='white', url='images/white-queen.png')

        self.board[0][3].set_piece(b_queen)
        self.board[7][3].set_piece(w_queen)

        b_king = King(color='black', url='images/black-king.png')
        w_king = King(color='white', url='images/white-king.png')

        self.board[0][4].set_piece(b_king)
        self.board[7][4].set_piece(w_king)
        return w_king, b_king

    def print_board(self):
        print('  -', end='')
        print('+---+' * 8)
        for x in range(8):
            print(8 - x, end=' ')
            print('| ', end='')
            for y in range(8):
                if self.board[x][y].get_piece() is None:
                    print('  ', end=' | ')
                else:
                    print(self.board[x][y].get_piece(), end=' | ')
            print()
            print('  -', end='')
            print('+---+' * 8)
        print('    a    b    c    d    e    f    g    h')

    def move_piece(self, start, stop, piece):
        x1, y1 = start
        x2, y2 = stop
        self.board[x1][y1].set_piece(None)
        self.board[x2][y2].set_piece(piece)

    def get_piece(self, cord):
        x, y = cord
        return self.board[x][y].get_piece()

    def has_piece(self, cord, piece):
        x, y = cord
        return self.board[x][y].get_piece() == piece

    def set_piece(self, cord, piece):
        x, y = cord
        self.board[x][y].set_piece(piece)


