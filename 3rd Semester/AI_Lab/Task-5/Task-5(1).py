## DFS with Stack and Node 

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

def dfs_stack(start_node):
    visited = set()  
    stack = [start_node]  

    while stack:
        current_node = stack.pop()  
        
        if current_node not in visited:
            print(current_node.value)  
            visited.add(current_node)
            
            for neighbor in current_node.neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node3]
node2.neighbors = [node4]
node3.neighbors = [node4]

dfs_stack(node1)
