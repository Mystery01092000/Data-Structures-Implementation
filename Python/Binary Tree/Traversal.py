class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def inorder(root):

    if root:

        inorder(root.left)
        print(root.value)
        inorder(root.right)

def postorder(root):

    if root:

        postorder(root.left)

        postorder(root.right)

        print(root.value)

def preorder(root):

    if root:

        print(root.value)

        preorder(root.left)

        preorder(root.right)



root = Node(1)

root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

inorder(root)
print("-----------------------------")
postorder(root)
print("------------------------------")
preorder(root)
