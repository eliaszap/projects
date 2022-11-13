"""
Script to solve the N Queen problem

"""
import numpy as np
import time

# A function to check if a spot on the board is free for a queen
def check(board, coordinate,n):
    
    i = coordinate[0]
    j = coordinate[1]

    #check if row is free
    row = board[i,:]
    if np.sum(row) > 0:
        return False
    
    # check if column is free
    col = board[:,j]
    if np.sum(col) > 0:
        return False
    
    #check if diagonals are free
    left_diag = [board[i-k,j-k] for k in range(1,i+1) if j != 0]
    right_diag = [board[i-k,j+k] for k in range(1,n-j)]
    if np.sum(left_diag) > 0 or np.sum(right_diag) > 0: 
        return False
    
    return True

#Function that backtracks to last placed queen, removes it and return the column index
def backtrack(board, row,n):
    
    if row == 0:
        row = 1
    col = np.where(board[row-1,:]==1)[0][0]
    board[row-1,col] = 0
    if col == n-1:
        backtrack(board,row-1,n)
    else:
         addQueens(board,n,row-1,col+1) 

# The recursive function that places the queens
def addQueens(board, n, row, col):
    
    # This if-statement is only true if the problem is solved
    if np.sum(board.flatten()) == n:
        print('Solution for the N = '+str(n)+' Queen problem:')
        print(board)
        return 
    
    if check(board,(row,col),n):
        board[row,col] = 1
        re_board = board.copy()
        addQueens(re_board,n,row+1,0)
        
    elif col == n-1 or (col == n-1 and row == n-1):
        backtrack(board,row,n)
        
    else:            
        addQueens(board,n,row,col+1)


# The Main function to solve the N Queen problem
def solve(n):
    
    # make the chess board
    board = np.zeros((n,n))
    
    # find a solution, starting in cornor i,j = 0,0
    t_start = time.perf_counter()
    addQueens(board, n, 0, 0)
    t_end = time.perf_counter() 
    t = t_end - t_start
    print('Solution found in '+str(round(t*100))+' ms')

N = 8
solve(N)
