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


def add(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Matrix are not the same size.")
        return None
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result


# Input
input_file1 = input("Enter first file name: (remember .txt)")
input_file2 = input("Enter second file name: (remember .txt)")

# Read
matrix1 = read(input_file1)
matrix2 = read(input_file2)

# Add
result_matrix = add(matrix1, matrix2)

if (result_matrix is not None):
    write(result_matrix, input("Enter the output filename, remember .txt:"))
