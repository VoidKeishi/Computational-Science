import numpy as np
import math

# Define f(x), f''(x) (self define)
def f(x):
    return 1/(x+1)

# Set range [a,b]
a = 0
b = 1

# Set number of divide range
N = 5

# Set decimal places
d = 5

# Define simpson 3/8
def simpson_3_8(a,b,N):
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
    print(x)
    print(y)
    approx= 3*h/8*(y[0]+3*sum+y[N])
    return approx

# Call
approx = simpson_3_8(a,b,N)
print(f'{approx:.{d}f}')