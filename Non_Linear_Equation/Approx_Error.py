import math

#Define the function and its derivative
def f(x):
    return x**3 - 5*x**2 + 12
def f_derivative(x):
    return 3*x**2 - 10*x
#Change parameters here
a = -2
b = -1
x0 = -1.37
#Number of decimal places
d = 4

#Approximate error
def approx_error(x0):
    min = f_derivative(a)
    if f_derivative(b) < min:
        min = f_derivative(b)
    c = f(x0)/min
    return c

print(f'{approx_error(x0):.{d}f}')