# sudoku-solver

sudoku solver using recursive backtracking in python

For more on backtracking: https://en.wikipedia.org/wiki/Backtracking

**possible_number function**: given a position (x,y) of the board return true iff number n is allowed

**solve_sudoku function**: given a blank space, it tries to put one number among all the allowed numbers and goes ahead with this approach till it reachs the end. If the chosen number in position (x,y) is wrong, the algo removes it (put it as blank) and try to compute the solution with another allowed number. 
