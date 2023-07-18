import numpy as np
import math
#Parameters to change
#y'= f(x,y)
def f(x, y):
    return -20*y+7*math.e**(-0.5*x)

#[a,b]
a = 0
b = 0.04

#Step size
h = 0.001

#Initial value
y0 = 5

#Number of steps
n = int((b-a)/h)

#Decimal places
d = 4

#Euler's method
def euler_forward(y0, a, b, h, n):
    x = np.zeros(n + 1)
    y = np.zeros(n + 1)
    x[0] = a + h
    y[0] = y0
    for i in range(n):
        y[i + 1] = y[i] + h * f(x[i], y[i])
        x[i + 1] = x[i] + h
    return x, y

x, y = euler_forward(y0 = y0, a = a, b = b, h = h, n = n)
print(f'x: {x[n]:.{d}f}')
print(f'y: {y[n]:.{d}f}')