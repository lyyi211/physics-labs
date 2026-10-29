x = 3.25
a = [12.78, 14.35, 17.19, 1.34, -1.72]

b = a[0]
print("b0 =", b)

for i in range(1, len(a)):
    b = b * x + a[i]
    print("b", i, "=", b)
print("P(3.25) =", b)
print("Округлено:", round(b, 5))

#----------------------------------------------------------------------
import math

eps = 1e-15
print(" k    x           y = 1/x^3              iterations")
print("----------------------------------------------------")


for k in range(16):
    x = 3 + 2*k
    a = x**3

    m = math.floor(math.log2(a)) + 1
    y = 2**(-m)

    t = 0 #к-ть ітерацій
    while True:
        y_new = y * (2 - a*y)
        t += 1
        if abs(y_new - y) <= eps * abs(y_new):
            y = y_new
            break
        y = y_new

    print(f"{k:<4}{x:<6}{y:<25.15f}{t}")


