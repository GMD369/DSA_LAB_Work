from collections import deque

# Graph represented as adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# DFS Function
def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")  # Process the node
        visited.add(node)  # Mark as visited
        for neighbor in graph[node]:  # Explore neighbors
            dfs(graph, neighbor, visited)

# BFS Function
def bfs(graph, start):
    visited = set()
    queue = deque([start])  # Initialize queue with start node
    while queue:
        node = queue.popleft()  # Dequeue the next node
        if node not in visited:
            print(node, end=" ")  # Process the node
            visited.add(node)  # Mark as visited
            for neighbor in graph[node]:  # Enqueue neighbors
                if neighbor not in visited:
                    queue.append(neighbor)

# Run DFS and BFS
print("DFS Traversal:")
dfs(graph, 'A', set())

print("\nBFS Traversal:")
bfs(graph, 'A')
