def constructMatrix(sequence):
    B = [
        [], [], [], []
    ]

    n = 0
    total = len(sequence) - 1
    column = total // 4
    if total % 4 != 0:
        column += 1

    for j in range(column):
        for i in range(4):
            if n < total:
                B[i].append(sequence[n])
                n += 1
            else:
                B[i].append(0)

    return B


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


# Step 1: Read the plaintext message from a text file
with open('Program2/input-A21.txt', 'r') as file:
    plaintext = file.read()

# Step 2: Define the encoding matrix A
A = [[1, -1, -1, 1], [2, -3, -5, 4], [-2, -1, -2, 2], [3, -3, -1, 2]]

# Step 3: Convert the message to a sequence of numbers
sequence = []
for char in plaintext:
    unicode_value = ord(char)
    sequence.append(unicode_value)

# Step 4: Construct the plaintext matrix B
B = constructMatrix(sequence)
# Step 5: Multiply A by B to get the cipher matrix C
C = times(A, B)

# Step 6: Output B and C
print("Plaintext Matrix B:", B)
print("Cipher Matrix C:", C)
