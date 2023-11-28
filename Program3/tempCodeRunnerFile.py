import numpy as np

# Read points from input file
points = []
with open('Program3/input2.txt', 'r') as file:
    for line in file:
        x, y = map(int, line.split())
        points.append((x, y))

# Create matrix X
X = np.array([[1, x] for x, _ in points])

# Create matrix Y
Y = np.array([y for _, y in points]).reshape(-1, 1)

# Print the results
print("X:")
print(X)
print("Y:")
print(Y)
