#варіант 7 (16)

from collections import deque
a = [
    [2, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 3]
]
for row in a:
    print(*row)
rows, cols = len(a), len(a[0])

directions = [
(-1, 0), (1, 0), (0, -1), (0, 1)
]

for i in range(rows):
    for j in range(cols):
        if a[i][j] == 2:
            start = (i, j)

queue = deque([(start, [start])])
visited = set([start])             

while queue:
    (x, y), path = queue.popleft()
    if a[x][y] == 3:        
        print("Шлях:", path)
        
        for px, py in path:
            if a[px][py] not in [2, 3]:
                a[px][py] = '+'
                
        for row in a:
            print(*row)
        break


    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            if a[nx][ny] != 1 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))
