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
    
def find_inorder_successor(node):
    successor = node.right
    while successor.left:
        successor = successor.left # the left gets smaler and smaller, while still being smaller than the first right but greater than the node
    return successor

def delete(root,item):
    if root is None:
        return root
    if root.value > item:
        root.left = delete(root.left,item) # delete happening at left of parent changes left of parent
    elif root.value < item:
        root.right = delete(root.right,item)
    else: # item equals root
        if not root.left:
            return root.right
        if not root.right:
            return root.left # takes care of node with no children or with 1 child.
        successor = find_inorder_successor(root)
        root.value = successor.value
        root.right = delete(root.right,successor.value)
    return root


root = None
amount = int(input("how many nodes ? "))
for i in range(amount):
    answer = int(input("whats the value of node {} ? ".format(i+1)))
    root = insert(root,answer) 

inorder_traversal(root)

#for i in range(3):
    #print(search(int(input("search for? ")),root))

delete(root,int(input("item to be deleted: ")))
inorder_traversal(root)
