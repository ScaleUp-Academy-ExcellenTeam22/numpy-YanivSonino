import numpy as np

if __name__ == '__main__':
    first_array_1d = np.array([10, 20, 30])
    second_array_1d = np.array([40, 50, 60])
    print(np.dstack((first_array_1d, second_array_1d)))
