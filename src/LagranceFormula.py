import math
import matplotlib.pyplot as pl
from matplotlib.ticker import NullFormatter


def sin(x):
    return math.sin(x)


def Lagrance(x_points, y_points, value):
    # points = x
    # solutions = y
    p = 0
    for i in range(len(x_points)):
        L_i = 1
        for k in range(len(x_points)):
            if i != k:
                L_i *= (value - x_points[k]) / (x_points[i] - x_points[k])
        p += L_i * y_points[i]
    return p


x_list1 = [-math.pi, -2.5, -2, -1.5, -1, 0, 1, 1.5, 2, math.pi]
step = (2 * math.pi) / 200
x_list = []
start = -math.pi
for i in range(200):
    x_list.append(start)
    start += step
y_list = []
y_list1 = []
lagrance_list = []
lagrance_list1 = []
for i in range(len(x_list)):
    y_list.append(sin(x_list[i]))
for i in range(len(x_list1)):
    y_list1.append(sin(x_list1[i]))
for element in x_list:
    lagrance_list.append(Lagrance(x_list, y_list, element))
for element in x_list1:
    lagrance_list1.append(Lagrance(x_list1, y_list1, element))
print("(200 points)Sin function results:", y_list)
print("(200 points)Lagrance function results:", lagrance_list)
print()
print("(10 points)Sin function results:", y_list1)
print("(10 points) Lagrance function results", lagrance_list1)

# tol computing
sum = 0
for i in range(200):
    sum += abs(y_list[i] - lagrance_list[i])
print("Tol:", sum)
