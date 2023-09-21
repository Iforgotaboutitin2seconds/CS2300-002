import numpy as np


def read(filename):
    with open(filename, 'r') as file:
        matrix = []
        for line in file:
            row = [float(x) for x in line.strip().split()]
            matrix.append(row)
        return matrix


def write(matrix, filename):
    with open(filename, 'w') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')


# Input
input_file1 = input("Enter first file name: (remember .txt)")
input_file2 = input("Enter second file name: (remember .txt)")
choose = input("Enter 0 to add, 1 to times:")

choose = int(choose)

# Read
matrix1 = read(input_file1)
matrix2 = read(input_file2)

if (choose == 0):
    result_matrix = np.add(matrix1, matrix2)
else:
    result_matrix = np.dot(matrix1, matrix2)

if (result_matrix is not None):
    write(result_matrix, input("Enter the output filename, remember .txt:"))
