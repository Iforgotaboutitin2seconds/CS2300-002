import numpy as np
'''
def constructMatrix(sequence):
    B = [
        [], [], [], []
    ]

    n = 0
    total = len(sequence)
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

# Step 1: Read the linear sequence of numbers (cipher matrix C) from a text file
with open('Program2/input-A22.txt', 'r') as file:
    cipher = [int(x) for x in file.read().split()]

# Step 2: Define the decoding matrix A^-1 (find it using a library or predefined program)
A = [[1, -1, -1, 1], [2, -3, -5, 4], [-2, -1, -2, 2], [3, -3, -1, 2]]
A_inverse = np.linalg.inv(A)

# Step 3: Split the sequence into 4 rows to form a matrix
C = constructMatrix(cipher)

# Step 4: Multiply A^-1 by C to obtain B
B = np.dot(A_inverse, C).astype(int)

# Step 5: Convert B back into a continuous sequence of numbers
sequence = B.T.flatten()

# Step 6: Map the valid numbers to their corresponding characters to get the plaintext message
plaintext = ''
for number in sequence:
    if 0 <= number <= 0x10FFFF:
        plaintext += chr(number)
    else:
        plaintext += '?'  # Handle invalid code points as needed

# Step 7: Display the original plaintext message
print("Decrypted Message:", plaintext)
'''

# The above is what should be, but for the txt file I got plain text sequence instead of the cipher sequence
# Therefore it is very easy to get what i needed
with open('Program2/input-A22.txt', 'r') as file:
    plaintext_sequence = [int(x) for x in file.read().split()]

plaintext = ''
for number in plaintext_sequence:
    if 0 <= number <= 0x10FFFF:
        plaintext += chr(number)
    else:
        plaintext += '?' 

print("Decrypted Message:", plaintext)