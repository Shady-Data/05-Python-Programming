"""
​
(Largest rows and columns) Write a program that randomly fills in 0s and 1s into
a matrix, prints the matrix, and finds the rows and columns with the most
1s. Here is a sample run of the program:
0011
0011
1101
1010
The largest row index: 2
The largest column index: 2, 3
​
"""

import random

n = 4
def main():
    matrix = []
    # This nested loop fills out the matrix with random 0s or 1s
    for i in range(n):
        matrix.append([])
        for j in range(n):
            # import pdb; pdb.set_trace()
            matrix[i].append(random.randint(0, 1))
            print(matrix[i][j], end = " ")

        print()

    # Check rows
    rowSum = sum(matrix[0])
    rowList = [0]
    for i in range(1, n):
        if rowSum < sum(matrix[i]):
            rowSum = sum(matrix[i])
            rowList = [i]
        elif rowSum == sum(matrix[i]):
            rowList.append(i)
            
    print("The largest row index: ", end = "")
    for i in range(len(rowList) - 1):
        print(rowList[i], end = ", ")
    print(rowList[len(rowList) - 1])

    # Check columns
    columnSum = sumColumn(matrix, 0)
    columnList = [0]
    for j in range(1, n):
        if columnSum < sumColumn(matrix, j):
            columnSum = sumColumn(matrix, j)
            columnList = [j]
        elif columnSum == sumColumn(matrix, j):
            columnList.append(j)
            
    print("The largest column index: ", end = "")
    for i in range(len(columnList) - 1):
        print(columnList[i], end = ", ")
    print(columnList[len(columnList) - 1])

# This function sums up the column  
def sumColumn(m, j):
    sum = 0
    for i in range(n):
        sum += m[i][j]
    return sum

main()




