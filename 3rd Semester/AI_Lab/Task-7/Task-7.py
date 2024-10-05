## Code of A* Algorithm

class Node:
    def __init__(self, value, g_cost=0, h_cost=0):
        self.value = value
        self.g_cost = g_cost  
        self.h_cost = h_cost 
        self.f_cost = g_cost + h_cost 
        self.neighbors = []

def a_star(start, goal):
    open_list = [start] 
    closed_list = []  

    while open_list:
        open_list.sort(key=lambda x: x.f_cost)
        current_node = open_list.pop(0)

        if current_node == goal:
            return reconstruct_path(goal)

        closed_list.append(current_node)

        for neighbor, cost in current_node.neighbors:
            if neighbor in closed_list:
                continue

            tentative_g_cost = current_node.g_cost + cost

            if neighbor not in open_list:
                open_list.append(neighbor)
            elif tentative_g_cost >= neighbor.g_cost:
                continue

            neighbor.g_cost = tentative_g_cost
            neighbor.f_cost = neighbor.g_cost + neighbor.h_cost 

def reconstruct_path(goal):
    path = []
    current = goal
    while current:
        path.append(current.value)
        current = current.parent if hasattr(current, 'parent') else None
    return path[::-1]

nodeA = Node('A', h_cost=4)
nodeB = Node('B', h_cost=2)
nodeC = Node('C', h_cost=1)
nodeD = Node('D', h_cost=0) # Goal Node is D

nodeA.neighbors = [(nodeB, 1), (nodeC, 3)]
nodeB.neighbors = [(nodeD, 1)]
nodeC.neighbors = [(nodeD, 1)]

path = a_star(nodeA, nodeD)
print(path)
