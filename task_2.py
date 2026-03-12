from collections import deque

def bfs(graph, start_vertex):
    
    if start_vertex not in graph:
        print(f"Вершина {start_vertex} отсутствует в графе.")
        return []

    visited = set()  
    queue = deque([start_vertex])
    order = [] 

    visited.add(start_vertex)

    while queue:
        vertex = queue.popleft()
        order.append(vertex)

        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order

#пример:

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start = 'A'
result = bfs(graph, start)

print(f"\nНачало обхода с вершины '{start}'")
print("Порядок обхода (BFS):")
print(" → ".join(result))