import sympy as sp

x = sp.Symbol('x')

# кількість коеф
N = 8

# коеф c0, c1, ...
c = sp.symbols(f'c0:{N}')

# ряд
y = sum(c[n] * x**n for n in range(N))

# похідні
y1 = sp.diff(y, x)
y2 = sp.diff(y1, x)


r = sp.series(sp.exp(-x**2), x, 0, N).removeO()
left = y2 - x*y1 - 2*y

expr = sp.expand(left - r)

equations = []

# початкові умови: c0 = 1, c1 = 1/2
equations.append(sp.Eq(c[0], 1))
equations.append(sp.Eq(c[1], sp.Rational(1, 2)))

for k in range(N - 2):
    coef = sp.expand(expr).coeff(x, k)
    equations.append(sp.Eq(coef, 0))

solution = sp.solve(equations, c, dict=True)[0]

print("Коефіцієнти:")
for n in range(N):
    print(f"c{n} =", solution[c[n]])

y_series = y.subs(solution)

print()
print("Наближений розв'язок:")
print("y(x) =", y_series)

print("----------------------------------------------------------------------------------------")

x, t = sp.symbols('x t', positive=True)

# початкові умови
x0 = 1
y_initial = -2

def f(t, y):
    return 2 - y / t

# початкове наближення
y0 = sp.Integer(2)

# 3 наближення
y1 = y_initial + sp.integrate(f(t, y0), (t, x0, x))
y2 = y_initial + sp.integrate(f(t, y1.subs(x, t)), (t, x0, x))
y3 = y_initial + sp.integrate(f(t, y2.subs(x, t)), (t, x0, x))

print("y0(x) =", y0)
print("y1(x) =", sp.simplify(y1))
print("y2(x) =", sp.simplify(y2))
print("y3(x) =", sp.simplify(y3))

print("----------------------------------------------------------------------------------------")

import math

# параметри
a = 0
b = 1
h = 0.1

betas = [1 + 0.25 * n for n in range(5)]

for beta in betas:

    print()
    print(f"beta = {beta}")

    x = 0.0
    y = 0.0

    print(f"{'i':>2} {'x':>6} {'y':>12}")

    i = 0
    print(f"{i:2d} {x:6.1f} {y:12.6f}")

    while x < b:

        f = 1 + 0.6 * y * math.sin(x) - beta * y**2

        y = y + h * f

        x = round(x + h, 10)

        i += 1

        print(f"{i:2d} {x:6.1f} {y:12.6f}")

print("----------------------------------------------------------------------------------------")

a = 0
b = 1
h = 0.1
y0 = -0.4122

def f(x, y, beta):
    return -y**2 + beta * x / (1 + x**2)

for alpha in range(15, 21):
    beta = 2.5 + alpha / 40

    print()
    print(f"alpha = {alpha}, beta = {beta:.4f}")
    print(f"{'i':>2} {'x_i':>6} {'y_i':>10}")

    x = a
    y = y0

    print(f"{0:2d} {x:6.1f} {y:10.4f}")

    i = 0

    while x < b:
        x_next = round(x + h, 10)

        # грубе наближення 7.35
        y_iter = y + h * f(x, y, beta)

        # ітераційна обробка 7.36
        while True:
            y_new = y + h / 2 * (
                f(x, y, beta) + f(x_next, y_iter, beta)
            )
 
            if round(y_new, 4) == round(y_iter, 4):
                break

            y_iter = y_new

        y = y_new
        x = x_next
        i += 1

        print(f"{i:2d} {x:6.1f} {y:10.4f}")

print("----------------------------------------------------------------------------------------")

h = 0.1
a = 0
T = 0.3

def f(t, x, b):
    return math.exp(-3*t) * (x**2 + b)

for k in range(6):
    b = 1 + 0.4 * k

    print()
    print(f"k = {k}, b = {b:.1f}")
    print(f"{'i':>2} {'t_i':>6} {'x_i':>10} {'K1':>10} {'K2':>10} {'K3':>10} {'K4':>10} {'dx':>10}")

    t = a
    x = 0.0
    i = 0

    while t < T:
        K1 = h * f(t, x, b)
        K2 = h * f(t + h/2, x + K1/2, b)
        K3 = h * f(t + h/2, x + K2/2, b)
        K4 = h * f(t + h, x + K3, b)

        dx = (K1 + 2*K2 + 2*K3 + K4) / 6

        print(f"{i:2d} {t:6.1f} {x:10.5f} {K1:10.5f} {K2:10.5f} {K3:10.5f} {K4:10.5f} {dx:10.5f}")

        x = x + dx
        t = round(t + h, 10)
        i += 1

    print(f"{i:2d} {t:6.1f} {x:10.5f}")
    
