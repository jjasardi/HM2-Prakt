import numpy as np
import matplotlib.pyplot as plt
import HM2_Serie06_Aufg3_Daten as daten

'''INPUT'''
data = daten.data
# Ansatzfunktion
f1 = lambda t: np.ones(t.shape)
f2 = lambda t: t - 1970
f = lambda t, theta: theta[0] * 1 + theta[1] * (t - 1970)

'''INPUT'''


def calc_theta(A):
    Q, R = np.linalg.qr(A)
    return np.linalg.solve(R, Q.T @ y)


x = data[:, 0].copy()
y = np.log10(data[:, 1].copy())

A = np.array([f1(x), f2(x)]).T
theta = calc_theta(A)

plt.scatter(x, y, color="orange", label="Data-Points")
plt.plot(x, f(x, theta), label="Gefittet")
plt.legend()
plt.grid()
plt.show()

# AUFG 3.2
z13 = 10 ** f(2015, theta)
print("Anzahl Transistoren im Z13 von IBM", z13)

# AUFG 3.3
print(theta)