a11, a12, a13, a14 = 3.14, -2.12, 1.17, 1.27
a21, a22, a23, a24 = -2.12, 1.32, -2.45, 2.13
a31, a32, a33, a34 = 1.17, -2.45, 1.18, 3.14

print("Ділимо перше рівняння на a11 = 3.14")

b12 = a12 / a11
b13 = a13 / a11
b14 = a14 / a11

print("b12 =", b12)
print("b13 =", b13)
print("b14 =", b14)
print()

# нові коеф (i = 2)
a22_1 = a22 - a21 * b12
a23_1 = a23 - a21 * b13
a24_1 = a24 - a21 * b14

print("a^(1)_22 =", a22_1)
print("a^(1)_23 =", a23_1)
print("a^(1)_24 =", a24_1)
print()

# нові коеф (i = 3)
a32_1 = a32 - a31 * b12
a33_1 = a33 - a31 * b13
a34_1 = a34 - a31 * b14

print("a^(1)_32 =", a32_1)
print("a^(1)_33 =", a33_1)
print("a^(1)_34 =", a34_1)
print()

print("Отримана система:")
print(a22_1, "*x2 +", a23_1, "*x3 =", a24_1)
print(a32_1, "*x2 +", a33_1, "*x3 =", a34_1)
print()

# ділимо друге рівняння
b23 = a23_1 / a22_1
b24 = a24_1 / a22_1

print("Ділимо перше рівняння нової системи на a^(1)_22")
print("b23 =", b23)
print("b24 =", b24)
print()

print("Отримана система:")
print("x2 +", b23, "*x3 =", b24)
print(a32_1, "*x2 +", a33_1, "*x3 =", a34_1)
print()

# (i = 2)
a33_2 = a33_1 - a32_1 * b23
a34_2 = a34_1 - a32_1 * b24

print("a^(2)_33 =", a33_2)
print("a^(2)_34 =", a34_2)
print()

print("Система з одним невідомим:")
print(a33_2, "*x3 =", a34_2)
print()

# знаходимо x3
x3 = a34_2 / a33_2
print("x3 =", x3)

# x2
x2 = b24 - b23 * x3
print("x2 =", x2)

# x1
x1 = b14 - b12 * x2 - b13 * x3
print("x1 =", x1)

print()
print("Перевірка підстановкою в початкову систему:")

r1 = a11*x1 + a12*x2 + a13*x3
r2 = a21*x1 + a22*x2 + a23*x3
r3 = a31*x1 + a32*x2 + a33*x3

print("1 рівняння: ", r1, "≈", a14)
print("2 рівняння: ", r2, "≈", a24)
print("3 рівняння: ", r3, "≈", a34)

print("---------------------------------------------------------------------------------------------------")
a11,a12,a13,a14 = 2, 1, -5, 1
a21,a22,a23,a24 = 1, -3, 0, -6
a31,a32,a33,a34 = 2, 0, -1, 2
a41,a42,a43,a44 = 1, 4, -7, 6
b1,b2,b3,b4     = 8, 9, -5, 0

print("A =")
print([a11,a12,a13,a14])
print([a21,a22,a23,a24])
print([a31,a32,a33,a34])
print([a41,a42,a43,a44])
print("b =", [b1,b2,b3,b4])
print()

# розклад A = B*C
# i=1
b11 = a11
c12 = a12/b11
c13 = a13/b11
c14 = a14/b11

print("i=1")
print("b11 =", b11)
print("c12 =", c12)
print("c13 =", c13)
print("c14 =", c14)
print()

#i=2
b21 = a21
b22 = a22 - b21*c12
c23 = (a23 - b21*c13)/b22
c24 = (a24 - b21*c14)/b22

print("i=2")
print("b21 =", b21)
print("b22 =", b22)
print("c23 =", c23)
print("c24 =", c24)
print()

#i=3
b31 = a31
b32 = a32 - b31*c12
b33 = a33 - (b31*c13 + b32*c23)
c34 = (a34 - (b31*c14 + b32*c24))/b33

print("i=3")
print("b31 =", b31)
print("b32 =", b32)
print("b33 =", b33)
print("c34 =", c34)
print()

#i=4
b41 = a41
b42 = a42 - b41*c12
b43 = a43 - (b41*c13 + b42*c23)
b44 = a44 - (b41*c14 + b42*c24 + b43*c34)

print("i=4")
print("b41 =", b41)
print("b42 =", b42)
print("b43 =", b43)
print("b44 =", b44)
print()

print("Отримали матриці B і C:")
print("B =")
print([b11, 0,   0,   0  ])
print([b21, b22, 0,   0  ])
print([b31, b32, b33, 0  ])
print([b41, b42, b43, b44])
print()
print("C =")
print([1,   c12, c13, c14])
print([0,   1,   c23, c24])
print([0,   0,   1,   c34])
print([0,   0,   0,   1  ])
print()
print("Система By=b:")
print(b11,"*y1 =",b1)
print(b21,"*y1 +",b22,"*y2 =",b2)
print(b31,"*y1 +",b32,"*y2 +",b33,"*y3 =",b3)
print(b41,"*y1 +",b42,"*y2 +",b43,"*y3 +",b44,"*y4 =",b4)
print()
print("Система Cx=y:")
print("x1 +",c12,"*x2 +",c13,"*x3 +",c14,"*x4 = y1")
print("x2 +",c23,"*x3 +",c24,"*x4 = y2")
print("x3 +",c34,"*x4 = y3")
print("x4 = y4")
print()

