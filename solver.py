import math

sudoku = [
    [0,0,6,1,0,0,3,4,5],
    [8,0,1,0,4,0,7,2,0],
    [0,0,3,6,0,2,8,9,1],
    [5,6,0,0,2,0,9,1,3],
    [3,4,2,0,0,9,0,8,7],
    [0,0,7,3,0,0,0,0,0],
    [0,8,0,0,0,1,4,7,0],
    [0,1,0,4,6,7,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    ]


    # Using the Backtracking Algorithm by regressing when solution isn't valid

number_of_rows = int(math.sqrt(len(sudoku[0])))

#function to print sudoku to terminal
def print_sudoku(sudo):
    for i in range(len(sudo)):
        print(" ") 
        if i % number_of_rows == 0 and i != 0:
            print("- - - - - - - - - - - - - - -") 
            print(" ") 
        for j in range(len(sudo[i])):
            if j % number_of_rows == 0 and j != 0:
                print("|", end="")
            
            if j == 8:
                print(" " + str(sudo[i][j])) 
            else:
                print(" " + str(sudo[i][j]) + " ", end="")


#function to find zero (empties)
def find_empty(sudo):
    for i in range(len(sudo)):
        for j in range(len(sudo[i])):
            if sudo[i][j] == 0:
                return (i, j)
    
    return False
            

#function to check whether given value in a sudoku maintains the boards validity
def check_sudoku_validity(sudo, value, value_position):
    #check row and column
    for i in range(len(sudo)):
        for j in range(len(sudo[i])):
            if value_position[1] != j and sudo[value_position[0]][j] == value:
                return False
            if value_position[0] != i and sudo[i][value_position[1]] == value:
                return False
            
    #check 3 cube blocks
    #Divide x pos by 3 and round down to give x pos cube    
    #Divide y pos by 3 and round down to give y pos cube  
    
    value_x_cube = int(math.floor(value_position[1] / number_of_rows))
    value_y_cube = int(math.floor(value_position[0] / number_of_rows))

    for i in range(value_x_cube * number_of_rows, (value_x_cube * number_of_rows) + number_of_rows):
        for j in range(value_y_cube * number_of_rows, (value_y_cube * number_of_rows) + number_of_rows):
            if value_position[1] != j and sudo[value_position[0]][j] == value:
                return False
            if value_position[0] != i and sudo[i][value_position[1]] == value:
                return False

    return True
   
#function to solve and backtrack     
def solver(sudo):
    
    find_empty_pos = find_empty(sudo)

    if not find_empty_pos:
        return True
    else:

        row = find_empty_pos[0]
        col = row = find_empty_pos[1]
        print(row)
        print(col)
        
    for i in range(1 , len(sudo[0]) + 1):
        print(check_sudoku_validity(sudo, i , (row, col)))
        if check_sudoku_validity(sudo, i , (row, col)):
            sudo[row][col] = i
            
            if solver(sudo):
                return True
        
            sudo[row][col] = 0
                
    return False

solver(sudoku)