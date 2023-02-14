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

sum1 = 0
for i in range(1, round(N / 2)):
    sum1 += sin_list[2 * i]
sum2 = 0
for k in range(1, round((N / 2) + 1)):
    sum2 += sin_list[(2 * k) - 1]

integral = (num / 3) * (sin(a) + sin(b) + 2 * sum1 + 4 * sum2)
M = max(sin_list)  # the fourth derivative of sin(x) is equal to sin(x)
tol = (((b - a) ** 5) / (180 * (N ** 4))) * M
print("Using the simpson method, the integral of sin(x) in [0,pi/2] is equal to:", integral)
print("tol = ", tol)
