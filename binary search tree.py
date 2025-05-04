# tree where left is smaller than node and right is greater than node

class Tree_Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(node):
    if node.left:
        inorder_traversal(node.left)
    print(node.value)
    if node.right:
        inorder_traversal(node.right)

def insert(node,item):
    if not node:
        return Tree_Node(item) # code ends at return
    if item < node.value:
        node.left = insert(node.left,item)
    else:
        node.right = insert(node.right,item)
    return node


def search(item,node):
    if item == node.value:
        return True
    elif item < node.value and node.left:
        return search(item,node.left)
    elif item > node.value and node.right:
        return search(item,node.right)
    else:
        return False


root = None
amount = int(input("how many nodes ? "))
for i in range(amount):
    answer = int(input("whats the value of node {} ? ".format(i+1)))
    root = insert(root,answer) 

inorder_traversal(root)

for i in range(3):
    print(search(int(input("search for? ")),root))