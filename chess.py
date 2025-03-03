# Chess Game (Text-based)
class ChessPiece:
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def __str__(self):
        return f"{self.color[0].upper()}{self.name[0].upper()}"


class ChessBoard:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        board = [[None for _ in range(8)] for _ in range(8)]

        # Place white pieces
        board[0][0] = board[0][7] = ChessPiece("white", "rook")
        board[0][1] = board[0][6] = ChessPiece("white", "knight")
        board[0][2] = board[0][5] = ChessPiece("white", "bishop")
        board[0][3] = ChessPiece("white", "queen")
        board[0][4] = ChessPiece("white", "king")
        for i in range(8):
            board[1][i] = ChessPiece("white", "pawn")

        # Place black pieces
        board[7][0] = board[7][7] = ChessPiece("black", "rook")
        board[7][1] = board[7][6] = ChessPiece("black", "knight")
        board[7][2] = board[7][5] = ChessPiece("black", "bishop")
        board[7][3] = ChessPiece("black", "queen")
        board[7][4] = ChessPiece("black", "king")
        for i in range(8):
            board[6][i] = ChessPiece("black", "pawn")

        return board

    def print_board(self):
        for row in self.board:
            print(" | ".join([str(piece) if piece else "  " for piece in row]))
            print("-" * 33)

    def is_valid_move(self, start, end, color):
        start_row, start_col = start
        end_row, end_col = end

        # Ensure it's within bounds
        if not (0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8):
            return False

        # Ensure the piece is of the correct color
        piece = self.board[start_row][start_col]
        if not piece or piece.color != color:
            return False

        # Basic validation: you can improve with specific movement rules
        return True

    def move_piece(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        self.board[end_row][end_col] = self.board[start_row][start_col]
        self.board[start_row][start_col] = None

    def is_check(self, color):
        # Placeholder for check detection logic
        # Check for check situations (we would check if the king is under threat)
        return False

    def is_checkmate(self, color):
        # Placeholder for checkmate detection logic
        # Check if the king is in checkmate
        return False


def get_move():
    """Prompts for a move in standard algebraic notation (e.g., 'e2 e4')."""
    while True:
        move = input("Enter your move (e.g., 'e2 e4'): ").strip().lower()
        try:
            start_pos, end_pos = move.split()
            start_row, start_col = 8 - int(start_pos[1]), ord(start_pos[0]) - ord('a')
            end_row, end_col = 8 - int(end_pos[1]), ord(end_pos[0]) - ord('a')
            return (start_row, start_col), (end_row, end_col)
        except ValueError:
            print("Invalid move. Please use algebraic notation, e.g., 'e2 e4'.")
            continue


def play_game():
    chess_board = ChessBoard()
    current_player = "white"
    
    while True:
        chess_board.print_board()
        print(f"{current_player.capitalize()}'s turn")

        # Get and validate the move
        start, end = get_move()

        if chess_board.is_valid_move(start, end, current_player):
            chess_board.move_piece(start, end)

            # Check for checkmate or check
            if chess_board.is_checkmate(current_player):
                print(f"{current_player.capitalize()} is in checkmate! Game over.")
                break
            elif chess_board.is_check(current_player):
                print(f"{current_player.capitalize()} is in check!")

            # Switch player turn
            current_player = "black" if current_player == "white" else "white"
        else:
            print("Invalid move. Please try again.")


if __name__ == "__main__":
    play_game()
