import numpy as np


def mul_arrays(arr1, arr2):
    return np.multiply(arr1, arr2)


if __name__ == '__main__':
    array_1 = np.eye(6)
    array_2 = np.eye(6)
    print(mul_arrays(array_1, array_2))
