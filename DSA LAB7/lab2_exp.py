





graph = { 
    '5' : ['3', '7'], 
    '3' : ['2', '4'], 
    '7' : ['8'], 
    '2' : [], 
    '4' : ['8'], 
    '8' : [] 
}


visited = set()

# Function for DFS
def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ") 
        visited.add(node)      
        
        # Visit all the adjacent nodes recursively
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search:")
dfs(visited, graph, '5')
