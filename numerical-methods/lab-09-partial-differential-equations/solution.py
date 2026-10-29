import numpy as np
import matplotlib.pyplot as plt
import math

h = 0.05
N = int(1 / h)

x = np.linspace(0, 1, N + 1)
y = np.linspace(0, 1, N + 1)

U = np.zeros((N + 1, N + 1))

# граничні умови
# AD: y = 0
U[:, 0] = 0

# BC: y = 1
U[:, N] = 0

# AB: x = 0
for j in range(N + 1):
    U[0, j] = y[j] * (0.5 - y[j])

# CD: x = 1
for j in range(N + 1):
    U[N, j] = math.sin(2 * math.pi * y[j])

# кути
U[0, 0] = 0
U[N, 0] = 0
U[0, N] = 0
U[N, N] = 0

# кількість внутрішніх вузлів
M = (N - 1) * (N - 1)

A = np.zeros((M, M))
B = np.zeros(M)

def index(i, j):
    return (j - 1) * (N - 1) + (i - 1)

for i in range(1, N):
    for j in range(1, N):
        row = index(i, j)

        A[row, row] = 4

        neighbors = [
            (i + 1, j),
            (i - 1, j),
            (i, j + 1),
            (i, j - 1)
        ]

        for ni, nj in neighbors:
            if 1 <= ni <= N - 1 and 1 <= nj <= N - 1:
                A[row, index(ni, nj)] = -1
            else:
                B[row] += U[ni, nj]

solution = np.linalg.solve(A, B)

# записуємо знайдені значення у сітку
for i in range(1, N):
    for j in range(1, N):
        U[i, j] = solution[index(i, j)]

# графік
X, Y = np.meshgrid(x, y)

plt.figure(figsize=(8, 6))
plt.contourf(X, Y, U.T, levels=30)
plt.colorbar(label="u(x,y)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Розв'язок рівняння Лапласа методом сіток")
plt.show()
# 3d
fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, U.T)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("u(x,y)")
ax.set_title("Поверхня розв'язку")
plt.show()
