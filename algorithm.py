sudoku_board = [
    [0,2,3,0,7,0,6,8,0],
    [0,8,0,0,0,0,0,0,4],
    [7,4,0,5,0,0,0,0,9],
    [0,0,0,0,1,0,0,0,0],
    [9,5,0,6,0,7,0,0,0],
    [6,3,8,0,5,0,1,0,0],
    [8,0,0,3,0,0,0,2,0],
    [0,9,0,0,0,6,0,0,0],
    [0,0,0,8,0,0,4,0,0]
]

#Step 0: Check if the sudoku board is valid or not
def isValid(board, number, position):

    #checks the column
    board_length = len(board)
    count2 = 0
    while count2 < board_length:
        if count2 != position[0]:
            if number == board[count2][position[1]]:
                return False
        count2 = count2 + 1

    #checks the row
    count = 0
    board_row_length = len(board[0])
    while count < board_row_length:
        if count != position[1]:
            if number == board[position[0]][count]:
                return False
        count = count + 1


    #checks which of the 9 boxes we are currently in
    x_pos1 = ((position[1] // 3) * 3 + 3)
    x_pos2 = ((position[1] // 3) * 3)
    y_pos1 = ((position[0] // 3) * 3)
    y_pos2 = ((position[0] // 3) * 3 + 3)
    index = y_pos1
    index2 = x_pos2
    while index < y_pos2:
        while index2 < x_pos1:
            if position != (index, index2):
                if number == board[index][index2]:
                    return False
            index2 = index2 + 1
        index = index + 1
    
    return True #the board is valid

#Step 0: Print out the sudoku board
def printBoard(board):
    count = 0
    board_row_length = len(board[0])
    board_length = len(board)
    while count < board_length:
        if count != 0:
            if count % 3 == 0:
                print("------------------------") #every 3 rows print a line
        for count2 in range(board_row_length):
            if count2 != 0:
                if count2 % 3 == 0:
                    print(" | ", end="")

            if count2 == 8:
                print(board[count][count2])
            else:
                print(str(board[count][count2]) + " ", end="")
        count = count + 1

#Step 1: find an empty square
def getEmpty(board):
    count = 0
    board_length = len(board)
    board_row_length = len(board[0])
    while count < board_length:
        for count2 in range(board_row_length):
            if board[count][count2] == 0:
                return (count, count2) #returns the row, col
        count = count + 1
    return None #no empty squares on the board

def backtrack_solver(board):
    #base case for recursion
    empty_slot = getEmpty(board)
    if empty_slot:
        row, col = empty_slot
    else:
        return True

    #loops through 1-9 and checks if a value works in the empty box
    for i in range(1,10):
        if isValid(board, i, (row,col)):
            board[row][col] = i
            if backtrack_solver(board):    #recursivly finds a solution using the backtracking algorithm
                return True
            board[row][col] = 0 
    return False 


printBoard(sudoku_board)
backtrack_solver(sudoku_board)
print("\n  SUDOKU BOARD SOLUTION:")
printBoard(sudoku_board)