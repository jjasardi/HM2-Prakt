from WIN03_S5_Aufg2 import WIN03_S5_Aufg2, plot_spline_function
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as ip

# Aufgabe 3a
x = np.arange(1900, 2020, 10)
y = np.array([75.995, 91.972, 105.711, 123.203, 131.669, 150.697, 179.323, 203.212, 226.505, 249.633, 281.422, 308.745])

result = WIN03_S5_Aufg2(x, y, np.array([]))
yy = result['yy']

plot_spline_function(x, y, np.array([]), yy)

# Aufgabe 3b
cs = ip.CubicSpline(x, y, bc_type='natural')
plt.figure(2)
plt.plot(x, y, 'x', color="red")
plt.plot(np.arange(x[0], x[-1]+ 0.001, 0.001), cs(np.arange(x[0], x[-1]+ 0.001, 0.001)), label="CubicSpline", linestyle=":", color="red")
plt.title("Aufgabe 3b")
plt.legend()
plt.show()

# Aufgabe 3c
fit = np.polyfit(x-1900, y, len(x)-1) # len(x)-1 = 11 is the degree of the polynomial
val = np.polyval(fit, np.linspace(0, 110, 1000))

plt.figure(3)
plt.plot(np.linspace(0, 110, len(val)) + 1900, val , color="green", label="Lagrange", linestyle="dotted")
plt.plot(x, y, 'x', color="red")
plt.plot(np.arange(x[0], x[-1]+ 0.001, 0.001), cs(np.arange(x[0], x[-1]+ 0.001, 0.001)), label="CubicSpline", linestyle=":", color="red")
plt.title("Aufgabe 3c")
plt.legend()
plt.show()



