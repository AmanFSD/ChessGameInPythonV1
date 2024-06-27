class BoardLog:
    def __init__(self):
        self.logs = []
        self.captured_white = []
        self.captured_black = []
        self.promoted = []

    def add_log(self, piece: 'Piece', source: tuple, dest: tuple) -> None:
        self.logs.append([piece, source, dest])

    def has_moved(self, piece: 'Piece') -> bool:
        for log in self.logs:
            if piece == log[0]:
                return True
        return False

    def add_capture(self, piece: 'Piece') -> None:
        if piece.get_color() == 'white':
            self.captured_white.append(piece)
        else:
            self.captured_black.append(piece)

    def add_promotion(self, piece: 'Piece', new_piece: 'Piece', cord: tuple) -> None:
        self.promoted.append([piece, new_piece, cord])