print("----------------------------------------------------------------------------------------")

h = 0.1

def f(t, x, a):
    return math.exp(-a * t) * (x**2 + 1)

def rk4_step(t, x, a):
    K1 = h * f(t, x, a)
    K2 = h * f(t + h/2, x + K1/2, a)
    K3 = h * f(t + h/2, x + K2/2, a)
    K4 = h * f(t + h, x + K3, a)

    dx = (K1 + 2*K2 + 2*K3 + K4) / 6
    return x + dx

for k in range(6):
    a = 1 + 0.4 * k

    print()
    print(f"k = {k}, a = {a:.1f}")
    print(f"{'i':>2} {'t_i':>6} {'x_i':>10} {'x*':>10}")

    t_values = [0.0]
    x_values = [0.0]

    # початковий відрізок методом Рунге-Кутта: x1, x2, x3
    t = 0.0
    x = 0.0

    for i in range(3):
        x = rk4_step(t, x, a)
        t = round(t + h, 10)

        t_values.append(t)
        x_values.append(x)

    # два кроки методом Адамса: x4, x5
    for i in range(3, 5):
        f_i   = f(t_values[i],   x_values[i],   a)
        f_i1  = f(t_values[i-1], x_values[i-1], a)
        f_i2  = f(t_values[i-2], x_values[i-2], a)
        f_i3  = f(t_values[i-3], x_values[i-3], a)

        # прогноз за формулою Адамса-Бешфорта
        x_pred = x_values[i] + h / 24 * (
            55*f_i - 59*f_i1 + 37*f_i2 - 9*f_i3
        )

        t_next = round(t_values[i] + h, 10)

        f_pred = f(t_next, x_pred, a)

        # уточнення за формулою Адамса-Мултона
        x_corr = x_values[i] + h / 24 * (
            9*f_pred + 19*f_i - 5*f_i1 + f_i2
        )

        t_values.append(t_next)
        x_values.append(x_corr)

    for i in range(len(t_values)):
        fp = f(t_values[i], x_values[i], a)
        print(f"{i:2d} {t_values[i]:6.1f} {x_values[i]:10.5f} {fp:10.5f}")

print("----------------------------------------------------------------------------------------")

h = 0.1
a = 1
b = 2

def f(x, y):
    return -y / x - y**2 * math.log(x)

def rk4_step(x, y):
    K1 = h * f(x, y)
    K2 = h * f(x + h/2, y + K1/2)
    K3 = h * f(x + h/2, y + K2/2)
    K4 = h * f(x + h, y + K3)

    return y + (K1 + 2*K2 + 2*K3 + K4) / 6

x_values = [1.0]
y_values = [1.0]

# початковий відрізок: y1, y2, y3 методом Рунге-Кутта
x = 1.0
y = 1.0

for i in range(3):
    y = rk4_step(x, y)
    x = round(x + h, 10)

    x_values.append(x)
    y_values.append(y)

# продовження методом Мілна
while x_values[-1] < b:
    i = len(x_values)

    f_i1 = f(x_values[i-1], y_values[i-1])
    f_i2 = f(x_values[i-2], y_values[i-2])
    f_i3 = f(x_values[i-3], y_values[i-3])

    # прогноз за першою формулою Мілна
    y_pred = y_values[i-4] + 4*h/3 * (2*f_i1 - f_i2 + 2*f_i3)

    x_next = round(x_values[-1] + h, 10)

    f_pred = f(x_next, y_pred)

    # корекція за другою формулою Мілна
    y_corr = y_values[i-2] + h/3 * (f_i2 + 4*f_i1 + f_pred)

    eps = abs(y_corr - y_pred) / 29

    x_values.append(x_next)
    y_values.append(y_corr)

print(f"{'i':>2} {'x_i':>6} {'y_i':>10}")

for i in range(len(x_values)):
    print(f"{i:2d} {x_values[i]:6.1f} {y_values[i]:10.4f}")

