# tic tac toe game

board = [" " for i in range(9)]

def print_board():
    row1 = "|{}|{}|{}|".format(board[0],board[1],board[2])
    row2 = "|{}|{}|{}|".format(board[3],board[4],board[5])
    row3 = "|{}|{}|{}|".format(board[6],board[7],board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

# it should return to the same player if the space is taken
# it's a largr loop including two loops
def player_move(icon):
    while True:
        print("Your turn player",icon)
        choice = int(input("enter your move (1-9):").strip())
        if board[choice-1] == " ":
            board[choice-1] = icon
            break
        else:
            print()
            print("The space is taken!")

# define the condtions of victory
# same icon in a row
# same icon in a column
# two diagonal
def victory(icon):
    if board[0] == board[1] == board[2] == icon \
        or board[3] == board[4] == board[5] == icon \
        or board[6] == board[7] == board[8] == icon \
        or board[0] == board[3] == board[6] == icon \
        or board[1] == board[4] == board[7] == icon \
        or board[2] == board[5] == board[8] == icon \
        or board[0] == board[4] == board[8] == icon \
        or board[2] == board[4] == board[6] == icon:
        return True
    else:
        return False

# when all the space are taken before victory, it's a draw
def draw():
    if " " not in board:
        return True
    else:
        return False

while True:                         # The game is a large loop, repeating
    print_board()                   # 1) show the blank board
    player_move("X")                # 2) player X move
    print_board()                   # 3) show the board after a move
    if victory("X"):
        print("X wins!")
        break
    elif draw():                    
        print("It's a draw!")
        break
    player_move("O")                # 4) player 2 move
    if victory("O"):  
        print("O wins!")
        break                       # 5) break the loop while victory() or draw()
    elif draw():
        print("It's a draw!")
        break

# the game is a large loop including two loops
# 1) player X move
# 2) player O move
# inside the small loops,
# whether the space is taken or not need to be considered
# if the space is taken, the loop returns to the same player and play again
