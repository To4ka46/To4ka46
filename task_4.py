class Graph:
    def __init__(self, directed=False):
       
        self.graph = {}
        self.directed = directed

    def create_from_edges(self, edges):
      
        for u, v in edges:
            self._add_edge(u, v)

    def _add_edge(self, u, v):
    
        if u not in self.graph:
            self.graph[u] = []
        if not self.directed and v not in self.graph:
            self.graph[v] = []
        
        self.graph[u].append(v)
        
        if not self.directed:
            self.graph[v].append(u)

    def add_vertex(self, vertex):
        
        if vertex not in self.graph:
            self.graph[vertex] = []
        else:
            print(f"")

    def add_edge(self, u, v):
       
        if u not in self.graph:
            print(f"")
            return
        if v not in self.graph and not self.directed:
            print(f"")
            return
        
        self._add_edge(u, v)

    def display(self):
        if not self.graph:
            return
        
        print("")
        for vertex in sorted(self.graph.keys()):
            neighbors = sorted(self.graph[vertex])
            print(f"{vertex}: {neighbors}")


#пример:

g = Graph(directed=False)
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (1, 3)]

g.create_from_edges(edges)
g.display()

g.add_vertex(4)
g.display()

g.add_edge(1, 4)
g.display()

print("")
dg = Graph(directed=True)
dg.create_from_edges([(0, 1), (1, 2), (2, 3)])
dg.display()
