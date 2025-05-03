import stack

class Queue_wStack():
    def __init__(self):
        self.stack1 = stack.Stack(200)
        self.stack2 = stack.Stack(200)
    def enqueue(self,item):
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())
        self.stack1.push(item)
        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())


    def dequeue(self):
        if self.stack1.is_empty():
            print("queue is empty")
        else:
            return self.stack1.pop()
        
    def display_queue(self):
        print(self.stack1.stack[::-1])

queue1 = Queue_wStack()
queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)
queue1.enqueue(4)
queue1.dequeue()
queue1.dequeue()
queue1.display_queue()


