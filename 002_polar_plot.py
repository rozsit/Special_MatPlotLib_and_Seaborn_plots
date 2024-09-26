import matplotlib.pyplot as plt
import numpy as np


def plot_polar(theta, radii, title=""):
    plt.figure(figsize=(8, 4))
    ax = plt.subplot(111, projection='polar')
    ax.plot(theta, radii)
    ax.set_title(title)
    plt.show()


# Usage
theta = np.linspace(0, 2 * np.pi, 100)
radii = np.abs(np.sin(theta) * 2)
plot_polar(theta, radii, "Sample Polar Plot")
