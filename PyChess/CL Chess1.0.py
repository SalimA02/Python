class ChessGame:
    def __init__(self):
        self.board = self.initialize_board()
        self.current_turn = 'white'

    def initialize_board(self):
        # Initialize an 8x8 grid with pawns in the second and seventh rows
        board = []
        for i in range(8):
            row = []
            for j in range(8):
                if i == 1:
                    row.append('wp')  # White pawn
                elif i == 6:
                    row.append('bp')  # Black pawn
                elif i == 0:
                    if j in [0, 7]:
                        row.append('wr')  # White rook
                    elif j in [1, 6]:
                        row.append('wn')  # White knight
                    elif j in [2, 5]:
                        row.append('wb')  # White bishop
                    elif j == 3:
                        row.append('wq')  # White queen
                    elif j == 4:
                        row.append('wk')  # White king
                elif i == 7:
                    if j in [0, 7]:
                        row.append('br')  # Black rook
                    elif j in [1, 6]:
                        row.append('bn')  # Black knight
                    elif j in [2, 5]:
                        row.append('bb')  # Black bishop
                    elif j == 3:
                        row.append('bq')  # Black queen
                    elif j == 4:
                        row.append('bk')  # Black king
                else:
                    row.append('--')  # Empty square
            board.append(row)
        return board

    def print_board(self):
        print('  a | b | c | d | e | f | g | h')
        print('-' * 34)
        for i in range(8):
            print(i + 1, end=' ')
            for j in range(8):
                print(self.board[i][j], end=' | ')
            print()
            print('-' * 34)

    def is_valid_move(self, start, end):
        start_x, start_y = ord(start[0]) - 97, int(start[1]) - 1
        end_x, end_y = ord(end[0]) - 97, int(end[1]) - 1
        piece = self.board[start_y][start_x]

        if piece[0] != self.current_turn[0]:  # Check if the piece belongs to the current player
            return False

        if piece[1] == 'p':  # Pawn
            if piece[0] == 'w':  # White pawn
                if start_y == 1 and end_y == 3 and self.board[2][start_x] == '--' and self.board[3][start_x] == '--':
                    return True
                elif start_y + 1 == end_y and start_x == end_x and self.board[end_y][end_x] == '--':
                    return True
                elif start_y + 1 == end_y and abs(start_x - end_x) == 1 and self.board[end_y][end_x] != '--' and self.board[end_y][end_x][0] == 'b':
                    return True
            else:  # Black pawn
                if start_y == 6 and end_y == 4 and self.board[5][start_x] == '--' and self.board[4][start_x] == '--':
                    return True
                elif start_y - 1 == end_y and start_x == end_x and self.board[end_y][end_x] == '--':
                    return True
                elif start_y - 1 == end_y and abs(start_x - end_x) == 1 and self.board[end_y][end_x] != '--' and self.board[end_y][end_x][0] == 'w':
                    return True
        elif piece[1] == 'r':  # Rook
            if start_x == end_x:  # Move up/down
                step = 1 if end_y > start_y else -1
                for i in range(start_y + step, end_y, step):
                    if self.board[i][start_x] != '--':
                        return False
                return True
            elif start_y == end_y:  # Move left/right
                step = 1 if end_x > start_x else -1
                for i in range(start_x + step, end_x, step):
                    if self.board[start_y][i] != '--':
                        return False
                return True
        elif piece[1] == 'n':  # Knight
            if abs(start_x - end_x) == 1 and abs(start_y - end_y) == 2:
                return True
            elif abs(start_x - end_x) == 2 and abs(start_y - end_y) == 1:
                return True
        elif piece[1] == 'b':  # Bishop
            if abs(start_x - end_x) == abs(start_y - end_y):
                step_x = 1 if end_x > start_x else -1
                step_y = 1 if end_y > start_y else -1
                for i in range(1, abs(start_x - end_x)):
                    if self.board[start_y + i * step_y][start_x + i * step_x] != '--':
                        return False
                return True
        elif piece[1] == 'q':  # Queen
            if start_x == end_x:  # Move up/down
                step = 1 if end_y > start_y else -1
                for i in range(start_y + step, end_y, step):
                    if self.board[i][start_x] != '--':
                        return False
                return True
            elif start_y == end_y:  # Move left/right
                step = 1 if end_x > start_x else -1
                for i in range(start_x + step, end_x, step):
                    if self.board[start_y][i] != '--':
                        return False
                return True
            elif abs(start_x - end_x) == abs(start_y - end_y):
                step_x = 1 if end_x > start_x else -1
                step_y = 1 if end_y > start_y else -1
                for i in range(1, abs(start_x - end_x)):
                    if self.board[start_y + i * step_y][start_x + i * step_x] != '--':
                        return False
                return True
        elif piece[1] == 'k':  # King
            if abs(start_x - end_x) <= 1 and abs(start_y - end_y) <= 1:
                return True
        return False

    def make_move(self, start, end):
        start_x, start_y = ord(start[0]) - 97, int(start[1]) - 1
        end_x, end_y = ord(end[0]) - 97, int(end[1]) - 1
        piece = self.board[start_y][start_x]
        self.board[end_y][end_x] = piece
        self.board[start_y][start_x] = '--'

    def play(self):
        while True:
            self.print_board()
            print(f"Current turn: {self.current_turn}")
            start = input("Enter the position of the piece to move (e.g. a2): ")
            end = input("Enter the position to move to (e.g. a3): ")
            if self.is_valid_move(start, end):
                self.make_move(start, end)
                self.current_turn = 'black' if self.current_turn == 'white' else 'white'
            else:
                print("Invalid move. Please try again.")

game = ChessGame()
game.play()