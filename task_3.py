class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder(root):
    
    if root:
        print(root.value, end=' ')
        preorder(root.left)
        preorder(root.right)


def inorder(root):
   
    if root:
        inorder(root.left)
        print(root.value, end=' ')
        inorder(root.right)


def postorder(root):
    
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=' ')



root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(8)

print("Прямой обход (preorder):")
preorder(root)
print("\n")

print("Симметричный обход (inorder):")
inorder(root)
print("\n")

print("Обратный обход (postorder):")
postorder(root)
print()