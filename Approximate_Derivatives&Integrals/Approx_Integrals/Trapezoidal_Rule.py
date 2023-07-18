import numpy as np
import math

# Define f(x), f''(x) (self define)
def f(x):
    return 2*x**4 + x**3 + 1
def f_2nd_derivative(x):
    return 24*x**2 + 6*x

# Set range [a,b]
a = 1
b = 2

# Set number of divide range
N = 3

# Set decimal places
d = 4

# Define trapezoidal
def trapezoidal_rule(a,b,N):
    h = (b-a)/N
    x = np.zeros(N+1)
    y = np.zeros(N+1)
    x[0]=a
    y[0]=f(a)
    x[N]=b
    y[N]=f(b)
    sum=0
    for i in range(0,N-1):
        x[i+1]=x[i]+h
        y[i+1]=f(x[i+1])
        sum = sum + y[i+1]
    approx= h/2*(f(a)+f(b)+2*sum)
    M = f_2nd_derivative(a)
    if f_2nd_derivative(b)>M:
        M=f_2nd_derivative(b)
    error = M*(b-a)/12*h**2
    return approx, error

# Call
approx, error = trapezoidal_rule(a,b,N)
print(f'{approx:.{d}f}')
print(f'{error:.{d}f}')