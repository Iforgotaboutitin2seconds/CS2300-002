def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed


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

matrix = read("kteoh_mat1.txt")
matrix = transpose(matrix)
write(matrix, "kteoh_p6_mat1.txt")

matrix = read("kteoh_mat2.txt")
matrix = transpose(matrix)
write(matrix, "kteoh_p6_mat2.txt")

matrix = read("kteoh_mat3.txt")
matrix = transpose(matrix)
write(matrix, "kteoh_p6_mat3.txt")

matrix = read("kteoh_mat4.txt")
matrix = transpose(matrix)
write(matrix, "kteoh_p6_mat4.txt")