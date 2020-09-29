class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def inorder_without_recursion(root):

    current = root
    stack = []
    done = 0

    while True:

        if current is not None:

            stack.append(current)
            current = current.left

        elif(stack):
            current = stack.pop()
            print(current.key, end=" ")

            current = current.right

        else:
            break

    print()


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inorder_without_recursion(root)


