#  File: Spiral.py

#  Description: This program is designed to create a spiral and then use
#  the function called sum adjacent numbers and give an output file.

#  Student Name: Gaytri Riya Vasal

#  Course Name: CS 313E

#  Unique Number: 86439

#  Date Created: 6/2/2022

#  Date Last Modified: 6/3/2022

import sys

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n


def create_spiral(n):
    """This function takes a dimension n and return a 2D list of N x N
     in a spiral formation"""
    if (n % 2) == 0:
        n += 1

    # Starting at center
    x_cord = (n // 2)
    y_cord = (n // 2)
    num = 1

    # Setting up spiral
    rows, cols = n, n
    spiral = [[0 for c in range(cols)] for r in range(rows)]

    # Starting Algorithm
    spiral[x_cord][y_cord] = num
    y_cord += 1
    num += 1

    for ring in range(1, n - (n // 2)):

        for i in range(0, ((ring + 1) * 2) - 3):
            spiral[x_cord][y_cord] = num
            x_cord += 1
            num += 1

        for j in range((ring + 1) * 2 - 2):
            spiral[x_cord][y_cord] = num
            y_cord -= 1
            num += 1

        for k in range((ring + 1) * 2 - 2):
            spiral[x_cord][y_cord] = num
            x_cord -= 1
            num += 1

        for m in range((ring + 1) * 2 - 2):
            spiral[x_cord][y_cord] = num
            y_cord += 1
            num += 1

        spiral[x_cord][y_cord] = num
        num += 1
        y_cord += 1

    return spiral


def sum_adjacent_numbers(spiral, n):
    for i in range(len(spiral)):
        for j in range(len(spiral[i])):
            if spiral[i][j] == n:
                return get_num_neighbors_sum(spiral, i, j)


def get_num_neighbors_sum(raster, row, col):
    """Return sum of cells around row and col that are inbounds.

    Must handle special cases for corner and edge cells.

    basically checking row minus 1 and row and row plus one and same for
    column"""
    num_neighbors_sum = 0
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if inbounds(r, c, raster):
                num_neighbors_sum += raster[r][c]
    num_neighbors_sum -= raster[row][col]

    return int(num_neighbors_sum)


def inbounds(r, c, matrix):
    """ Return if r and c are inbounds for the given matrix.
     in other words return true if they are valid indices for matrix
     ignoring the negative indices"""

    return 0 <= r < len(matrix) and 0 <= c < len(matrix[r])


def main():

    x = sys.stdin.read()

    a = x.split("\n")

    n = int(a[0])
    dim_spiral = n
    spiral = create_spiral(dim_spiral)

    for value in range(1, len(a) - 1):
        print(sum_adjacent_numbers(spiral, int(a[value])))


if __name__ == "__main__":
    main()
