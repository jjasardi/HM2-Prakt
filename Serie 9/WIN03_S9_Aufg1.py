import numpy as np
import sympy as sp

# 1

x = sp.Symbol('x')

a = 1.
b = 2.
tol = 10 ** -5


def f(x):
    return sp.ln(x ** 2)


def f2(x):
    return sp.diff(f(x), x, 2)


def absolute_maximum_f(f, a, b):
    f_diff = sp.lambdify(x, f, 'numpy')
    x_values = np.array([a, b])
    return np.max(np.abs(f_diff(x_values)))


h = {'Rf': tol, 'Tf': tol, 'Sf': tol}
f_diff = sp.diff(f(x), 'x', 2)
f_max = absolute_maximum_f(f_diff, a, b)

h['Rf'] = np.ceil(1 / np.sqrt((24 * tol) / (f_max * (b - a))))
print("Rf: h = ", h['Rf'])

h['Tf'] = np.ceil(1 / np.sqrt((12 * tol) / (f_max * (b - a))))
print("Tf: h = ", h['Tf'])

f_diff = sp.diff(f(x), 'x', 4)
f_max = absolute_maximum_f(f_diff, a, b)
h['Sf'] = np.ceil(1 / ((2880 * tol) / (f_max * (b - a))) ** (1 / 4))
print("Sf: h = ", h['Sf'])
