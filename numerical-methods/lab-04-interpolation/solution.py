x_x = [2.0, 2.3, 2.5, 3.0, 3.5, 3.8, 4.0]
y_y = [5.848, 6.127, 6.300, 6.694, 7.047, 7.243, 7.368]

x = 2.56
n = len(x_x)

L = 0.0

for i in range(n):
    mult = y_y[i]
    for j in range(n):
        if j != i:
            mult *= (x - x_x[j]) / (x_x[i] - x_x[j])
    L += mult

print("f(2.56) =", round(L, 7))
print("-----------------------------------------------------------------------")

x_x = [1.00, 1.08, 1.13, 1.20, 1.27, 1.31, 1.38]
y_y = [1.17520, 1.30254, 1.38631, 1.50946, 1.21730, 1.22361, 1.23470]

x = 1.135
n = len(x_x)

for k in range(1, n):
    for i in range(n - k):
        y_y[i] = ((x_x[i + k] - x) * y_y[i] - (x_x[i] - x) * y_y[i + 1]) / (x_x[i + k] - x_x[i])

print(round(y_y[0], 5))

print("-----------------------------------------------------------------------")

import math       

x_x = []                
y_y = []               

x = 0.75

while x <= 0.85 + 0.000001:
    y = x**2 - math.sin(math.pi * x)
    x_x.append(round(x, 2))
    y_y.append(y)
    x += 0.01

print("Таблиця:")
for i in range(len(x_x)):
    print(round(x_x[i], 2), "   ", round(y_y[i], 7))

#y найближчі до нуля, зміна знаку

x0 = 0.79                              
y0 = 0.79**2 - math.sin(math.pi * 0.79)

x1 = 0.78
y1 = 0.78**2 - math.sin(math.pi * 0.78)

x2 = 0.80         
y2 = 0.80**2 - math.sin(math.pi * 0.80)

x3 = 0.77                         
y3 = 0.77**2 - math.sin(math.pi * 0.77)


#x, при y = 0

P01 = (x0 * (0 - y1) - x1 * (0 - y0)) / (y0 - y1)
P12 = (x1 * (0 - y2) - x2 * (0 - y1)) / (y1 - y2)
P23 = (x2 * (0 - y3) - x3 * (0 - y2)) / (y2 - y3)


P012 = (P01 * (0 - y2) - P12 * (0 - y0)) / (y0 - y2)
P123 = (P12 * (0 - y3) - P23 * (0 - y1)) / (y1 - y3)

P0123 = (P012 * (0 - y3) - P123 * (0 - y0)) / (y0 - y3)

print("x ≈", round(P0123, 4))

