import numpy as np
from numpy.linalg import inv

#Input data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 7, 9])
#Degree of regression (degree = 2 is ax^2+b*x+c)
degree = 2
#Number of decimal places
d=4

#Regression matrix
matrixA = np.zeros((degree + 1, degree + 1))
matrixB = np.zeros((degree + 1, 1))

for i in range(degree + 1):
    for j in range(degree + 1):
        if matrixA[i][j] == 0:
            matrixA[i][j] = np.sum(x ** (i + j))
        if i != j:
            matrixA[j][i] = np.sum(x ** (i + j))
    matrixB[i] = np.sum(y * (x ** i))

result = np.dot(inv(matrixA), matrixB)
for i in range(len(result)):
    print(f'a_{i} = {result[i, 0]:.{d}f}')

for i in range(len(result)):
    print(f'{result[i, 0]:.{d}f}*x^{i}', end=' ')
    if i != len(result) - 1:
        print("+", end=' ')