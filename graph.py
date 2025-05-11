class Graph():
    def __init__(self,amount):
        self.n = amount
        self.adjacency_lists = [[] for i in range(self.n)] # list comprehension
        #print(self.adjacency_lists)

graph1 = Graph(5)