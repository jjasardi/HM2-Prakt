import sympy as sp
import numpy as np

x1, x2 = sp.symbols('x1, x2')  # Definitions of the symbols

f1 = 20 - 18 * x1 - 2 * x2 ** 2
f2 = -4 * x2 * (x1 - x2 ** 2)
x0 = np.array([
    [1.1], [0.9]]
)


def newton(func1, func2, x_0):
    # Define the functions and their Jacobian matrix
    f = sp.Matrix([func1, func2])
    J = f.jacobian([x1, x2])

    # Evaluate the functions and their Jacobian matrix at x_0
    f_x0 = f.subs([(x1, x_0[0].item()), (x2, x_0[1].item())])
    J_x0 = J.subs([(x1, x_0[0].item()), (x2, x_0[1].item())])

    # Solve the linear system of equations
    delta = np.linalg.solve(np.array(J_x0).astype(np.float64), -np.array(f_x0).astype(np.float64))

    # Return the updated value of x
    return x_0 + delta


for i in range(10):  # 10 iterations of Newton's method
    x_1 = newton(f1, f2, x0)
    x0 = x_1
    print(f"x{i+1}:\n", x_1)
