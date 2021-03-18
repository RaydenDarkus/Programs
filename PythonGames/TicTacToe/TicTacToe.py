board = ["-","-","-","-","-","-","-","-","-"]

game_still_going = True
winner = None
current_player = "X"

def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2] + "  1|2|3")
    print(board[3] + "|" + board[4] + "|" + board[5] + "  4|5|6")
    print(board[6] + "|" + board[7] + "|" + board[8] + "  7|8|9")

def play_game():
    display_board()
    while game_still_going:
        handle_turn(current_player)
        check_game_over()
        flip_player()
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")

def handle_turn(player):
    print(player + " 's turn.")
    position = input("Choose a position from 1-9: ")
    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Invalid Input. Choose a position from 1-9: ")
        position = int(position) - 1
        if board[position]== "-":
            valid = True
        else:
            print("You can't fo there. Go again.")
    board[position] = player
    display_board()

def check_game_over():
    check_for_winner()
    check_for_tie()

def check_for_winner():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

def check_rows():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] !="-" 
    row_2 = board[3] == board[4] == board[5] !="-"
    row_3 = board[6] == board[7] == board[8] !="-"
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]   
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None

def check_columns():
    global game_still_going
    col_1 = board[0] == board[3] == board[6] !="-" 
    col_2 = board[1] == board[4] == board[7] !="-"
    col_3 = board[2] == board[5] == board[8] !="-"
    if col_1 or col_2 or col_3:
        game_still_going = False
    if col_1:
        return board[0]   
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    else:
        return None

def check_diagonals():
    global game_still_going
    dia_1 = board[0] == board[4] == board[8] !="-" 
    dia_2 = board[6] == board[4] == board[2] !="-"
    if dia_1 or dia_2:
        game_still_going = False
    if dia_1:
        return board[0]   
    elif dia_2:
        return board[6]
    else:
        return None

def check_for_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
        return True
    else:
        return False

def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"

play_game()
