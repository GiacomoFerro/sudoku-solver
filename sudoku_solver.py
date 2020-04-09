
import numpy as np

board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]
print("initial board:\n",np.matrix(board),"\n")

#return true if number n is possible in position (row,col)
def possible_number(row,col,n):
  global board
  for i in range(0,9):
    if board[row][i] == n:
      return False
  for i in range(0,9):
    if board[i][col] == n:
      return False
  x0=(row//3)*3
  y0=(col//3)*3
  for i in range(0,3):
    for j in range(0,3):
      if board[x0+i][y0+j] == n:
        return False
  return True

#recursive approach with backtracking of values
def solve_sudoku():
  global board
  for row in range(9):
    for col in range(9):
      if board[row][col] == 0: #find empty cell
        for n in range(1,10): # put possible_number number
          if possible_number(row,col,n):
            board[row][col]=n
            solve_sudoku()
            #backtracking if 'n' was wrong choice in row,col
            board[row][col]=0 
        return
  print("possible_number solution:\n",np.matrix(board),"\n")
  input("More?")

#solve sudoku (you can display all possible_number solutions)
solve_sudoku()
#P.S. in this case there is exactly one solution
