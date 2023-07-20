import heapq
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self,u,v,weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
            
        self.graph[u].append((v,weight))
        self.graph[v].append((u,weight))
    
    def prim(self):
        start_node = next(iter(self.graph))
        cost = 0
        visited = set()
        priority_queue = [(0,start_node)]
        
        while priority_queue:
            current_cost,current_node = heapq.heappop(priority_queue)
            
            if current_node in visited:
                continue
            
            visited.add(current_node)
            cost += current_cost 
            
            for neighbor,weight in self.graph[current_node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue,(weight,neighbor))
        return cost
g = Graph()
g.add_edge(1,2,4)
g.add_edge(1,4,8)
g.add_edge(2,3,3)
g.add_edge(2,4,1)
g.add_edge(3,4,7)
g.add_edge(3,6,8)
g.add_edge(4,6,3)

min_cost = g.prim()
print(min_cost)
#Include an extra function to compute the minimum spanning tree using Prim's algorithm
