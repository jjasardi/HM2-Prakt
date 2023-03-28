# Aufgabe 2 - Spline Interpolation

import numpy as np
import matplotlib.pyplot as plt


def plot_spline_function(x, y, xx, yy):
    plt.figure()
    plt.plot(xx, yy, label="Predicted Values")
    plt.scatter(x, y, color='red', marker="x", label="Original Values")
    plt.title("Spline-Function")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()


def print_coefficients_and_matrix(x, y, a, b, c, d, h, z, A):
    print("x = ", x)
    print("y = ", y)
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)
    print("d = ", d)
    print("h = ", h)
    print("Coefficients")
    print("A = ", A)
    print("z = ", z)


def matrixA(hi, n):
    A = np.zeros((n - 1, n - 1))
    for j in range(n - 1):
        for i in range(n - 1):
            if i == j:
                A[j, i] = 2 * (hi[i] + hi[j + 1])
            if i == j - 1:
                A[j, i] = hi[i]
            if i == j + 1:
                A[j, i] = hi[j]
    return A


def WIN03_S5_Aufg2(x, y, xx):
    n = len(x) - 1
    a = np.copy(y)
    c = np.array([0])
    h = np.diff(x)
    A = matrixA(h, n)
    b = np.array([])
    d = np.array([])
    z = np.array([3 * (y[i + 2] - y[i + 1]) / h[i + 1] - 3 * (y[i + 1] - y[i]) / h[i] for i in range(len(x) - 2)])
    yy = np.array([])
    c = np.append(c, np.linalg.solve(A, z))
    c = np.append(c, 0)
    for i in range(n):
        b = np.append(b, (y[i + 1] - y[i]) / h[i] - h[i] / 3 * (c[i + 1] + 2 * c[i]))
        d = np.append(d, (1 / (3 * h[i])) * (c[i + 1] - c[i]))

    def s(x_val):
        for i in range(len(x) - 1):
            if x[i] <= x_val < x[i + 1]:
                return a[i] + b[i] * (x_val - x[i]) + c[i] * (x_val - x[i]) ** 2 + d[i] * (x_val - x[i]) ** 3

    for i in xx:
        yy = np.append(yy, s(i))

    return {'a': a, 'b': b, 'c': c, 'd': d, 'h': h, 'z': z, 'A': A, 'yy': yy}


if __name__ == '__main__':
    x = np.array([4, 6, 8, 10])
    y = np.array([6, 3, 9, 0])
    xx = np.arange(4, 10, 0.01)

    result = WIN03_S5_Aufg2(x, y, xx)
    a = result['a']
    b = result['b']
    c = result['c']
    d = result['d']
    h = result['h']
    z = result['z']
    A = result['A']
    yy = result['yy']

    plot_spline_function(x, y, xx, yy)
    print_coefficients_and_matrix(x, y, a, b, c, d, h, z, A)
