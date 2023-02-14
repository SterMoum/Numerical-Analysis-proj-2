import numpy as np
import math

N = 10


def sin(x):
    return math.sin(x)


x_list = [-math.pi, -2.5, -2, -1.5, -1, 0, 1, 1.5, 2, math.pi]
y_list = []
for i in range(N):
    y_list.append(sin(x_list[i]))

# according to least squares method, it has to be solved the following system (Ma = b)
k = 9
M_initial = np.zeros((k + 1, k + 1))  # System Array
vector = np.zeros((k + 1))
power = 0
counter = 0
# initializing M_initial array (M)
for i in range(k + 1):
    for j in range(k + 1):
        sum = 0
        for r in range(N):
            sum += (x_list[r] ** power)
        M_initial[j][i] = sum
        power += 1
    counter += 1
    power = counter

# initializing vector (b)
sum = 0
power = 0
for i in range(k + 1):
    sum = 0
    for j in range(N):
        sum += y_list[j] * (x_list[j] ** power)
    power += 1
    vector[i] = sum

# using Cramer`s rule we can find the regression coefficients using the determinants of matrix M_initial
M = M_initial.copy()
array_list = []  # in this list each position contains a matrix which is matrix M_initial with the i_th collumn
# replaced with vector (b)
for i in range(k + 1):
    for j in range(k + 1):
        M[j][i] = vector[j]
    array_list.append(M)
    M = M_initial.copy()

# solving the equations (a_k.. a_0) using cramer`s rule
factors = []
for i in range(k + 1):
    solution = (np.linalg.det(array_list[i])) / (np.linalg.det(M_initial))
    # solution = round(solution, 4)
    factors.append(solution)

print(factors)
