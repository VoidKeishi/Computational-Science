import math

# Define f(x)
def f(x):
    return math.sin(x) - (x**2)*math.cos(x)

#Set range [a,b] (Interval of solution separation)
a=0
b=2

#Set epsilon (Accuracy)
epsilon=0.01

#Set decimal places
d=4

def secant_method(a, b, epsilon):
    if f(a) * f(b) >= 0:
        print("Can't apply secant method.")
        return None

    while (b - a) >= epsilon:
        c = (a*f(b) - b*f(a)) / (f(b) - f(a))
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

approx_solution = secant_method(a, b, epsilon)
if approx_solution is not None:
    print("Approx solution:", approx_solution)
else:
    print("Can't find solution")