print("Розв'язуємо By=b:")
y1 = b1 / b11
print("y1 =", y1)

y2 = (b2 - b21*y1) / b22
print("y2 =", y2)

y3 = (b3 - (b31*y1 + b32*y2)) / b33
print("y3 =", y3)

y4 = (b4 - (b41*y1 + b42*y2 + b43*y3)) / b44
print("y4 =", y4)
print()


print("Розв'язуємо Cx=y:")

x4 = y4
print("x4 =", x4)

x3 = y3 - c34*x4
print("x3 =", x3)

x2 = y2 - c23*x3 - c24*x4
print("x2 =", x2)

x1 = y1 - c12*x2 - c13*x3 - c14*x4
print("x1 =", x1)
print()

print("Перевірка")
r1 = a11*x1 + a12*x2 + a13*x3 + a14*x4
r2 = a21*x1 + a22*x2 + a23*x3 + a24*x4
r3 = a31*x1 + a32*x2 + a33*x3 + a34*x4
r4 = a41*x1 + a42*x2 + a43*x3 + a44*x4
print("r1 =", r1, ",b1 =", b1)
print("r2 =", r2, ",b2 =", b2)
print("r3 =", r3, ",b3 =", b3)
print("r4 =", r4, ",b4 =", b4)
print("--------------------------------------------------------------------------------------------")
import math
def r4(x):
    return round(x, 4)

a11,a12,a13 = 2.65, -0.52, 1.02
a21,a22,a23 = -0.52, 2.53, 0.46
a31,a32,a33 = 1.02, 0.46, 2.16
b1,b2,b3    = 1.25, 0.95, 1.33

print("Перевірка симетричності A:")
sym = (a12 == a21) and (a13 == a31) and (a23 == a32)
print("A симетрична?", sym)
print()

#Прямий хід: A = T^T * T
print("Знаходимо T (верхня трикутна), округлення 4 знаки:")

t11=r4(math.sqrt(a11))
print("t11 =",t11)

t12=r4(a12/t11)
print("t12 =",t12)

t13=r4(a13/t11)
print("t13 =",t13)

t22=r4(math.sqrt(r4(a22-r4(t12*t12))))
print("t22 =",t22)

t23=r4((r4(a23-r4(t12*t13)))/t22)
print("t23 =",t23)

t33=r4(math.sqrt(r4(a33-r4(t13*t13)-r4(t23*t23))))
print("t33 =",t33)

print()

print("T =")
print([t11,t12,t13])
print([0,t22,t23])
print([0,0,t33])
print()

#Зворотній хід: T^T y = b
print("Система T^T y = b:")
print(t11,"* y1 =",b1)
print(t12,"* y1 +",t22,"* y2 =",b2)
print(t13,"* y1 +",t23,"* y2 +",t33,"* y3 =",b3)
print()

y1=r4(b1/t11)
print("y1 =",y1)

y2=r4(r4(b2-r4(t12*y1))/t22)
print("y2 =",y2)

y3=r4(r4(b3-r4(t13*y1)-r4(t23*y2))/t33)
print("y3 =",y3)

print()

#T x = y
print("Система T x = y:")
print(t11,"* x1 +",t12,"* x2 +",t13,"* x3 =",y1)
print(t22,"* x2 +",t23,"* x3 =",y2)
print(t33,"* x3 =",y3)
print()

x3=r4(y3/t33)
print("x3 =",x3)

x2=r4(r4(y2-r4(t23*x3))/t22)
print("x2 =",x2)

x1=r4(r4(y1-r4(t12*x2)-r4(t13*x3))/t11)
print("x1 =",x1)

print()
print("Відповідь:")
print("x1 =",x1," x2 =",x2," x3 =",x3)

#Перевірка Ax ≈ b
print("Перевірка Ax ≈ b (4 знаки):")

r1 = r4(r4(a11*x1) + r4(a12*x2) + r4(a13*x3))
r2 = r4(r4(a21*x1) + r4(a22*x2) + r4(a23*x3))
r3 = r4(r4(a31*x1) + r4(a32*x2) + r4(a33*x3))

print("r1 =", r1, " ~ b1 =", b1)
print("r2 =", r2, " ~ b2 =", b2)
print("r3 =", r3, " ~ b3 =", b3)
print("--------------------------------------------------------------------------------------------")
eps = 1e-4

a11,a12,a13,b1 = 5,-1,1,10
a21,a22,a23,b2 = 2,8,-1,11
a31,a32,a33,b3 = -1,1,4,3

print("Перетворюємо систему:")

