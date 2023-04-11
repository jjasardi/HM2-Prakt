# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 16:40:56 2021

Höhere Mathematik 2, Serie 7, Aufgabe 2, Daten

@author: knaa
"""

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import scipy.optimize as opt

x=np.array([2. , 2.5, 3. , 3.5, 4. , 4.5, 5. , 5.5, 6. , 6.5, 7. , 7.5, 8. ,
       8.5, 9. , 9.5])

y=np.array([159.57209984, 159.8851819 , 159.89378952, 160.30305273,
       160.84630757, 160.94703969, 161.56961845, 162.31468058,
       162.32140561, 162.88880047, 163.53234609, 163.85817086,
       163.55339958, 163.86393263, 163.90535931, 163.44385491])

p = sp.symbols('p0 p1 p2 p3')


def f(x, p):
    """fit function"""
    return (p[0] + p[1] * 10 ** (p[2] + p[3] * x)) / (1 + 10 ** (p[2] + p[3] * x))


lam_0 = np.array([100, 120, 3, -1], dtype=np.float64)
tol = 1e-5

g = sp.Matrix([y[k] - f(x[k], p) for k in range(len(x))])
Dg = g.jacobian(p)
g = sp.lambdify([p], g, 'numpy')
Dg = sp.lambdify([p], Dg, 'numpy')


# Fitten mit gedämpftem Gauss-Newton Verfahren
def gauss_newton_d(g, Dg, lam0, tol, max_iter, pmax, damping):
    k = 0
    lam = np.copy(lam0)
    increment = tol + 1
    err_func = np.linalg.norm(g(lam)) ** 2

    while increment > tol and k < max_iter:
        [Q, R] = np.linalg.qr(Dg(lam))
        delta = np.linalg.solve(R, -Q.T @ g(lam)).flatten()

        p = 0
        while damping and p < pmax:
            print('Dämpfung: ', p)
            err_func_cur = np.linalg.norm(g(lam)) ** 2
            err_func_next = np.linalg.norm(g(lam + delta / 2 ** p)) ** 2
            if err_func_next < err_func_cur:
                break
            p += 1

        # Update des Vektors Lambda
        lam = lam + delta / 2 ** p
        err_func = np.linalg.norm(g(lam)) ** 2
        increment = np.linalg.norm(delta)
        k = k + 1
        print('Iteration: ', k)
        print('lambda = ', lam)
        print('Inkrement = ', increment)
        print('Fehlerfunktional =', err_func)
    return (lam, k)


max_iter = 30
pmax = 5
damping = 1
[lam_with, n] = gauss_newton_d(g, Dg, lam_0, tol, max_iter, pmax, damping)

# Plotten der Daten und der Fitfunktion
x_plot = np.linspace(2, 10, 100)
plt.plot(x, y, 'o', label='Messwerte')
plt.plot(x_plot, f(x_plot, lam_with), label='Fit')

# Minimum des Fehlerfunktionals
def err_func(lam):
    return np.linalg.norm(g(lam)) ** 2


lam_opt = opt.fmin(err_func, lam_0)

# Plotten der scipy Ergebnisse
plt.plot(x_plot, f(x_plot, lam_opt), label='scipy')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()