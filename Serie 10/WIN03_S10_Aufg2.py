import numpy as np
import matplotlib.pyplot as plt
from WIN03_S8_Aufg3a import trap as trap

g = 9.81
m_a = 300000
m_e = 80000
v_rel = 2600
t_e = 190
u = (m_a - m_e) / t_e


def acceleration(x):
    return v_rel * (u / (m_a - u * x)) - g


def plot_values(x, y):
    arr = np.zeros(x.size)
    for i in range(x.size):
        arr[i] = trap(x[0:i], y[0:i])
    return arr


def plotter(id, data, ylabel, legend):
    plt.figure(id)
    for dat in data:
        plt.plot(dat[0], dat[1])
    plt.xlabel('Zeit t')
    plt.ylabel(ylabel)
    plt.grid()
    plt.legend(legend)
    plt.title(ylabel)
    plt.show()


# 2a
t = np.arange(0, t_e)
a = acceleration(t)

v = plot_values(t, a)
h = plot_values(t, v)

plotter(1, [(t, a)], 'Beschleunigung a', ['a(t)'])
plotter(2, [(t, v)], 'Geschwindigkeit v', ['v(t)'])
plotter(3, [(t, h)], 'Höhe h', ['h(t)'])

# 2b
v_analytic = v_rel * np.log(m_a / (m_a - u * t)) - g * t
h_analytic = -(v_rel * (m_a - u * t)) / u * (np.log(m_a / (m_a - u * t))) + v_rel * t - 0.5 * g * t ** 2

plotter(4, [(t, v), (t, v_analytic)], 'Geschwindigkeit v', ['v(t)', 'v_analytic(t)'])
plotter(5, [(t, h), (t, h_analytic)], 'Höhe h', ['h(t)', 'h_analytic(t)'])
