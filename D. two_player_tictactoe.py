from time import sleep
import os,time
board = [" " for i in range(9)]

def print_board():
    row1 = ("|{}|{}|{}|".format(board[0],board[1],board[2]))
    row2 = ("|{}|{}|{}|".format(board[3],board[4],board[5]))
    row3 = ("|{}|{}|{}|".format(board[6],board[7],board[8]))
    os.system("cls")
    print("{}\n{}\n{}\n".format(row1,row2,row3))

def player_move(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2
    print("Player 1 is X | Player 2 is O")    
    print("Your turn player {}".format(number))
    choice = int(input("Enter your move (1-9): ").strip())
    if board[choice-1] == " ":
        board[choice-1] = icon
    else:
        print("That space is taken. \n Please try again.")
        sleep(3)
        os.system("cls")
        print_board()
        player_move(icon)
    
def isVictory(icon):
    for i in range(9):
        if (board[i] == icon and board[i+1] == icon and board[i+2] == icon)or\
           (board[i] == icon and board[i+3] == icon and board[i+6] == icon)or\
           (board[i] == icon and board[i+4] == icon and board[i+8] == icon)or\
           (board[i+2] == icon and board[i+4] == icon and board[i+6] == icon):
            return True
        else:
            return False

def isDraw():
    if " " not in board:
        return True
    else:
        return False
    
# Game Loop
# player 1 has X and player 2 has O

while True:
    print_board()
    player_move("X")
    print_board()
    if isVictory("X"):
        print("Player 1 Wins! ")
        sleep(3)
        break
    elif isDraw():
        print("Its a Draw")
        sleep(3)
        break
    player_move("O")
    if isVictory("O"):
        print_board()
        print("Player 2 Wins! ")
        sleep(3)
        break
    elif isDraw():
        print("Its a Draw")
        sleep(3)
        break
