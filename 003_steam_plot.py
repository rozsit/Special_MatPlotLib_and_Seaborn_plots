import matplotlib.pyplot as plt
import numpy as np


def plot_streamplot(x, y, u, v):
    plt.streamplot(x, y, u, v, density=1)
    plt.show()


# Usage
x = np.linspace(-5, 5, 10)
y = np.linspace(-5, 5, 10)

x, y = np.meshgrid(x, y)
u = -1 - x**2 + y
v = 1 + x - y**2

plot_streamplot(x, y, u, v)
