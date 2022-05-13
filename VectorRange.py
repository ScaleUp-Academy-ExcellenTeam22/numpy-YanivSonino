import numpy as np

if __name__ == '__main__':
    vector = np.array((range(0, 21)))
    vector[9:16] *= -1
    print(vector)
