import numpy as np
import matplotlib.pyplot as plt
# Compute the x and y coordinates for points on a sine curve
if __name__ == '__main__':
    vectorX = np.arange(0, 10)
    vectorY = np.sin(vectorX)
    plt.plot(vectorX, vectorY)
    plt.show()