import sys

def init_board(): 
    """Returns an empty 3-by-3 board (with .)."""
    board = [
    [ '.','.','.' ],
    [ '.','.','.' ],
    [ '.','.','.' ]
    ]
    return board


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    colum_id = { "a": 0, "b": 1, "c": 2 }
    moves = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
    while True:  
        user_input = input(f"{player}, please make your move: ").lower()
        if user_input not in moves:
            print(f' {user_input} - Not a valid move. Try again!')
        else:
            user_input == colum_id[user_input[0]], int(user_input[1]) - 1
            print(board)1
        

def mark(board, player, row, col):
    if board[row][col] == ".":
        board[row][col] = player
        print_board(board)
    elif board[row][col] == "X" or "O":
        print('Cel already taken! Try again!') 
    return board


def quit(player):
     if user_input.lower() == "QUIT".lower():
         return sys.exit(f"Thank you for the game, {player}!")


def has_won(board, player):
    """Returns True if player has won the game."""
    a1 = board[0][0]
    a2 = board[0][1]
    a3 = board[0][2]
    b1 = board[1][0]
    b2 = board[1][1]
    b3 = board[1][2]
    c1 = board[2][0]
    c2 = board[2][1]
    c3 = board[2][2]
    win_player = [player, player, player]
    win_list = [[a1, a2, a3], [b1, b2, b3], [c1, c2, c3], [a1, b1, c1], [a2, b2, c2], [a3, b3, c3], [a1, b2, c3], [a3, b2, c1]]

    for element in win_list:
        if element == win_player:
            return True
    return False

