import numpy as np

'''sudoku_matrix = [[0,0,7,0,0,9,6,2,0],
                 [0,0,1,6,5,0,0,0,0],
                 [9,0,0,0,0,0,0,7,0],
                 [0,0,9,4,6,0,0,0,0],
                 [0,5,0,0,0,0,0,9,0],
                 [0,0,0,0,2,1,8,0,0],
                 [0,1,0,0,0,0,0,0,8],
                 [0,0,0,0,4,3,1,0,0],
                 [0,4,2,1,0,0,9,0,0]]'''

sudoku_matrix = [[5,3,0,0,7,0,0,0,0],
                 [6,0,0,1,9,5,0,0,0],
                 [0,9,8,0,0,0,0,6,0],
                 [8,0,0,0,6,0,0,0,3],
                 [4,0,0,8,0,3,0,0,1],
                 [7,0,0,0,2,0,0,0,6],
                 [0,6,0,0,0,0,2,8,0],
                 [0,0,0,4,1,9,0,0,5],
                 [0,0,0,0,8,0,0,7,9]]



def possible_to_write_number(rows,columns,number):
    global sudoku_matrix
    for i in range(0,9):
        if sudoku_matrix[rows][i] == number:
            return False
    for i in range(0,9):
        if sudoku_matrix[i][columns] == number:
            return False
    x0 = (columns//3)*3
    y0 = (rows//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if sudoku_matrix[y0+i][x0+j] == number:
                return False
    return True


def solving_game():
    global sudoku_matrix
    for rows in range(9):
        for columns in range(9):
            if sudoku_matrix[rows][columns] == 0:
                for n in range(1,10):
                    if possible_to_write_number(rows,columns,n):
                        sudoku_matrix[rows][columns] = n
                        solving_game()
                        sudoku_matrix[rows][columns] = 0
                return
    print(np.matrix(sudoku_matrix))
    input("more?")


solving_game()
