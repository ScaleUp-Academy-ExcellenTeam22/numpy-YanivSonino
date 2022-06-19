import numpy as np


def add_vector(matrix, vector, matrix_size):
    """
    Adds vector to each row of matrix.
    :param matrix: The matrix.
    :param vector: The vector.
    :param matrix_size: Size of the matrix row
    :return: The matrix
    """
    for i in range(matrix_size):
        matrix[i, :] = matrix[i, :] + vector
    return matrix


if __name__ == '__main__':
    array = np.eye(6)
    vector = np.array(range(0, 6))
    print(add_vector(array, vector, 6))
