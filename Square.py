from Piece import Piece


class Square:
    def __init__(self):
        self.__piece = None
        self.color = None

    def is_empty(self) -> bool:
        return self.__piece is None

    def set_piece(self, piece: 'Piece') -> None:
        if isinstance(piece, Piece) or piece is None:
            self.__piece = piece
        else:
            raise ValueError("Invalid piece type")

    def get_piece(self) -> 'Piece':
        return self.__piece

    def remove_piece(self) -> None:
        self.__piece = None

    def __str__(self) -> str:
        return f"Square(color={self.color}, piece={self.__piece})"

    def __repr__(self) -> str:
        return self.__str__()