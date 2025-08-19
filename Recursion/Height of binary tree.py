class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def heightofBinaryTree(root):
    if root is None:
        return 0
    Hleft = heightofBinaryTree(root.left)
    Hright = heightofBinaryTree(root.right)

    return max(Hleft, Hright) + 1

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Height of tree:", heightofBinaryTree(root))
