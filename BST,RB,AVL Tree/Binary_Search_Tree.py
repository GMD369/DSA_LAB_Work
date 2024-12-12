class Node:
    def __init__(self, key):
        self.key=key
        self.left=None
        self.right=None
        self.parent=None

class BST:
    def __init__(self):
        self.root=None
    
    def insert(self,key):
        if self.root is None:
            self.root=Node(key)
        else:
            self.Insert_recursive(self.root,key)
    
    def Insert_recursive(self,node,key):
        if key<node.key:
            if node.left is None:
                node.left=Node(key)
                node.left.parent=node
            else:
                self.Insert_recursive(node.left,key)
        if key>node.key:
            if node.right is None:
                node.right=Node(key)
                node.right.parent=node
            else:
                self.Insert_recursive(node.right,key)
    
    def search(self,key):
        return self.search_recursive(self.root,key)

    def search_recursive(self,node,key):
        if node is None or node.key==key:
            return node
        elif key<node.key:
            return self.search_recursive(node.left,key)
        elif key >node.key:
            return self.search_recursive(node.right,key)
    
    def inorder_traversal(self):
        self.inorder_traversal_recursive(self.root)
    
    def inorder_traversal_recursive(self,node):
        if node:
            self.inorder_traversal_recursive(node.left)
            print(node.key,end=" ")
            self.inorder_traversal_recursive(node.right)

    def Tree_Max(self):
        return self.Tree_Max_recursive(self.root)
    def Tree_Max_recursive(self,node):
        while node.right:
            node=node.right
        return node.key
    
    def Tree_Min(self):
        return self.Tree_Min_recursive(self.root)
    
    def Tree_Min_recursive(self,node):
        while node.left:
            node=node.left
        return node.key
    
    def Tree_Successor(self,node):
        if node.right:
            return self.Tree_Min_recursive(node.right)
        while node.parent and node==node.parent.right:
            node=node.parent
        return node.parent
    
    def Tree_Predecesor(self,node):
        if node.left:
            return self.Tree_Max_recursive(node.left)
        while node.parent and node==node.parent.left:
            node=node.parent
        return node.parent
    
    
    def _delete_node(self, node,value):
        if self.root is None:
            return None
        elif value<node.key:
            node.left=self._delete_node(node.left,value)
        elif value>node.key:
            node.right=self._delete_node(node.right,value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor=self.Tree_Min_recursive(node.right)
                node.key=successor.key
                node.right=self._delete_node(node.right,successor.key)
            return Node


bst=BST()
values=[20, 10, 30, 5, 15, 25, 35]

for value in values:
    bst.insert(value)

node=bst.search(20)
if node:
    print("Node found with key:", node.key)
    succ=bst.Tree_Successor(node)
    pre=bst.Tree_Predecesor(node)
    print("Successor of node with key",node.key,"is:",succ)
    print("Predecessor of node with key",node.key,"is:",pre)
else:
    print("Node not found")

bst.inorder_traversal()
print("")
print("Tree Maximum: ",bst.Tree_Max())
print("Tree Minimum: ",bst.Tree_Min())
node1=bst.search(10)
if node1:
    print("Node found with key:", node1.key)
    bst._delete_node(node1)
    node2=bst.search(15)
    if node2:
        print("Node not deleted")
    else:
        print("Node deleted")
else:
    print("Node not found")

