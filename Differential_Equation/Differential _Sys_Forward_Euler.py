import numpy as np
import math

#Parameters for tuning
#y'= f(x,y,z) & z' = g(x,y,z)
def f(x, y, z):
    return (z-y)*x
def g(x, y, z):
    return (z+y)*x

#[a,b]
a = 0
b = 0.6

#Step h
h = 0.1

#Init values
y0 = 1
z0 = 1

#Number of steps
n = int((b-a)/h)

#Decimal places
d = 4

#Euler's method (No change)
def euler_modified(y0, z0, a, b, h, n):
    x = np.zeros(n + 1)
    y = np.zeros(n + 1)
    z = np.zeros(n + 1)
    x[0] = a+h
    y[0] = y0
    z[0] = z0
    for i in range(n):
        y[i + 1] = y[i] + h * f(x[i], y[i], z[i])
        z[i + 1] = z[i] + h * g(x[i], y[i], z[i])
        x[i + 1] = x[i] + h
    return x, y, z

x, y, z = euler_modified(y0 = y0, z0 = z0, a = a, b = b, h = h, n = n)
print(f'x: {x[n]}')
print(f'y: {y[n]:.{d}f}')
print(f'z: {z[n]:.{d}f}')