print("x1 = (",b1,"+",-a12,"x2 +",-a13,"x3 )/",a11)
print("x2 = (",b2,"+",-a21,"x1 +",-a23,"x3 )/",a22)
print("x3 = (",b3,"+",-a31,"x1 +",-a32,"x2 )/",a33)
print()

c12 = -a12/a11
c13 = -a13/a11
d1 = b1/a11

c21 = -a21/a22
c23 = -a23/a22
d2 = b2/a22

c31 = -a31/a33
c32 = -a32/a33
d3 = b3/a33

print("Ітераційна форма:")
print("x1 =",d1,"+",c12,"*x2 +",c13,"*x3")
print("x2 =",d2,"+",c21,"*x1 +",c23,"*x3")
print("x3 =",d3,"+",c31,"*x1 +",c32,"*x2")
print()

#перевірка збіжності
s1 = abs(c12) + abs(c13)
s2 = abs(c21) + abs(c23)
s3 = abs(c31) + abs(c32)

print("Перевірка умови збіжності:")
print("c1 =", s1)
print("c2 =", s2)
print("c3 =", s3)
print()

alpha = max(s1, s2, s3)
print("alpha =", alpha)

if alpha < 1:
    print("Умова збіжності виконується (alpha < 1)")
else:
    print("Умова збіжності НЕ виконується")
print()

#початковий вектор x0
x1 = round(d1,2)
x2 = round(d2,2)
x3 = round(d3,2)

print("k    x1        x2        x3        delta")
print("-------------------------------------------")

k = 0
print(k, "   ", round(x1,4), "   ", round(x2,4), "   ", round(x3,4), "   ", "-")

while True:
    k += 1

    x1_new = d1 + c12*x2 + c13*x3
    x2_new = d2 + c21*x1 + c23*x3
    x3_new = d3 + c31*x1 + c32*x2

    delta = max(abs(x1_new-x1), abs(x2_new-x2), abs(x3_new-x3))

    print(k, "   ", round(x1_new,4), "   ", round(x2_new,4), "   ", round(x3_new,4), "   ", round(delta,4))

    x1 = x1_new
    x2 = x2_new
    x3 = x3_new

    if delta < eps:
        break

print()
print("Розв'язок:")
print("x1 =", round(x1,4))
print("x2 =", round(x2,4))
print("x3 =", round(x3,4))
print("Кількість ітерацій =", k)
print("--------------------------------------------------------------------------------------------")
eps = 1e-4

a11,a12,a13,b1 = 5,-1,1,10
a21,a22,a23,b2 = 2,8,-1,11
a31,a32,a33,b3 = -1,1,4,3

print("Перетворюємо систему:")

print("x1 = (",b1,"+",-a12,"x2 +",-a13,"x3 )/",a11)
print("x2 = (",b2,"+",-a21,"x1 +",-a23,"x3 )/",a22)
print("x3 = (",b3,"+",-a31,"x1 +",-a32,"x2 )/",a33)
print()

c12 = -a12/a11
c13 = -a13/a11
d1 = b1/a11

c21 = -a21/a22
c23 = -a23/a22
d2 = b2/a22

c31 = -a31/a33
c32 = -a32/a33
d3 = b3/a33

print("Ітераційна форма:")
print("x1 =",d1,"+",c12,"*x2 +",c13,"*x3")
print("x2 =",d2,"+",c21,"*x1 +",c23,"*x3")
print("x3 =",d3,"+",c31,"*x1 +",c32,"*x2")
print()

#перевірка збіжності
s1 = abs(c12) + abs(c13)
s2 = abs(c21) + abs(c23)
s3 = abs(c31) + abs(c32)

print("Перевірка умови збіжності:")
print("c1 =", s1)
print("c2 =", s2)
print("c3 =", s3)
print()

alpha = max(s1, s2, s3)
print("alpha =", alpha)

if alpha < 1:
    print("Умова збіжності виконується (alpha < 1)")
else:
    print("Умова збіжності НЕ виконується")
print()

#початковий вектор x0
x1 = round(d1,2)
x2 = round(d2,2)
x3 = round(d3,2)

print("k    x1        x2        x3        delta")
print("-------------------------------------------")

k = 0
print(k, "   ", round(x1,4), "   ", round(x2,4), "   ", round(x3,4), "   ", "-")

while True:
    k += 1

    x1_new = d1 + c12*x2 + c13*x3
    x2_new = d2 + c21*x1_new + c23*x3
    x3_new = d3 + c31*x1_new + c32*x2_new

    delta = max(abs(x1_new-x1), abs(x2_new-x2), abs(x3_new-x3))

    print(k, "   ", round(x1_new,4), "   ", round(x2_new,4), "   ", round(x3_new,4), "   ", round(delta,4))

    x1 = x1_new
    x2 = x2_new
    x3 = x3_new

    if delta < eps:
        break

print()
print("Розв'язок:")
print("x1 =", round(x1,4))
print("x2 =", round(x2,4))
print("x3 =", round(x3,4))
print("Кількість ітерацій =", k)

