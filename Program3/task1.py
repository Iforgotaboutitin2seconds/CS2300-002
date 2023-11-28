import numpy as np

# Define the function to solve for x
def solveX(D, E):
    # Define the identity matrix
    I = np.identity(D.shape[0])

    # Create an augmented matrix [I - D | I]
    augmented_matrix = np.hstack((I - D, I))

    # Apply Gauss-Jordan elimination
    n = augmented_matrix.shape[0]
    for i in range(n):
        pivot = augmented_matrix[i, i]
        augmented_matrix[i, :] /= pivot
        for j in range(n):
            if i != j:
                factor = augmented_matrix[j, i]
                augmented_matrix[j, :] -= factor * augmented_matrix[i, :]

    # Extract the inverse matrix from the augmented matrix
    inv_I_minus_D = augmented_matrix[:, n:]

    # Round the result to the nearest hundredth
    inv_I_minus_D = np.round(inv_I_minus_D, decimals=2)

    # Calculate x by multiplying (I - D)^-1 with E
    x = np.dot(inv_I_minus_D, E)

    # Round the result to the nearest tenth
    x = np.round(x, decimals=1)

    return x

with open('Program3/input1D.txt', 'r') as file:
    lines = file.readlines()
    D = np.array([list(map(float, line.strip().split())) for line in lines])

with open('Program3/input1E.txt', 'r') as file:
    lines = file.readlines()
    E = np.array([list(map(float, line.strip().split())) for line in lines])

x = solveX(D, E)

for row in x:
    print(row)

with open('Program3/output1.txt', 'w') as file:
    for row in x:
        file.write(' '.join(map(str, row)) + '\n')
