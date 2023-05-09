import numpy as np

m = 97000
a1 = -5
b1 = 570000
v0 = 100
ve = 0


def f(v):
    return m / ((a1 * v ** 2) - b1)


def vf(v):
    return (v * m) / ((a1 * v ** 2) - b1)


def romberg_extrapolation(f, a, b, m):
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

    return T[0][m]


def sum_trapez(f, a, b, n):
    h = (b - a) / n
    res = (f(a) + f(b)) / 2.
    for i in range(1, n):
        xi = a + i * h
        res = res + f(xi)
    return (h * res)


print("a): Total Time TE = ", romberg_extrapolation(f, v0, ve, 4))
print("b): Total length XE = ", romberg_extrapolation(vf, v0, ve, 4))