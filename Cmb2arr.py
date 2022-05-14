import numpy as np

if __name__ == '__main__':
    first_array_1d = np.array([10, 20, 30])

    second_array_1d = np.array([[40, 50, 60], [70, 80, 90]])
    print(first_array_1d)
    print(second_array_1d)

    for first_array_1d, second_array_1d in np.nditer([first_array_1d, second_array_1d]):
        print("{}:{}".format(first_array_1d, second_array_1d))
