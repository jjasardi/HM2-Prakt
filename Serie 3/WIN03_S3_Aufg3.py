import sympy as sp
import numpy as np
from numpy import linalg

# symbolic part
# =============
x, y, z = sp.symbols('x y z')
f1s = x + y**2 - z**2 - 13
f2s = sp.ln(y/4) + sp.exp(0.5*z-1) - 1
f3s = (y - 3)**2 - z**3 + 7

# set tolerance to 10e-5:
tol = 10e-5

fs = sp.Matrix([f1s, f2s, f3s])
Dfs = fs.jacobian(sp.Matrix([x, y, z]))

Df = sp.lambdify([([x], [y], [z])], Dfs, "numpy")
f = sp.lambdify([([x], [y], [z])], fs, "numpy")
X_zero = np.array([[1.5], [3], [2.5]])


def dampNewtonSys(coord):
    norm_of_f = 1
    k_max = 4
    k = 0
    while norm_of_f > tol:                  # as long as tol not reached
        norm_of_f = linalg.norm(f(coord))
        delta = linalg.solve(Df(coord), -f(coord))
        if linalg.norm(f(coord + delta / 2 ** k)) \
                >= norm_of_f and k <= k_max:
            coord = coord + delta / 2 ** k
            k += 1
        else:
            coord = delta + coord
    return coord


print("the solutions is:")
print(dampNewtonSys(X_zero))