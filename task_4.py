class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1 


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                node.right = self._insert_recursive(node.right, value)
        else:
            return node 



class AVLTree(BinaryTree):
    def get_height(self, node):
        
        if not node:
            return 0
        return node.height

    def update_height(self, node):
        
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_balance(self, node):
        
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, z):
        
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        
        self.update_height(z)
        self.update_height(y)

        return y 

    def right_rotate(self, y):
        
        x = y.left
        T3 = x.right

        x.right = y
        y.left = T3

        self.update_height(y)
        self.update_height(x)

        return x

    def rebalance(self, node):
        
        self.update_height(node)
        balance = self.get_balance(node)

        
        if balance > 1:
            if self.get_balance(node.left) < 0:
                node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        
        if balance < -1:
            if self.get_balance(node.right) > 0:
                node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def _insert_recursive(self, node, value):
        
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                node.right = self._insert_recursive(node.right, value)
        else:
            return node 

        return self.rebalance(node)

    def insert(self, value):
    
        if self.root is None:
            self.root = Node(value)
        else:
            self.root = self._insert_recursive(self.root, value)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=' ')
        inorder(root.right)

#пример

avl = AVLTree()

values = [10, 20, 30, 40, 50, 25]

for v in values:
    avl.insert(v)

inorder(avl.root)  
print()


