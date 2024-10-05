## Inorder,Preorder and Postorder and implement in DFS

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder_traversal(node):     # Inorder Traversal (Left, Root, Right)
    if node:
        inorder_traversal(node.left)  
        print(node.value)  
        inorder_traversal(node.right) 

def preorder_traversal(node):  # Preorder Traversal (Root, Left, Right)    
    if node:
        print(node.value) 
        preorder_traversal(node.left) 
        preorder_traversal(node.right) 

def postorder_traversal(node):  # Postorder Traversal (Left, Right, Root)
    if node:
        postorder_traversal(node.left)  
        postorder_traversal(node.right) 
        print(node.value) 


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Inorder Traversal:")
inorder_traversal(root)
print()

print("\nPreorder Traversal:")
preorder_traversal(root)
print()


print("\nPostorder Traversal:")
postorder_traversal(root)
