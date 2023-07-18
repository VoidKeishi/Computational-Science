import math
import numpy as np

# Define f(x)
def f(x):
    return math.log(x)

# x0
x0 = 1.8

# Step size
h = 0.1

def backward_diff(x):
    approx = (f(x0) - f(x0-h))/h
    return approx

# Call
print(backward_diff(x0))
