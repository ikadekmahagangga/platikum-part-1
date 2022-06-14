print("NIM : 21101203")              
print("Nama : I Kadek Maha Gangga")  
print("Kelas : Q")                   
vertices = {"A", "B", "C", "D", "E", "F"}
edges = {("A", "D"), ("A", "B"), ("A", "E"), ("A", "F"), ("B", "F"), ("B", "C")}
graph = dict()
for vertex in vertices:
    graph[vertex] = []
for edge in edges:
    v1 = edge[0]
    v2 = edge[1]
    graph[v1].append(v2)
    graph[v2].append(v1)
print("The given set of vertices is:", vertices)
print("The given set of edges is:", edges)
print("Graph representation in python is:")
print(graph)

#referensi https://www.pythonforbeginners.com/data-structures/graph-in-python
#ini adalah codingan basic dari graph sederhana