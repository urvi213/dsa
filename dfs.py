import stack

class Graph():
    def __init__(self,amount):
        self.n = amount
        self.adjacency_lists = [[] for i in range(self.n)] # list comprehension
    def create_edge(self,nodeA,nodeB):
        self.adjacency_lists[nodeA].append(nodeB)
        self.adjacency_lists[nodeB].append(nodeA)
        #print(self.adjacency_lists)

    def dfs(self,source): # depth first search - explore all of one neighbours neighbours before moving to next
        stack1 = stack.Stack(self.n)
        visited = []
        stack1.push(source)
        while not stack1.is_empty():
            node = stack1.pop()
            visited.append(node)
            for n in self.adjacency_lists[node]:
                if n not in visited and n not in stack1.stack:
                    stack1.push(n)
        return visited
    
    def dfs_start(self):
        visited = [False for i in range(self.n)]
        self.recursive_dfs(0,visited)

    def recursive_dfs(self,source,visited):
        visited[source] = True
        print(source)
        for n in self.adjacency_lists[source]:
            if not visited[n]:
                self.recursive_dfs(n,visited)

    def check_path(self,a,b):
        path_exists = False
        stack1 = stack.Stack(self.n)
        visited = []
        stack1.push(a)
        while not stack1.is_empty():
            node = stack1.pop()
            visited.append(node)
            for n in self.adjacency_lists[node]:
                if n not in visited and n not in stack1.stack:
                        stack1.push(n)
                if n == b:
                    #print("exists")
                    path_exists = True
        #return visited
        return path_exists


graph1 = Graph(15)
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
graph1.create_edge(11,12)

print(graph1.dfs(0))
print(graph1.dfs_start())
print(graph1.check_path(0,8))
print(graph1.check_path(0,11))
print(graph1.check_path(3,4))
