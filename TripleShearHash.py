import numpy as np
import math as m

# Define theta in degrees
angle = 30
theta = m.radians(angle)

# Triple shear transformation

# first = np.array([[1, -np.tan(theta/2)], [0, 1]])
# second = np.array([[1, 0], [np.sin(theta), 1]])
# third = np.array([[1, -np.tan(theta/2)], [0, 1]])

side = np.array([[1, -np.tan(theta/2)], [0, 1]])
middle = np.array([[1, 0], [np.sin(theta), 1]])

# Define vector test set - X, Y
pixels = np.array([[10, 5], [20, 3], [4, 5]])

# Perform the matrix multiplication

# result = first @ second @ third @ pixels.T
result = side @ middle @ side @ pixels.T

# Print the result
print(np.round(result.T))

