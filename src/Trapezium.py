import math

N = 11


def sin(x):
    return math.sin(x)


# Interval [0,π/2]
a = 0
b = math.pi / 2
num = (b - a) / N
x_list = []
sin_list = []
for k in range(N + 1):
    x_list.append(a + (k * num))

for element in x_list:
    sin_list.append(sin(element))

sum = 0
for i in range(1, N):
    sum += sin_list[i]

integral = (num / 2) * (sin(a) + sin(b) + 2 * sum)
M = max(sin_list)  # the second derivative of sin(x) is equal to -sin(x),but |-sin(x)| = sin(x)
tol = (((b - a) ** 3) / (12 * (N ** 3))) * M
print("Using the trapezium method, the integral of sin(x) in [0,pi/2] is equal to:", integral)
print("tol = ", tol)
