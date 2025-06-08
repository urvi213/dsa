import stack

class Graph():
    def __init__(self,max):
        self.n = max
        self.adjacency_lists = [[] for i in range(max)]
    def create_edge(self,a,b):
        self.adjacency_lists[a].append(b)
        self.adjacency_lists[b].append(a)
    def detect_cycle(self):
        visited = [False for i in range(self.n)]
        for i in range(self.n):
            if not visited[i]:
                if self.cycle_util(i,visited,-1):
                    return True
        return False

    def cycle_util(self,node,visited,parent): # utility functions - help you with another function
        visited[node] = True
        for adjacent_node in self.adjacency_lists[node]:
            if not visited[adjacent_node]:
                if self.cycle_util(adjacent_node,visited,node):
                    return True
            elif adjacent_node != parent: # i has been visited but isn't the node's parent - there's a cycle
                return True
        return False

    
graph1 = Graph(13)
graph1.create_edge(0,2)
graph1.create_edge(0,3)
graph1.create_edge(4,1)
#graph1.create_edge(2,3)
graph1.create_edge(3,1)
graph1.create_edge(9,1)
graph1.create_edge(6,3)
graph1.create_edge(4,8)
graph1.create_edge(9,10)
graph1.create_edge(10,8)
graph1.create_edge(5,7)
graph1.create_edge(11,12)

print(graph1.detect_cycle())
