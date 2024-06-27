# Chess Game In Python Repository

This repository contains the test code for a chess game implementation in Python. The code includes classes representing different chess pieces, a board, and the game logic.

## Classes Overview

### `Square`

Represents a square on the chessboard.

- **Attributes:**
  - `__piece`: The piece currently on the square (if any).
  - `color`: The color of the square.

- **Methods:**
  - `is_empty() -> bool`: Checks if the square is empty.
  - `set_piece(piece: 'Piece') -> None`: Places a piece on the square.
  - `get_piece() -> 'Piece'`: Returns the piece on the square.
  - `remove_piece() -> None`: Removes the piece from the square.
  - `__str__() -> str`: Returns a string representation of the square.
  - `__repr__() -> str`: Returns a string representation of the square.

### `BoardLog`

Logs the moves and captures in the game.

- **Attributes:**
  - `logs`: A list of moves made in the game.
  - `captured_white`: A list of white pieces captured.
  - `captured_black`: A list of black pieces captured.
  - `promoted`: A list of pieces that have been promoted.

- **Methods:**
  - `add_log(piece: 'Piece', source: tuple, dest: tuple) -> None`: Logs a move.
  - `has_moved(piece: 'Piece') -> bool`: Checks if a piece has moved.
  - `add_capture(piece: 'Piece') -> None`: Logs a captured piece.
  - `add_promotion(piece: 'Piece', new_piece: 'Piece', cord: tuple) -> None`: Logs a promotion.

### `Piece`

Base class for all chess pieces.

- **Attributes:**
  - `__color`: The color of the piece.
  - `url`: The URL of the piece's image.

- **Methods:**
  - `get_color() -> str`: Returns the color of the piece.
  - `is_legit_move(board: 'Board', source: tuple, dest: tuple, log: 'BoardLog') -> bool`: Checks if a move is legal.
  - `move(board: 'Board', source: tuple, dest: tuple, log: 'BoardLog') -> bool`: Moves the piece.
  - `__str__() -> str`: Returns a string representation of the piece.

### `Pawn`

Represents a pawn piece.

- **Methods:**
  - `is_legit_move(source: tuple, dest: tuple, board: 'Board', log: 'BoardLog') -> bool`: Checks if a move is legal.
  - `promote(source: tuple, dest: tuple, board: 'Board', log: 'BoardLog') -> None`: Promotes the pawn.
  - `can_be_promoted(dest: tuple, board: 'Board', log: 'BoardLog') -> bool`: Checks if the pawn can be promoted.
  - `can_en_passent() -> bool`: Checks if the pawn can perform en passant.
  - `__str__() -> str`: Returns a string representation of the pawn.

### `Knight`

Represents a knight piece.

- **Methods:**
  - `is_legit_move(source: tuple, dest: tuple, board: 'Board', log: 'BoardLog') -> bool`: Checks if a move is legal.
  - `__str__() -> str`: Returns a string representation of the knight.

### `Rook`

Represents a rook piece.

- **Methods:**
  - `is_legit_move(source: tuple, dest: tuple, board: 'Board', log: 'BoardLog') -> bool`: Checks if a move is legal.
  - `__str__() -> str`: Returns a string representation of the rook.

### `Bishop`

Represents a bishop piece.

- **Methods:**
  - `is_legit_move(source: tuple, dest: tuple, board: 'Board', log: 'BoardLog') -> bool`: Checks if a move is legal.
  - `__str__() -> str`: Returns a string representation of the bishop.

### `Queen`

Represents a queen piece.

- **Methods:**
  - `is_legit_move(source: tuple, dest: tuple, board: 'Board', log: 'BoardLog') -> bool`: Checks if a move is legal.
  - `__str__() -> str`: Returns a string representation of the queen.

### `King`

Represents a king piece.

- **Methods:**
  - `is_legit_move(source: tuple, dest: tuple, board: 'Board', log: 'BoardLog') -> bool`: Checks if a move is legal.
  - `can_castle() -> bool`: Checks if the king can castle.
  - `__str__() -> str`: Returns a string representation of the king.

## Usage

Clone the repository and run the Python scripts to test the chess game implementation. Ensure you have the necessary dependencies installed.

```bash
git clone <https://github.com/AmanFSD/ChessGameInPythonV1.git>
cd <ChessGameInPythonV1>
python main.py
