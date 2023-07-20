def find(parent,i):
    if parent[i] == i:
        return i
    return find(parent,parent[i])

def union(parent,rank,x,y):
    root_x = find(parent,x)
    root_y = find(parent,y)
    
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1

def kruskal(graph):
    edges = []
    mst = []
    
    parent = {vertex: vertex for vertex in graph}
    rank = {vertex: 0 for vertex in graph}
    
    for u in graph:
        for v,weight in graph[u]:
            edges.append((u,v,weight))
    
    edges.sort(key = lambda x:x[2])
    
    for u,v,weight in edges:
        root_u = find(parent,u)
        root_v = find(parent,v)
        
        if root_u != root_v:
            mst.append((u,v,weight))
            union(parent,rank,root_u,root_v)
    return mst

g = {
    '1': [('5', 5), ('2', 10)],
 '2': [('1', 10), ('3', 1), ('4', 6)],
 '3': [('2', 1), ('4', 2), ('5', 7)],
 '4': [('5', 3), ('2', 6), ('3', 2)],
 '5': [('1', 5), ('3', 7), ('4', 3)]
}
cost = kruskal(g)
for edge in cost:
    print(edge)
