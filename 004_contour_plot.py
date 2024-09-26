import matplotlib.pyplot as plt
import numpy as np


def plot_contour(x, y, z):
    plt.contourf(x, y, z, 20, cmap='viridis')
    plt.colorbar()
    plt.show()


# Usage
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

plot_contour(x, y, z)
