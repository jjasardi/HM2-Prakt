import sympy as sp
import numpy as np

x1, x2 = sp.symbols('x1, x2')  # Definitions of the symbols

# Teilaufgabe a

f1 = 20 - 18 * x1 - 2 * x2 ** 2
f2 = -4 * x2 * (x1 - x2 ** 2)
x0 = np.array([
    [1.1], [0.9]]
)


def newton(func1, func2, x_0):
    funcMatrix = sp.Matrix([func1, func2])  # Matrix with the two functions
    funcMatrix0 = funcMatrix.subs([(x1, x_0[0].item()), [x2, x0[1].item()]])
    Xa = sp.Matrix([x1, x2])  # Matrix with the two symbols
    Dfunca = funcMatrix.jacobian(Xa)  # Jacobian matrix of fa
    Dfunca0 = Dfunca.subs([(x1, x_0[0].item()), [x2, x_0[1].item()]])  # Dfa.subs([(x1, 1.1), [x2, 0.9]]) means: substitute x1 with 1.1 and x2 with 0.9
    AMatrix = np.array(Dfunca0).astype(np.float64)  # Convert Dfa0 to a numpy array
    funcX0 = -1 * np.array(funcMatrix0).astype(np.float64)  # Convert fa0 to a numpy array
    sig0 = np.linalg.solve(AMatrix, funcX0)  # Solve the linear system of equations
    return x_0 + sig0


for i in range(10):  # 10 iterations of Newton's method
    x_1 = newton(f1, f2, x0)
    x0 = x_1
    print(f"x{i+1}:\n", x_1)
