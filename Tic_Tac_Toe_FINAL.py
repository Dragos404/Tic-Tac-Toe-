import sys, random

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
        if user_input.lower() == "QUIT".lower():
            return sys.exit(f"Thank you for the game, {player}!")
        elif user_input not in moves:
            print(f' {user_input} - Not a valid move. Try again!')
        else:
            row, col = colum_id[user_input[0]], int(user_input[1]) - 1
            if user_input in moves and board[row][col] == '.':
                mark(board,player,row,col)
                break
            else:
                print(f'{user_input} - Cel already taken! Try again!')  
        

def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    while True:
        random_row = random.randint(0, 2)
        random_col = random.randint(0, 2)
        if board[random_row][random_col] == ".":
            mark(board,player,random_row,random_col)
            break
    

def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    if board[row][col] == ".":
        board[row][col] = player
        print_board(board)
    return True


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


def is_full(board): #andrei
    """Returns True if board is full."""
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == ".":
                return False
    return True


def print_board(board): #andrei
    print("\n    1   2   3 \n")
    print("A   " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("   ---+---+---")
    print("B   " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("   ---+---+---")
    print("C   " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + "\n")
    

def print_result(winner): #andrei
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    if winner == "X":
        print("Congratulations, player X won!")
    elif winner == "O":
        print("Congratulations,player O won!")
    else:
        print("It's Tie!")
    sys.exit()
   

def tictactoe_game(mode):
    player = "X"
    who_play = 0
    board = init_board()
    print_board(board)
    while True:
        if mode.split("-")[who_play] == "HUMAN":
            get_move(board, player)
        if mode.split("-")[who_play] == "AI":
            get_ai_move(board, player)
        if has_won(board, player):
            print_result(player)
        if is_full(board):
            print_result("")
        if player == "X": 
            player = "O"
        else:
            player = "X"
        
        if who_play == 1:
            who_play = 0
        else:
            who_play = 1


def main_menu():
    print("Welcome to Tic-Tac-Toe...")
    print("Press 1 for Human - Human ")
    print("Press 2 for Human - AI")
    user_input = input("Please choose your mode: ")
    valid_input = ["1", "2"]
    print("""
    

                 _   _      _             _             
                | | (_)    | |           | |            
                | |_ _  ___| |_ __ _  ___| |_ ___   ___ 
                | __| |/ __| __/ _` |/ __| __/ _ \ / _ \
                                                        
                | |_| | (__| || (_| | (__| || (_) |  __/
                 \__|_|\___|\__\__,_|\___|\__\___/ \___|


    1. Must insert a valid coordonate for your move : A1, A2, A3, B1, B2, B3, C1, C2, C3
    2. If you want to Quit the game, just press Quit to console

                                Play safe! 
                           Dont try this at home!
    """)
    while user_input not in valid_input:
        user_input = input("Invalid input, please try again! ")
    if user_input == "1":
        tictactoe_game('HUMAN-HUMAN')
    elif user_input == "2":
        tictactoe_game('HUMAN-AI')


if __name__ == '__main__':
    main_menu()
