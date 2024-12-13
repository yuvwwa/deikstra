from deikstra import Graph

graph = {
    'A': {'B':10, 'C':6, 'D':8},
    'B': {'G':11, 'D':5}, 
    'C': {'E':3},
    'D': {'C':2, 'E':5, 'F':7, 'G':12},
    'E': {'F':9, 'I':12},
    'F': {'H':8, 'I':10},
    'G': {'F':4, 'H':6},
    'H': {'I':5},
    'I': {'I':0}
}

graph0 = Graph(graph)
result, previous = graph0.deikstra('A')

print(graph0.full_path(previous, 'A', 'I'))


for vertex, distance in result.items():
    print(f"{vertex}: {distance}")
