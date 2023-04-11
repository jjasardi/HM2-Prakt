import numpy as np
import matplotlib.pyplot as plt
from HM2_Serie06_Aufg2_Daten import data


# ---------------------------------------------- Teilaufgabe a ---------------------------------------
rows = np.shape(data)[0]
columns = np.shape(data)[1]
X = np.arange(1, rows + 1)
Y = data[0:rows, columns - 1]  # m_CH

A = np.ones((rows, columns))
A[0:rows, 0:columns - 1] = data[0:rows, 0:columns - 1]

# calculation
[Q, R] = np.linalg.qr(A)
C_qr = R
b_qr = Q.T @ Y
lam_qr = np.linalg.solve(C_qr, b_qr)
polyfit = A @ lam_qr


# ------------------------------------------------ plotting ---------------------------------------
# Data points
plt.figure(1)
plt.plot(X, Y, "o", label="Data points")

# balancing function
plt.plot(X, polyfit, linestyle='-', color='orange', label="polyfit")
plt.xlabel('id')
plt.ylabel('measurement')
plt.title('escaping gas')
plt.legend()
plt.show()