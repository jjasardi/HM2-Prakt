import numpy as np


def trap(x, y):
    assert len(x) == len(y)

    tf = 0
    for i in range(len(x) - 1):
        tf += ((y[i] + y[i + 1]) / 2) * (x[i + 1] - x[i])

    return tf


if __name__ == "__main__":
    vec_r = np.array([0, 800, 1200, 1400, 2000, 3000, 3400, 3600, 4000, 5000, 5500, 6370])
    vec_p = np.array([13000, 12900, 12700, 12000, 11650, 10600, 9900, 5500, 5300, 4750, 4500, 3300])
    print(trap(vec_r, vec_p))