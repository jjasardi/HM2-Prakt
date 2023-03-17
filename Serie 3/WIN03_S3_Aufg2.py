import sympy as sp
from numpy import linalg
import numpy as np

# symbolic part
# =============
x, y = sp.symbols('x y')
f1s = x ** 2 / 186 ** 2 - y ** 2 / (300 ** 2 - 186 ** 2) - 1
f2s = (y - 500) ** 2 / 279 ** 2 - (x - 300) ** 2 / (500 ** 2 - 279 ** 2) - 1

# a)
p1 = sp.plot_implicit(sp.Eq(f1s, 0), (x, -2000, 2000), (y, -2000, 2000))
p2 = sp.plot_implicit(sp.Eq(f2s, 0), (x, -2000, 2000), (y, -2000, 2000))
p1.append(p2[0])
p1.show()
# they are overlapping at:
# (-1280, 1600), (750, 920), (-200, 70), (250, 210)

# b)
# define the four vectors:
S1 = np.array([[-1280], [1600]])
S2 = np.array([[-200], [70]])
S3 = np.array([[750], [920]])
S4 = np.array([[250], [210]])
X_all = [S1, S2, S3, S4]

# set tolerance to 10e-5:
tol = 10e-5

fs = sp.Matrix([f1s, f2s])
Dfs = fs.jacobian(sp.Matrix([x, y]))

Df = sp.lambdify([([x], [y])], Dfs, "numpy")
f = sp.lambdify([([x], [y])], fs, "numpy")


def newtonSys(coord):
    norm_of_f = 1
    while norm_of_f > tol:
        norm_of_f = linalg.norm(f(coord))
        delta = linalg.solve(Df(coord), -f(coord))
        coord = delta + coord
    return coord


print("the solutions are:")
for x in X_all:
    print(newtonSys(x))
    print()
