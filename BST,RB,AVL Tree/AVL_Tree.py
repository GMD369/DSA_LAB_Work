class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Height of node for balancing

 
 
class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        # Call the recursive _insert method starting from the root
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        # Step 1: Perform normal BST insertion
        if root is None:
            return Node(key)
        elif key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)

        # Step 2: Update height of the ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Step 3: Get the balance factor
        balance = self.get_balance(root)

        # Step 4: If the node becomes unbalanced, then there are 4 cases

        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Return the new root
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Return the new root
        return y

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def in_order_traversal(self):
        self._in_order_recursive(self.root)

    def _in_order_recursive(self, node):
        if node:
            self._in_order_recursive(node.left)
            print(node.key, end=' ')
            self._in_order_recursive(node.right)


# Example usage:
avl_tree = AVLTree()

# Inserting nodes
values = [30, 20, 10, 5, 25, 40, 35, 50]
for value in values:
    avl_tree.insert(value)

print("In-order traversal of the AVL tree:")
avl_tree.in_order_traversal()  # Output should be a sorted sequence of keys
