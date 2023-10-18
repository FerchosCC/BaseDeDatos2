#10/10/23
class Node:
    def __init__(self, data):
        self.left = Node
        self.right = Node
        self.data = data
def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)
def postorden(node):
    if node:
        postorden(node.left)
        postorden(node.right)
        print(node.data)


root = Node(10)

root.left = Node(34)
root.right = Node(89)
root.left.left = Node(45)
print(preorder(root))