from collections import deque

def bfs(adj,s,visited):
    queue = deque()
    queue.append(s)
    visited[s] = True
    while queue:
        u = queue.popleft()
        print(u,end=" ")
        for v in adj[u]:
            if not visited[v]:
                visited[v]=True
                queue.append(v)

def add_edge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)

def disconnected(adj):
    visited = [False] * len(adj)
    for i in range(len(adj)):
        if not visited[i]:
            bfs(adj,i,visited)

V=6
adj = [[] for i in range(V)]
add_edge(adj, 0, 1)
add_edge(adj, 0, 2)
add_edge(adj, 3, 4)
add_edge(adj, 4, 5)


disconnected(adj)

