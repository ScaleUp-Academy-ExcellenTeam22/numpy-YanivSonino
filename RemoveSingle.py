import numpy as np

if __name__ == '__main__':
    array = np.zeros((3, 1, 4))
    print(np.squeeze(array).shape)
