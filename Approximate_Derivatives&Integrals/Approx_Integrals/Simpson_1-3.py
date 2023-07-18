import numpy as np
import math

# Define f(x), f''(x) (self define)
def f(x):
    return math.log(2.7*x+5.6)
def f_4th_derivative(x):
    return -318.8646/(2.7*x+5.6)**4

# Set range [a,b]
a = 0
b = 1

# Set number of divide range
N = 4

# Set decimal places
d = 6

# Set epsilon
epsilon = 1e-5

# Define simpson 1/3
def simpson_1_3(a,b,N):
    h = (b-a)/N
    x = np.zeros(N+1)
    y = np.zeros(N+1)
    x[0]=a
    y[0]=f(a)
    x[N]=b
    y[N]=f(b)
    sum_odd=0
    sum_even=0
    for i in range(0,N-1):
        x[i+1]=x[i]+h
        y[i+1]=f(x[i+1])
    for i in range(1,N):
        if i%2==0:
            sum_even = sum_even + y[i]
        else:
            sum_odd = sum_odd + y[i]
    approx= (b-a)*(y[0]+4*sum_odd+2*sum_even+y[N])/(3*N)
    M = abs(f_4th_derivative(a))
    if M<abs(f_4th_derivative(b)):
        M = abs(f_4th_derivative(b))
    error = M*(b-a)/180*h**4
    min_n = round(math.sqrt(math.sqrt((b-a)**5*M/(180*epsilon))))
    return approx, error, min_n

# Call
approx, error, min_n = simpson_1_3(a,b,N)
print(f'{approx:.{d}f}')
print(f'{error:.{d}f}')
print(min_n)