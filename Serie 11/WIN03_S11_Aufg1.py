from typing import Any, Callable
import numpy as np
import matplotlib.pyplot as plt


def demof(x, y):
    return x ** 2 + 0.1 * y


def WIN03_S11_Aufg1(f: Callable[[Any, Any], Any], xmin, xmax, ymin, ymax, hx, hy):
    x = np.arange(xmin, xmax, hx, dtype=np.float64)
    y = np.arange(ymin, ymax, hy, dtype=np.float64)
    x, y = np.meshgrid(x, y, indexing='xy')

    dx = np.ones_like(x)
    dy = f(x, y)

    # pfeil vektoren normieren
    l = np.sqrt(dx ** 2 + dy ** 2)
    dx /= l
    dy /= l

    plt.title('Richtungsfeld der DGL')
    plt.quiver(x, y, dx, dy, color='blue', width=0.003, angles='xy')
    plt.grid()
    plt.show()


if __name__ == '__main__':
    WIN03_S11_Aufg1(demof, -2., 2., -1., 2., 0.3, 0.3)