import numpy as np
import matplotlib.pyplot as plt

'''INPUT'''
x = np.arange(0, 101, 10)  # x = T
y = np.array([999.9, 999.7, 998.2, 995.7, 992.2, 988.1, 983.2, 977.8, 971.8, 965.3, 958.4])
# ausgleichsfunktion = aT^2 + bT + c
A = np.array([x ** 2, x, np.ones(x.shape)]).T
'''INPUT'''


def aufg1a_solve(A, y):
    return np.linalg.solve(A.T @ A, A.T @ y)


def aufg1a_qr(A, y):
    Q, R = np.linalg.qr(A)
    return np.linalg.solve(R, Q.T @ y)


def aufg1b(A):
    print("Cond A.T@A", np.linalg.cond(A.T @ A))
    Q, R = np.linalg.qr(A)
    print("Cond R    ", np.linalg.cond(R))


def aufg1c(x, y):
    return np.polyfit(x, y, 2)


def aufg1d_fehlerfnktionale(A, y, lam, qr, p):  # y = orginale Y, yy = lamdba a), yy_fit = lamdba c)
    print("2-Norm: E(lam)", np.linalg.norm((y - A @ lam)) ** 2)
    print("2-Norm: E(lam) QR", np.linalg.norm((y - A @ qr)) ** 2)
    print("2-Norm: E(lam) polyfit", np.linalg.norm((y - A @ p)) ** 2)


aufg1b(A)

plt.scatter(x, y, color='orange')
xx = np.linspace(x.min(), x.max())
# a)
yy = aufg1a_solve(A, y)
yy2 = aufg1a_qr(A, y)
plt.plot(xx, yy[0] * xx ** 2 + yy[1] * xx + yy[2], '-b')
plt.plot(xx, yy2[0] * xx ** 2 + yy2[1] * xx + yy2[2], '--r')

# c)
p = aufg1c(x, y)
plt.plot(xx, np.polyval(p, xx), '-g')

# d) Es gibt kaum ein Unterschied
aufg1d_fehlerfnktionale(A, y, yy, yy2, p)

plt.grid()
plt.legend(["data-points", "solve", "QR", "Polyval"])
plt.show()