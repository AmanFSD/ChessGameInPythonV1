from King import King
from Board import Board
from BoardLog import BoardLog


class Game:
    def __init__(self):
        self.board = Board()
        self.board.initialize_board()
        self.log = BoardLog()
        self.turn =self.player_setup()
    def switch_turn(self):
        self.turn = 'black' if self.turn == 'white' else 'white'

    def player_setup(self):
        pw = input('Enter White Player Name: ')
        pb = input('Enter Black Player Name: ')
        turn = input('Enter the name of 1st mover: ')
        if turn == pw:
            self.turn = 'white'
            self.is_white = True
        else:
            self.is_white = False
            self.turn = 'black'
        return self.turn

    def is_in_check(self, color):
        king_pos = self.find_king(color)
        for row in range(8):
            for col in range(8):
                piece = self.board.get_piece((row, col))
                if piece and piece.get_color() != color:
                    if piece.is_legit_move((row, col), king_pos, self.board, self.log):
                        return True
        return False

    def is_checkmate(self, color):
        if not self.is_in_check(color):
            return False
        for row in range(8):
            for col in range(8):
                piece = self.board.get_piece((row, col))
                if piece and piece.get_color() == color:
                    for r in range(8):
                        for c in range(8):
                            if piece.is_legit_move((row, col), (r, c), self.board, self.log):
                                original_piece = self.board.get_piece((r, c))
                                self.board.move_piece((row, col), (r, c), piece)
                                if not self.is_in_check(color):
                                    self.board.move_piece((r, c), (row, col), piece)
                                    self.board.set_piece((r, c), original_piece)
                                    return False
                                self.board.move_piece((r, c), (row, col), piece)
                                self.board.set_piece((r, c), original_piece)
        return True

    def find_king(self, color):
        for row in range(8):
            for col in range(8):
                piece = self.board.get_piece((row, col))
                if isinstance(piece,King) and piece.get_color() == color:
                    return (row, col)
        return None

    def move(self, source, dest):
        piece = self.board.get_piece(source)
        if piece and piece.get_color() == self.turn:
            if piece.move(self.board, source, dest, self.log):
                if self.is_in_check(self.turn):
                    print(f"Move places {self.turn} in check! Illegal move.")
                    self.board.move_piece(dest, source, piece)
                    return False
                self.switch_turn()
                return True
            else:
                print("Illegal move!")
        else:
            print("No piece at source or not your turn!")
        return False

    def play(self):
        while True:
            self.board.print_board()
            if self.is_checkmate(self.turn):
                print(f"Checkmate! {self.turn} loses.")
                break
            if self.is_in_check(self.turn):
                print(f"{self.turn} is in check!")
            print(f"{self.turn}'s move")
            source,dest = input("Enter source (e.g., 'e2,e4'): ").strip().split(",")
            source = (8 - int(source[1]), ord(source[0]) - ord('a'))
            dest = (8 - int(dest[1]), ord(dest[0]) - ord('a'))
            self.move(source, dest)


