from dfs import Graph
from stack import Stack

graph = Graph()

my_vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
# add verices
for i in range(len(my_vertices)):
    graph.add_vertex(my_vertices[i])


graph.add_edge('A','B') # A -> B
graph.add_edge('A','C') # A -> B A-> C
graph.add_edge('A', 'D')# A -> B, A-> C, A->D
graph.add_edge('C', 'D')# C->D
graph.add_edge('C', 'G')# C -> G
graph.add_edge('D', 'G')# D -> G
graph.add_edge('D', 'H')# D -> H
graph.add_edge('B', 'E') # B -> E
graph.add_edge('B', 'F') # B -> F
graph.add_edge('E', 'I') # E -> I

graph.dfs("B")
print(graph.return_path("C"))


