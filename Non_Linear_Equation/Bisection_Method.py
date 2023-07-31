import math

#Define f(x)
def f(x):
    return x**3-x-1

#Set range [a,b] (Interval of solution separation)
a=1
b=2

#Set epsilon (Accuracy)
epsilon=0.02

#Set decimal places
d=7

#Define bisection method
def bisection_method(f, a, b, epsilon):
    if f(a) * f(b) >= 0:
        print("No solution in range a, b.")
        return None

    while abs(b - a) > epsilon:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return a,b,(a+b)/2, abs(a-b)

#Call bisection method
a,b,approx_solution, error=bisection_method(f, a, b, epsilon)
print(f'Range: [{a:.{d}f}, {b:.{d}f}]')
print(f'Solution: {approx_solution:.{d}f}')
print(f'Error: {error:.{d}f}')