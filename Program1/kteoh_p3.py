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


def times(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("Nah.")
        return None
    result_matrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            dot_product = 0
            for k in range(len(matrix1[0])):
                dot_product += matrix1[i][k] * matrix2[k][j]
            row.append(dot_product)
        result_matrix.append(row)
    return result_matrix


# Input
input_file1 = input("Enter first file name: (remember .txt)")
input_file2 = input("Enter second file name: (remember .txt)")

# Read
matrix1 = read(input_file1)
matrix2 = read(input_file2)

# Times
result_matrix = times(matrix1, matrix2)

if (result_matrix is not None):
    write(result_matrix, input("Enter the output filename, remember .txt:"))
