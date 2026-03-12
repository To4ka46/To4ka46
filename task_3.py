class Graph:
    def __init__(self):
        
        self.adj_matrix = []
        self.vertices = set()


    def create_from_edges(self, edges, directed=False):
        
        for u, v in edges:
            self.vertices.add(u)
            self.vertices.add(v)
        
        
        sorted_vertices = sorted(self.vertices)
        n = len(sorted_vertices)
        
        self.adj_matrix = [[0] * n for _ in range(n)]
        
        for u, v in edges:
            i = sorted_vertices.index(u)
            j = sorted_vertices.index(v)
            self.adj_matrix[i][j] = 1
            if not directed:
                self.adj_matrix[j][i] = 1

    def add_vertex(self, vertex):
        
        if vertex in self.vertices:
            return
        
        self.vertices.add(vertex)
        sorted_vertices = sorted(self.vertices)
        n = len(sorted_vertices)
        
        for row in self.adj_matrix:
            row.append(0)
        self.adj_matrix.append([0] * n)

    def add_edge(self, u, v, directed=False):
        
        if u not in self.vertices:
            return
        if v not in self.vertices:
            return
        
        sorted_vertices = sorted(self.vertices)
        i = sorted_vertices.index(u)
        j = sorted_vertices.index(v)
        
        self.adj_matrix[i][j] = 1
        if not directed:
            self.adj_matrix[j][i] = 1

    def display(self):
    
        if not self.adj_matrix:
            print("")
            return
        
        sorted_vertices = sorted(self.vertices)
        print("")
        print("  ", " ".join(map(str, sorted_vertices)))
        for idx, row in enumerate(self.adj_matrix):
            print(sorted_vertices[idx], " ", " ".join(map(str, row)))


#пример:

g = Graph()

edges = [(0, 1), (1, 2), (2, 3), (3, 0)]

g.create_from_edges(edges, directed=False)
g.display()
g.add_vertex(4)
g.display()
g.add_edge(1, 4, directed=False)
g.display()