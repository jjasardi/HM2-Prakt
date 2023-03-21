# Aufgabe 2 - Serie 4 Lagrange Interpolation

import numpy as np
import matplotlib.pyplot as plt

Nan = np.nan

# Daten
x = np.array([0, 2500, 5000, 10000], dtype=float)
y = np.array([1013, 747, 540, 226], dtype=float)


def lagrange_int(x, y, x_int):
    """ Lagrange Interpolation """
    n = len(x)
    y_int = 0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (x_int - x[j]) / (x[i] - x[j])
        y_int += term
    return y_int


# Interpolation
x_int = 3750
y_int = lagrange_int(x, y, x_int)

print("Das Ergebnis der Lagrange-Interpolation für den Wert ", x_int, "lautet: ", y_int)

# Plot
plt.plot(x, y, 'o', label='Messwerte')
plt.plot(x_int, y_int, 'o', label='Interpolierter Wert')
plt.title('Lagrange Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
