import numpy as np
import matplotlib.pyplot as plt
from WIN03_S4_Aufg2 import lagrange_int

x_values = np.array([1981, 1984, 1989, 1993, 1997, 2000, 2001, 2003, 2004, 2010], dtype=np.float64)
y_values = np.array([0.5, 8.2, 15, 22.9, 36.6, 51, 56.3, 61.8, 65, 76.7], dtype=np.float64)
P = np.polyfit(x_values, y_values, len(x_values) - 1)
print(P)

# ----------------------------------------- Exercise 3 ----------------------------------------------
# --------------------------------------------- a) --------------------------------------------------
x_axis = np.arange(1975, 2020.1, 0.1)
plt.figure(0)
plt.title("Exercise a) percentage of households possessing a PC")
plt.xlabel("year")
plt.ylabel("households in percentage")
plt.ylim([-100, 250])
plt.grid()
plt.plot(x_axis, np.polyval(P, x_axis))
plt.plot(x_values, y_values, ls="", marker="o", label="points")

# As one can see in the plot, the polynom isn't matching with every single data point

# ---------------------------------------------------------------------------------------------------
# --------------------------------------------- b) --------------------------------------------------

x_values_corr = x_values - x_values.mean()
P1 = np.polyfit(x_values_corr, y_values, len(x_values) - 1)
print(P1)
plt.figure(1)
plt.title("Exercise b) percentage of households possessing a PC")
plt.xlabel("year")
plt.ylabel("households in percentage")
plt.ylim([-100, 250])
plt.grid()
plt.plot(x_axis, np.polyval(P1, x_axis - x_values.mean()))
plt.plot(x_values, y_values, ls="", marker="o", label="points")

# The polynom matches better with the data points, but stronger amplitude between the points

# ---------------------------------------------------------------------------------------------------
# --------------------------------------------- c) --------------------------------------------------
print(np.polyval(P1, 2020))
# the result for 2020 is -9.394939401965316e+22, which is clearly not realistic.
# The polynom can't be used for predictions.

# ---------------------------------------------------------------------------------------------------
# --------------------------------------------- d) --------------------------------------------------
plt.figure(2)
plt.title("Exercise d) percentage of households possessing a PC")
plt.xlabel("year")
plt.ylabel("households in percentage")
plt.ylim([-100, 250])
plt.grid()
result = []
# consider this as a compound of the code from Exercise 2 ----
for x_int in x_axis:
    result.append(lagrange_int(x_values, y_values, x_int))
# -------------------------------------------------------------
plt.plot(x_axis, result, label="lagrange")
plt.plot(x_values, y_values, linewidth=3, ls="", marker="o", label="Data points")
plt.plot(x_axis, np.polyval(P1, x_axis - x_values.mean()), linewidth=3, linestyle=(0, (1, 5)), color="green", label="polyfit")
plt.legend()
plt.show()
# As one can see, they are the same. Those green dots are representing the polyfit from b).