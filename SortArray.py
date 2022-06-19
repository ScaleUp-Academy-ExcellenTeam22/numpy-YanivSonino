import numpy as np

if __name__ == '__main__':
    array = np.random.randn(6, 6)
    print(array)
    array_sort_0 = np.sort(array, axis=0)
    print(array_sort_0)
    array_sort_1 = np.sort(array, axis=1)
    print(array_sort_1)
