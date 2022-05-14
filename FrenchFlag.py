import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    mask = np.zeros((4, 6), dtype=int)
    mask[:, 2:4] = 1
    mask[:, 4:] = 2
    flag = np.full((4, 6, 3), 255, dtype=np.uint8)
    flag[mask == 0] = [0, 38, 84]
    flag[mask == 2] = [255, 0, 0]
    plt.imshow(flag)
    plt.show()
