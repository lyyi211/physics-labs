import math

h = 0.1
a = 0
B_end = 1

N = int((B_end - a) / h)

def solve_for_b(b):
    x = [i * h for i in range(N + 1)]

    p = [math.sin(2.2 * xi) for xi in x]
    q = [1 for _ in x]
    f = [1 / (b + math.sin(2.2 * xi)**2) for xi in x]

    m = []
    k = []

    for i in range(N - 1):
        mi = -2 + h * p[i]
        ki = 1 - h * p[i] + h**2 * q[i]

        m.append(mi)
        k.append(ki)

    c = [0 for _ in range(N - 1)]
    d = [0 for _ in range(N - 1)]

    # y(0)=0
    alpha0 = 1
    alpha1 = 0
    A = 0

    # y(1)=0
    beta0 = 1
    beta1 = 0
    B = 0

    # прямий хід
    denominator = m[0] * (alpha1 - alpha0 * h) + k[0] * alpha1

    c[0] = (alpha1 - alpha0 * h) / denominator
    d[0] = k[0] * A * h / denominator + h**2 * f[0]

    for i in range(1, N - 1):
        c[i] = 1 / (m[i] - k[i] * c[i - 1])
        d[i] = h**2 * f[i] - k[i] * c[i - 1] * d[i - 1]

    # зворотний хід
    y = [0 for _ in range(N + 1)]

    y[N] = 0

    for i in range(N - 1, 0, -1):
        y[i] = c[i - 1] * (d[i - 1] - y[i + 1])

    y[0] = 0

    return x, y


for n in range(6):
    b = 2.5 + 0.5 * n

    x, y = solve_for_b(b)

    print()
    print(f"n = {n}, b = {b:.1f}")
    print(f"{'i':>2} {'x_i':>6} {'y_i':>12}")

    for i in range(len(x)):
        print(f"{i:2d} {x[i]:6.1f} {y[i]:12.5f}")

print("--------------------------------------------------------------------------------")

import sympy as sp

x = sp.Symbol('x')

# невідомі коефіцієнти
c1, c2, c3 = sp.symbols('c1 c2 c3')

# базисні функції
u0 = x
u1 = x**2 - 2*x
u2 = x**3 - 3*x
u3 = x**4 - 4*x

# розв'язок
y = u0 + c1*u1 + c2*u2 + c3*u3

# похідні
y1 = sp.diff(y, x)
y2 = sp.diff(y1, x)

# нев'язка
R = y2 + y1 - y/x - (4*x**2 - x + sp.Rational(3, 2))

print("R(x) =")
print(sp.expand(R))
print()

# точки колокації
x1 = sp.Rational(1, 4)
x2 = sp.Rational(1, 2)
x3 = sp.Rational(3, 4)

# система рівнянь
eq1 = sp.Eq(R.subs(x, x1), 0)
eq2 = sp.Eq(R.subs(x, x2), 0)
eq3 = sp.Eq(R.subs(x, x3), 0)

# розв'язок 
solution = sp.solve([eq1, eq2, eq3], [c1, c2, c3])

print("Коефіцієнти:")
print(solution)
print()

y_final = sp.expand(y.subs(solution))

print("Наближений розв'язок:")
print(y_final)
print()

print("Десятковий вигляд:")
print(sp.N(y_final, 5))
