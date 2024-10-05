## BFS with queue and node

from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

def bfs_queue(start_node):
    visited = set()
    queue = deque([start_node])
    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            print(current_node.value)
            visited.add(current_node)
            for neighbor in current_node.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node1.neighbors = [node2, node3]
node2.neighbors = [node4, node5]

bfs_queue(node1)


