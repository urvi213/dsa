class Stack():
    def __init__(self,max_size):
        self.stack = []
        self.max_size = max_size
    def push(self,item):
        if self.size() < self.max_size:
            self.stack.append(item)
        else:
            print("stack is full")
    def pop(self): # removes and returns top item
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("stack is empty")
    def top(self): # returns top without removing it
        if self.is_empty(): return "stack is empty"
        else:
            return self.stack[-1] # negative index is last item
    def is_empty(self):
        if self.size() > 0: return False
        else: return True
    def size(self):
        return len(self.stack)
    def display(self):
        print(self.stack)
    
#stack1 = Stack()
#for i in range(6):
  #  stack1.push(i)
#print(stack1.size())
#print(stack1.top())
