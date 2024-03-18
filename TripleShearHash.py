from PIL import Image
import numpy as np
import math as m

def load_image(image_path):
    img = Image.open(image_path)
    return np.array(img)

def hash_function(x, y):
    return hash((x, y))

def rotate(image, angle)
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
    print(np.floor(result.T))

image = load_image('')

