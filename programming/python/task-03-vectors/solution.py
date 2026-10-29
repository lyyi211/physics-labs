#варіант 16 (6)
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'



class Vector:
    def __init__(self, start: Point, end: Point):
        self.vector_x = end.x - start.x
        self.vector_y = end.y - start.y

    def setVX(self, vector_x):
        self.vector_x = vector_x

    def setVY(self, vector_y):
        self.vector_y = vector_y

    def __str__(self):
        return '(' + str(self.vector_x) + ', ' + str(self.vector_y) + ')'



    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(Point(0, 0), Point(self.vector_x * other, self.vector_y * other))
        elif isinstance(other, Vector):
            return self.vector_x * other.vector_x + self.vector_y * other.vector_y
        return NotImplemented


    def length(self):
        return math.sqrt(self.vector_x ** 2 + self.vector_y ** 2)


x1, y1 = map(float, input("Введіть координати початкової точки першого вектора: ").split())
x2, y2 = map(float, input("Введіть координати кінцевої точки першого вектора: ").split())
x3, y3 = map(float, input("Введіть координати початкової точки другого вектора: ").split())
x4, y4 = map(float, input("Введіть координати кінцевої точки другого вектора: ").split())
scalar = float(input("Введіть скаляр для множення: "))


p1 = Point(x1, y1)
p2 = Point(x2, y2)
p3 = Point(x3, y3)
p4 = Point(x4, y4)

vector1 = Vector(p1, p2)
vector2 = Vector(p3, p4)

v1_length = vector1.length()
v2_length = vector2.length()

scaled_vector1 = vector1 * scalar
scaled_vector2 = vector2 * scalar

scalar_multiplication = vector1 * vector2

print("Перший вектор:", vector1)
print("Другий вектор:", vector2)
print("Довжина першого вектора:", v1_length)
print("Довжина другого вектора:", v2_length)
print("Множення першого вектора на скаляр:", scaled_vector1)
print("Множення другого вектора на скаляр:", scaled_vector2)
print("Скалярний добуток двох векторів:", scalar_multiplication)
