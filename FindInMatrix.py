import numpy as np


def find_rows_cols(matrix):
    """
    Find the rows and cols of matrix
    :param matrix: The matrix we want to check.
    :return: Rows and cols.
    """
    return matrix.shape


if __name__ == '__main__':
    arr = np.eye(6)
    print(find_rows_cols(arr))

