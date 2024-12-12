import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(vertices)}  # Adjacency list

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def prim(self):
        visited = [False] * self.V
        min_heap = [(0, 0)]  # (weight, vertex)
        mst_cost = 0
        mst_edges = []

        while min_heap:
            weight, u = heapq.heappop(min_heap)

            if visited[u]:
                continue

            visited[u] = True
            mst_cost += weight
            for v, w in self.graph[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (w, v))
                    mst_edges.append((u, v, w))

        return mst_cost, mst_edges

# Example Usage
g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

mst_cost, mst_edges = g.prim()
print(f"Minimum Spanning Tree Cost: {mst_cost}")
print("Edges in the Minimum Spanning Tree:")
for u, v, weight in mst_edges:
    print(f"{u} -- {v} == {weight}")
