class DirectedGraph:

    def __init__(self):
        self.graph = {} 

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        
        if from_vertex not in self.graph:
            self.add_vertex(from_vertex)
        if to_vertex not in self.graph:
            self.add_vertex(to_vertex)

        
        if to_vertex not in self.graph[from_vertex]:
            self.graph[from_vertex].append(to_vertex)

    def display(self):
        
        print("\n Текущий ориентированный граф:")
        if not self.graph:
            print("  Граф пуст.")
            return
        for vertex, neighbors in self.graph.items():
            if neighbors:
                print(f"  {vertex} → {', '.join(map(str, neighbors))}")
            else:
                print(f"  {vertex} → []")


dg = DirectedGraph()

    
dg.add_vertex("A")
dg.add_vertex("B")
dg.add_vertex("C")

dg.add_edge("A", "B")
dg.add_edge("B", "C")
dg.add_edge("A", "C")
dg.add_edge("C", "B")  
dg.add_edge("A", "B") 

    
dg.display()

