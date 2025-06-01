import queueDS
import stack

class Graph():
    def __init__(self,amount):
        self.n = amount
        self.adjacency_lists = [[] for i in range(self.n)] # list comprehension
    def create_edge(self,nodeA,nodeB):
        self.adjacency_lists[nodeA].append(nodeB)
        self.adjacency_lists[nodeB].append(nodeA)
        #print(self.adjacency_lists)


    def bfs(self,source): # breadth first search - finds all neighbour nodes then moves on.
        visited = []
        result = []
        queue = queueDS.Queue_DS(self.n)
        queue.enqueue(source)
        visited.append(source)
        while not queue.is_empty():
            node = queue.dequeue() # empties queue into result
            result.append(node)
            
            for n in self.adjacency_lists[node]:
                if n not in visited:
                    queue.enqueue(n)
                    visited.append(n)
        return result
    
    def bfs_calculatedistance(self,source):
        distances = [0 for i in range(self.n)]
        visited = []
        result = []
        queue = queueDS.Queue_DS(self.n)
        queue.enqueue(source)
        visited.append(source)
        while not queue.is_empty():
            node = queue.dequeue()
            result.append(node)

            for n in self.adjacency_lists[node]:
                if n not in visited:
                    distances[n] = distances[node]+1 # distance of current node is distance of previous node = 1
                    queue.enqueue(n)
                    visited.append(n)                    

        return result, distances # distances list returns in chronolgoical order of node values, though calculated in order of breadth first search
    


    


    

graph1 = Graph(10)
#print(graph1.adjacency_lists)
graph1.create_edge(0,2)
graph1.create_edge(0,3)
graph1.create_edge(4,1)
graph1.create_edge(2,3)
graph1.create_edge(3,1)
graph1.create_edge(9,1)
graph1.create_edge(8,5)
graph1.create_edge(7,5)
graph1.create_edge(6,3)
graph1.create_edge(4,8)

print(graph1.bfs(0))
print(graph1.bfs_calculatedistance(0)[1])
