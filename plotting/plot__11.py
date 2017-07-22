# Import numpy and matplotlib.pyplot
import numpy as np
import matplotlib.pyplot as plt


def doplt(A):
    plt.pcolor(A, cmap='Blues')
    plt.colorbar()
    plt.show()


doplt(np.array([[1, 2, 1], [0, 0, 1], [-1, 1, 1]]))
doplt(np.array([[1, 0, -1], [2, 0, 1], [1, 1, 1]]))
doplt(np.array([[-1, 0, 1], [1, 0, 2], [1, 1, 1]]))
doplt(np.array([[1, 1, 1], [2, 0, 1], [1, 0, -1]]))

