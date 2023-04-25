import numpy as np


def WIN03_S9_Aufg9(f, a, b, m):
    T = np.zeros([m + 1, m + 1])

    T[0, 0] = sum_trapez(f, a, b, 1)

    for j in range(1, m + 1):
        hj = (b - a) / 2 ** j
        y = 0
        for i in range(1, 2 ** (j - 1) + 1):
            y += f(a + (2 * i - 1) * hj)
        T[j][0] = 0.5 * T[j - 1][0] + hj * y

    for k in range(1, m + 1):
        for j in range(0, m - k + 1):
            T[j][k] = (4 ** k * T[j + 1][k - 1] - T[j][k - 1]) / ((4 ** k) - 1)

    print(T)
    print("T = ", T[0][m])
    return T[0][m]


def sum_trapez(f, a, b, n):
    h = (b - a) / n
    res = (f(a) + f(b)) / 2.
    for i in range(1, n):
        xi = a + i * h
        res = res + f(xi)
    return (h * res)


f = lambda x: np.cos(x ** 2)

a = 0
b = np.pi

m = 4

WIN03_S9_Aufg9(f, a, b, m)
