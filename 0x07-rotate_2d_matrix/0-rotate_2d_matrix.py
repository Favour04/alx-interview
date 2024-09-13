#!/usr/bin/env python3
"""
This module contain a function to rotate
python matrix clockwise

* Psudeocode
- check the legnth of the matrix row
- check the legnth of the matrix column
- let N be the highest length
- with x loop through the range of N / 2
- loop through the range of x to N - x - 1
- save the fist place value with temp = [y][N-x-1]
- [y][N-x-1] = [x][y]  
- [N-x-1][N-y-1] = temp
- [N-y-1][x] = [N-x-1][N-y-1]
- [x][y] = [N-y-1][x]
"""


def rotateMatrix(mat):
    xaxis = len(mat)
    yaxis = len(mat[0])
    
    if xaxis >= yaxis:
        N = xaxis
    else:
        N = yaxis 
    # Consider all squares one by one
    for x in range(0, int(N / 2)):
 
        # Consider elements in group
        # of 4 in current square
        for y in range(x, N-x-1):
 
            # store current cell in temp variable
            temp = mat[x][y
 
            # move values from right to top
            mat[x][y] = mat[y][N-1-x]
 
            # move values from bottom to right
            mat[y][N-1-x] = mat[N-1-x][N-1-y]
 
            # move values from left to bottom
            mat[N-1-x][N-1-y] = mat[N-1-y][x]
 
            # assign temp to left
            mat[N-1-y][x] = temp