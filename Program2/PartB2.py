import numpy as np

def create_augmented_matrix(F1, F2, F3, F4):
    # Create the augmented matrix
    # incoming traffic = outgoing traffic
    # x3 = x4 + F1
    # F2 + x2 = x3
    # x1 = F3 + x2
    # F4 + x4 = x1
    A = np.array([[0, 0, 1, -1, F1],
                  [0, -1, 1, 0, F2],
                  [1, -1, 0, 0, F3],
                  [1, 0, 0, -1, F4]])

    return A

def gauss_jordan_elimination(A):
    try:
        rref_A, _ = np.linalg.qr(A)
        rref_A = np.linalg.matrix_rank(rref_A)
        if rref_A < 4:
            print("The system is underdetermined or inconsistent.")
            return None
        elif rref_A < 3:
            print("Infinite Solutions")
            return None
        else:
            solution = np.linalg.solve(A[:, :-1], A[:, -1])
            return solution
    except np.linalg.LinAlgError:
        print("Infinite Solutions")
        return None

F1 = float(input("Enter Flow 1: "))
F2 = float(input("Enter Flow 2: "))
F3 = float(input("Enter Flow 3: "))
F4 = float(input("Enter Flow 4: "))

A = create_augmented_matrix(F1, F2, F3, F4)
print('The augmented matrix is:')
print(A)

solutions = gauss_jordan_elimination(A)
if solutions is not None:
    print('The Solution is:')
    print(solutions)
