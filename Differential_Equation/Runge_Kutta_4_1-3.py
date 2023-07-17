import numpy as np
import math

#Define the function
def f(y,x):
    return y + x

#Change parameters here
y0 = 1
x0 = 0
h = 0.1 
n = 5

#Runge-Kutta 4th order method, simpson's 1/3 rule
def runge_kutta_4th_simpson1_3(y0,x0,h,n):
    y = np.zeros(n+1)
    x = np.zeros(n+1)
    y[0] = y0
    x[0] = x0
    for i in range(n):
        k1 = h*f(y[i], x[i])
        k2 = h*f(y[i] + k1/2, x[i] + h/2)
        k3 = h*f(y[i] + k2/2, x[i] + h/2)
        k4 = h*f(y[i] + k3, x[i] + h)
        y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4)/6
        x[i+1] = x[i] + h
    return y,x

result = runge_kutta_4th_simpson1_3(y0 = y0, x0 = x0, h = h, n = n)
print('x: ', end='')
print(result[1])
print('y: ', end='')
print(result[0])
