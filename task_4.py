import math

def floyd_warshall(graph):
    
    n = len(graph)
    dist = [row[:] for row in graph]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

# Пример
if __name__ == "__main__":
    graph = [
        [0,      5,      math.inf, 10    ],
        [math.inf, 0,      3,      math.inf],
        [math.inf, math.inf, 0,      1     ],
        [math.inf, math.inf, math.inf, 0     ]
    ]
    
    shortest_paths = floyd_warshall(graph)
    
    print("Матрица кратчайших расстояний:")
    for row in shortest_paths:
        print([f"{x:4}" if x != math.inf else " inf" for x in row])
