class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def height(node):

    if node is None:
        return 0

    return 1 + max(height(node.left), height(node.right))


def diameter(root):

    if root is None:
        return 0

    lh = height(root.left)
    rh = height(root.right)

    ldia = diameter(root.left)
    rdia = diameter(root.right)

    return max(lh + rh + 1, max(ldia, rdia))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(diameter(root))