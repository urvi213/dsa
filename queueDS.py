class Queue_DS():
    def __init__(self,max_size):
        self.queue = []
        self.max_size = max_size
    def enqueue(self,item):
        if self.size() < self.max_size:
            self.queue.append(item)
        else:
            print("queue is full")
    def dequeue(self):
        if self.is_empty():
            return "queue is empty"
        else:
            return self.queue.pop(0)
    def front(self):
        if self.is_empty(): return "queue is empty"
        else: return self.queue[0]
    def rear(self):
        if self.is_empty(): return "queue is empty"
        else: return self.queue[-1]
    def is_empty(self):
        if self.size() == 0: return True
        else: return False
    def size(self):
        return len(self.queue)
    def display(self):
        print(self.queue)
    

"""queue1 = Queue_DS(5)
for i in range(3):
    queue1.enqueue(i)
queue1.display()
print(queue1.front())
print(queue1.rear())
queue1.dequeue()
queue1.display()"""
