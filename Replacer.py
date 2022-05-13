import numpy as np

if __name__ == '__main__':
    array = np.array([[1, 2, 3], [5, 6, 9]])
    given_number = 3
    replace_number = 10

    print(np.where(array == given_number, replace_number, array))
    print(np.where(array < given_number, replace_number, array))
    print(np.where(array > given_number, replace_number, array))

    print(array)
