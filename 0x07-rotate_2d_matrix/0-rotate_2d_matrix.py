#!/usr/bin/python3
"""
This module contain a function to rotate
python matrix clockwise

* Psudeocode
- check the legnth of the matrix row
- check the legnth of the matrix column
- let N be the highest length
- with x loop through the range of N / 2
- loop through the range of x to N - x - 1
- save the fist place value with temp
- temp = mat[x][N-y-1]
- mat[x][N-y-1] = mat[y][x]
- mat[y][x] = mat[N-x-1][y]
- mat[N-x-1][y] = mat[N-y-1][N-x-1]
- mat[N-y-1][N-x-1] = temp
"""


def rotate_2d_matrix(mat):
    """This function rotate matrix clockwise
    """
    xaxis = len(mat)
    yaxis = len(mat[0])

    if xaxis >= yaxis:
        N = xaxis
    else:
        N = yaxis
    # Consider all squares one by one
    for x in range(0, int(N / 2)):
        for y in range(x, N-1-x):
            temp = mat[x][N-y-1]

            mat[x][N-y-1] = mat[y][x]

            mat[y][x] = mat[N-x-1][y]

            mat[N-x-1][y] = mat[N-y-1][N-x-1]

            mat[N-y-1][N-x-1] = temp
