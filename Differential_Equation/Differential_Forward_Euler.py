import numpy as np
import math
#Tham so can thay doi
#Dang y'= f(x,y)
def f(x, y):
    return -20*y+7*math.e**(-0.5*x)

#Khoang [a,b]
a = 0
b = 0.04

#Buoc nhay h
h = 0.001

#Gia tri ban dau
y0 = 5

#So buoc nhay
n = int((b-a)/h)

#Ham giai
def euler_modified(y0, a, b, h, n):
    x = np.zeros(n + 1)
    y = np.zeros(n + 1)
    x[0] = a + h
    y[0] = y0
    for i in range(n):
        y[i + 1] = y[i] + h * f(x[i], y[i])
        x[i + 1] = x[i] + h
    return x, y

x, y = euler_modified(y0 = y0, a = a, b = b, h = h, n = n)
print(f'x: {x[n]}')
print(f'y: {y[n]}')