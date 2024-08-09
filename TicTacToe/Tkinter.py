# Initialize the game board as a list of 9 empty spaces
board = [' ' for _ in range(9)]

# Function to draw the game board
def draw_board():
    # Create each row of the board using string formatting
    row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
    row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
    row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])

    # Print the board with empty lines before and after
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

# Function to handle player moves
def player_move(icon):
    # Determine which player's turn it is based on the icon
    if icon == 'X':
        number = 1
    elif icon == 'O':
        number = 2

    # Print whose turn it is
    print("Your turn player {}".format(number))

    # Get the player's move
    choice = int(input("Enter your move (1-9): ").strip())

    # Check if the chosen space is empty
    if board[choice - 1] == ' ':
        # If it is, place the player's icon there
        board[choice - 1] = icon
    else:
        # If it's not, print an error message
        print()
        print("That space is taken!")

# Function to check if a player has won
def is_victory(icon):
    # Check all possible winning combinations
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
        (board[3] == icon and board[4] == icon and board[5] == icon) or \
        (board[6] == icon and board[7] == icon and board[8] == icon) or \
        (board[0] == icon and board[3] == icon and board[6] == icon) or \
        (board[1] == icon and board[4] == icon and board[7] == icon) or \
        (board[2] == icon and board[5] == icon and board[8] == icon) or \
        (board[0] == icon and board[4] == icon and board[8] == icon) or \
        (board[2] == icon and board[4] == icon and board[6] == icon):
        # If any combination is true, return True
        return True
    else:
        # If none are true, return False
        return False

# Function to check if the game is a draw
def is_draw():
    # Check if there are any empty spaces left on the board
    if ' ' not in board:
        # If not, return True
        return True
    else:
        # If there are, return False
        return False

# Main game loop
while True:
    # Draw the initial board
    draw_board()

    # Handle player 1's move
    player_move('X')

    # Draw the updated board
    draw_board()

    # Check if player 1 has won
    if is_victory('X'):
        # If they have, print a victory message and break out of the loop
        print("Player 1 wins! Congratulations!")
        break
    # Check if the game is a draw
    elif is_draw():
        # If it is, print a draw message and break out of the loop
        print("It's a draw!")
        break

    # Handle player 2's move
    player_move('O')

    # Check if player 2 has won
    if is_victory('O'):
        # If they have, print a victory message and break out of the loop
        print("Player 2 wins! Congratulations!")
        break