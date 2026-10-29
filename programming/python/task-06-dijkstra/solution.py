#варіант 6 (16)

#Реалізувати алгоритм Дейкстра по знаходженню найкоротших шляхів від заданої вершини графа до всіх інших


import heapq

graph = {
    'A': [('B', 14), ('C', 9), ('D', 7)],
    'D': [('A', 7), ('C', 10), ('E', 15)],
    'C': [('A', 9), ('B', 2), ('D', 10), ('E', 11)],
    'B': [('A', 14), ('C', 2), ('P', 9)],
    'P': [('B', 9), ('E', 6)],
    'E': [('D', 15), ('C', 11), ('P', 6)]
}


def distances(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    previous = {vertex: None for vertex in graph}
    queue = [(0, start)]

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(queue, (distance, neighbor))

    return distances, previous

def path(previous, start, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    return path if path[0] == start else []




start_node = input("Введіть назву початкової вершини: ")
if start_node not in graph:
    print(f"Вершина '{start_node}' не існує в графі.")
else:
    distances, previous = distances(graph, start_node)
    print(f"\nНайкоротші відстані від вершини {start_node}:")
    for vertex in sorted(graph):
        print(f"{start_node} → {vertex}: {distances[vertex]} шлях: {path(previous, start_node, vertex)}")
