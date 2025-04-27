class Tree_Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(root_node): # left,parent,right
    if root_node.left is not None:
        inorder_traversal(root_node.left)
    print(root_node.value) # prints parent
    if root_node.right is not None:
        inorder_traversal(root_node.right)

def preorder_transversal(root_node): # parent, left, right
    print(root_node.value)
    if root_node.left is not None:
        preorder_transversal(root_node.left)
    if root_node.right is not None:
        preorder_transversal(root_node.right)

def postorder_transversal(root_node): # left,right,parent
    if root_node.left is not None:
        postorder_transversal(root_node.left)
    if root_node.right is not None:
        postorder_transversal(root_node.right)
    print(root_node.value)
    

root = Tree_Node(5)
root.left = Tree_Node(3)
root.right = Tree_Node(4)
root.left.left = Tree_Node(2)
root.left.right = Tree_Node(6)
root.right.left = Tree_Node(7)
root.right.right = Tree_Node(8)

inorder_traversal(root)
print("")
preorder_transversal(root)
print("")
postorder_transversal(root)