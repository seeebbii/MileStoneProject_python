import os
updateBoard = [0,1,2,3,4,5,6,7,8]
counter = 0
# FUNCTIONS THAT RUNS THE GAME
def start():
    print("\n\n/****************WELCOME TO TIC TAC TOE****************/\n")
    return input("Please pick a marker 'X' or 'O': ").upper()

def clear():
    os.system("cls")
    #print('\n'*100)

def selectPostion():
    return int(input("Please enter the position number: "))

def display_board(test_board):
    board = ""
    counter = 0
    for i in range(0, len(test_board)):
        if(i == 0):
            board += "\t-------------------------\n"
        board += f"\t|   {test_board[i]}  "
        counter += 1
        if((i + 1) % 3 == 0):
            board += " |"
        if(counter == 3):
            board += '\n'
            board += "\t-------------------------\n"
            counter = 0
    print(board)

turn = None
def player_input():
    position = 0
    global counter, turn
    turn = player1
    while True:
        if(turn == player1):
            print(f"---{turn}'s Turn---")
            position = selectPostion()
            while(position > 8):
                print("0-8: ")
                position = selectPostion()
            while(not place_marker(position,turn)):
                print("Position already assigned!")
                position = selectPostion()
            else:
                if(win_check(updateBoard)):
                    print("CONGRATULATIONS!!!")
                    print(f"--- {turn} is winner ---")
                    break
                else:
                    counter +=1
                    turn = player2
                    if (counter == 9):
                        if (not win_check(updateBoard)):
                            print("!____GAME OVER____!")
                            Replay()
                        else:
                            print("CONGRATULATIONS!!!")
                            print(f"--- {turn} is winner ---")
        if(turn  == player2):
            print(f"---{turn}'s Turn---")
            position = selectPostion()
            while (position > 8):
                print("0-8: ")
                position = selectPostion()
            while (not place_marker(position, turn)):
                print("Position already assigned!")
                position = selectPostion()
            else:
                if (win_check(updateBoard)):
                    print("CONGRATULATIONS!!!")
                    print(f"--- {turn} is winner ---")
                    break
                else:
                    counter += 1
                    turn = player1
                    if (counter == 9):
                        if (not win_check(updateBoard)):
                            print("!____GAME OVER____!")
                            Replay()
                        else:
                            print("CONGRATULATIONS!!!")
                            print(f"--- {turn} is winner ---")

def place_marker(position, turn):
    if type(updateBoard[position]) != str:
        updateBoard[position] = turn
        clear()
        display_board(updateBoard)
        return True
    else:
        return False

def win_check(board):
    if board[0] == board[1] == board[2]:
        return True
    if board[3] == board[4] == board[5]:
        return True
    if board[6] == board[7] == board[8]:
        return True
    if board[0] == board[3] == board[6]:
        return True
    if board[1] == board[4] == board[7]:
        return True
    if board[2] == board[5] == board[8]:
        return True
    if board[0] == board[4] == board[8]:
        return True
    if board[6] == board[4] == board[2]:
        return True
    else:
        return False

def Game():
    global updateBoard
    for i in range(0, 9):
        updateBoard[i] = i
    global player1, player2
    global counter
    counter = 0
    player1 = start()
    player2 = ''
    if (player1 == 'X'):
        player2 = 'O'.upper()
    else:
        player2 = 'X'
    display_board(updateBoard)
    player_input()

def Replay():
    print("Replay option...")
    print("Type YES to play again , else NO: ")
    if(input().lower() == "yes"):
        clear()
        Game()
    else:
        print("Game Ended!")
        return False

# MAIN
player1 = None
player2 = None
Game()
while Replay():
    Replay()