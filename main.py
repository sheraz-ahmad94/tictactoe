board = ["_"] * 9 # not actually prints it. but we just define a list of 9 elements with _ in them

def print_board():
    count = 0
    for i in range(3):
        print(f"|{board[count]}|{board[count+1]}|{board[count+2]}|")
        count += 3
        # it's a for loop. which runs from 1 - 3. it will print first roww

def win_condition(board):
    
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == 'X':
            return True
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == 'O':
            return True
    count = 0
    
    for i in range(3):
        if board[i+count] == board[i+1+count] == board[i+2+count] == "X":
            return True
        count += 2

    count = 0
    for i in range(3):
        if board[i+count] == board[i+1+count] == board[i+2+count] == "O":
            return True
        count += 2

    if board[0] == board[4] == board[8] == 'X' or board[2] == board[4] == board[6] == 'X':
        return True
    
    if board[0] == board[4] == board[8] == 'O' or board[2] == board[4] == board[6] == 'O':
        return True
    
count = 0
moves = 9
while moves > 0:
        
    print_board() # printing the board once.. empty rn
    while True: # this while loop is to check for a valid input... like if the user enters some other number than 1 - 9, 
        #it will display error or a number which has already been entered
        player1 = int(input("Player 1 Turn (X): "))
        if 1 <= player1 <= 9 and board[player1-1] == "_":
            break
        else:
            print("Wrong Input. Enter Again!")
            
    board[player1-1] = 'X' # when user has entered a valid input, loop will break and that input will be stored in board.
    moves -= 1
    
    if moves == 0:
        break
    
    if win_condition(board):
        print_board()
        print("Player 1 Wins!")
        break
    
    print_board() # and we print the board
    
    while True:
        player2 = int(input("Player 2 Turn (O): "))
        if 1 <= player2 <= 9 and board[player2-1] == "_":
            break
        else:
            print("Wrong Input. Enter Again!")
    
    board[player2-1] = 'O'
    moves -= 1
    
    if win_condition(board):
        print_board()
        print("Player 2 Wins!")
        break
    print("moves = " + str(moves))

if moves == 0:
    print_board()
    print("DRAW!")