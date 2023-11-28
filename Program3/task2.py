import numpy as np


# Make sure to use pip install matplotlib to see the graph
import matplotlib.pyplot as plt

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

# Calculate X^TX
XTX = np.dot(X.T, X)

# Calculate X^TY
XTY = np.dot(X.T, Y)

# Calculate A
A = np.dot(np.linalg.inv(XTX), XTY)

# Calculate the least squares regression line
slope = round(A[1][0], 1)
intercept = round(A[0][0], 1)

# Print the least squares regression line
print("Least squares regression line: y = {}x + {}".format(slope, intercept))

# Create x and y values for the line
x_values = np.linspace(min([x for x, _ in points]), max([x for x, _ in points]), 100)
y_values = A[1][0] * x_values + A[0][0]

# Plot the points and the line
plt.scatter([x for x, _ in points], [y for _, y in points], color='blue', label='Points')
plt.plot(x_values, y_values, color='red', label='Regression Line')

# Set labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Least Squares Regression')

# Show the legend
plt.legend()

# Show the plot
plt.show()
