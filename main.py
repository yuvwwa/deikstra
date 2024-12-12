from deikstra import Graph

graph = {
    'A': {'B':6, 'C':10, 'F':1},
    'B': {'C':8, 'D':5}, 
    'C': {'D':9, 'F':11},
    'D': {'E':4,},
    'E': {'F':3},
    'F': {'B':7}
}

graph0 = Graph(graph)
result = graph0.deikstra('A')

for vertex, distance in result.items():
    print(f"{vertex}: {distance}")
