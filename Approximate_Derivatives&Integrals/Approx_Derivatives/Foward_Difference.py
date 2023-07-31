import math
import numpy as np

# Define f(x)
def f(x):
    return math.log(x)

# x0
x0 = 1.8

# Step size
h = 0.1

def foward_diff(x):
    approx = (f(x0+h) - f(x0))/h
    return approx

# Call
print(foward_diff(x0))

