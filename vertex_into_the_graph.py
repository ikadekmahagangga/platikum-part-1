graph = {'A': ['B', 'D', 'E', 'F'], 'D': ['A'], 'B': ['A', 'F', 'C'], 'F': ['B', 'A'], 'C': ['B'], 'E': ['A']}
print("Original Graph representation is:")
print(graph)
# insert vertex G
graph["G"] = []
print("The new graph after inserting vertex G is:")
print(graph)

#link https://www.pythonforbeginners.com/data-structures/graph-operations-in-python