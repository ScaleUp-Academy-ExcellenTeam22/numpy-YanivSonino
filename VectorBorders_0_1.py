import numpy as np


def create_array_borders_1_in_0():
    """
    Creates an array size 10x10 with borders of 1 and inside cell are 0
    :return: The array
    """
    array = np.ones((10, 10))
    array[1:-1, 1:-1] = 0
    return array


if __name__ == '__main__':
    print(create_array_borders_1_in_0())
