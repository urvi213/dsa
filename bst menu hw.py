class Tree_Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def insert(node,item):
    if not node:
        return Tree_Node(item)
    if item < node.value:
        node.left  = insert(node.left,item)
    else:
        node.right = insert(node.right,item)
    return node

def search(node,item):
    if item == node.value:
        return True
    elif item < node.value and node.left:
        return search(node.left,item)
    elif item > node.value and node.right:
         return search(node.right,item)
    else: 
        return False
    
def inorder_traversal(node):
    if node.left:
        inorder_traversal(node.left)
    print(node.value)
    if node.right:
        inorder_traversal(node.right)

def postorder_traversal(root_node):
    if root_node.left:
        postorder_traversal(root_node.left)
    if root_node.right:
        postorder_traversal(root_node.right)
    print(root_node.value)

def preorder_traversal(root_node):
    print(root_node.value)
    if root_node.left:
        preorder_traversal(root_node.left)
    if root_node.right:
        preorder_traversal(root_node.right)

def find_inordersuccessor(node):
    successor = node.right
    while successor.left:
        successor = successor.left
    return successor

def delete(root,item):
    if root is None:
        return root
    if root.value > item:
        root.left = delete(root.left,item)
    elif root.value < item:
        root.right = delete(root.right,item)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        successor = find_inordersuccessor(root)
        root.value = successor.value
        root.right = delete(root.right,successor.value)
    return root



BSTs = {}
run = True

while run:
    option = input("\n1 - create BST\n2 - insert node \n3 - search for node \n4 - inorder traversal \n5 - preorder traversal \n6 - postorder traversal \n7 delete node \n8 - end: ")

    if option == "1":
        #input("name of bst? ") = Tree_Node(input("value of node? "))
        BSTs[input("name of bst? ")] = Tree_Node(int(input("value of node? ")))

    elif option == "2":
        current_BST = input("which BST to insert to? ")
        if current_BST in BSTs:
            insert(BSTs[current_BST],int(input("item to insert? ")))
        else:
            print("BST doesnt exist")

    elif option == "3":
        current_BST = input("which BST to search? ")
        if current_BST in BSTs:
            if search(BSTs[current_BST],int(input("item to search for? "))):
                print("item exists in BST")
            else:
                print("item does not exist in BST")
        else:
            print("BST doesn't exist")

    elif option == "4":
        current_BST = input("which BST to inorder transverse? ")
        if current_BST in BSTs:
            inorder_traversal(BSTs[current_BST])
        else:
            print("BST doesn't exist")

    elif option == "5":
        current_BST = input("which BST to preorder transverse? ")
        if current_BST in BSTs:
            preorder_traversal(BSTs[current_BST])
        else:
            print("BST doesn't exist")

    elif option == "6":
        current_BST = input("which BST to postorder transverse? ")
        if current_BST in BSTs:
            postorder_traversal(BSTs[current_BST])
        else:
            print("BST doesn't exist")

    elif option == "7":
        current_BST = input("which BST to delete an item from ? ")
        if current_BST in BSTs:
            delete(BSTs[current_BST],int(input("which item to delete? ")))
        else:
            print("BST doesn't exist")

    elif option == "8":
        run = False
    else:
        print("invalid")
