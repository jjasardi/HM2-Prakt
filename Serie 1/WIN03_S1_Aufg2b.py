import numpy as np
import matplotlib.pyplot as plt

# Parameter
c = 1


def w(x, t):
    return np.sin(x + c * t)


def v(x, t):
    return np.sin(x + c * t) + np.cos(2 * x + 2 * c * t)


[x, y] = np.meshgrid(np.linspace(-5, 5), np.linspace(-5, 5))
z = w(x, y)
fig1 = plt.figure(1)
ax = fig1.add_subplot(111, projection='3d')
ax.plot_wireframe(x, y, z,)
ax.set_xlabel('Space')
ax.set_ylabel('Time')
ax.set_zlabel('Oscillation')
plt.title('w(x,t) = sin(x + ct)')


z = v(x, y)
fig2 = plt.figure(2)
ax = fig2.add_subplot(111, projection='3d')
ax.plot_wireframe(x, y, z,)
ax.set_xlabel('Space')
ax.set_ylabel('Time')
ax.set_zlabel('Oscillation')
plt.title('v(x,t) = sin(x + ct) + cos(2x + 2ct)')
plt.show()