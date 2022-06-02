graph = {'A': ['B', 'D', 'E', 'F'], 'D': ['A'], 'B': ['A', 'F', 'C'], 'F': ['B', 'A'], 'C': ['B'], 'E': ['A']}
print("Graph representation in python is:")
print(graph)
edges = []
for vertex in graph:
    for adjacent_vertex in graph[vertex]:
        edge = {vertex, adjacent_vertex}
        if edge not in edges:
            edges.append(edge)

print("Edges in the graph are:", edges)


# link https://www.pythonforbeginners.com/data-structures/graph-operations-in-python