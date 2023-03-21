import numpy as np

x = 3750

x0 = 0
x1 = 2500
x2 = 5000
x3 = 10000

y0 = 1013
y1 = 747
y2 = 540
y3 = 226

l0 = (x-x1) * (x-x2) * (x-x3) / ((x0-x1) * (x0-x2) * (x0-x3))
l1 = (x-x0) * (x-x2) * (x-x3) / ((x1-x0) * (x1-x2) * (x1-x3))
l2 = (x-x0) * (x-x1) * (x-x3) / ((x2-x0) * (x2-x1) * (x2-x3))
l3 = (x-x0) * (x-x1) * (x-x2) / ((x3-x0) * (x3-x1) * (x3-x2))

print(l0)
print(l1)
print(l2)
print(l3)

p3 = l0 * y0 + l1 * y1 + l2 * y2 + l3 * y3
print(p3)
