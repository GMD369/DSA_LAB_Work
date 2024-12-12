class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.edges = []    # List of edges (u, v, weight)

    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1
        print(parent)
        print(rank)

    def kruskal(self):
        self.edges.sort(key=lambda edge: edge[2])  # Sort edges by weight
        parent = []
        rank = []
        mst = []  # Resulting Minimum Spanning Tree

        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        print(parent)
        print(rank)
        for u, v, weight in self.edges:
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)

            if root_u != root_v:  # No cycle
                mst.append((u, v, weight))
                self.union(parent, rank, root_u, root_v)

        return mst

# Example Usage
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

mst = g.kruskal()
print("Edges in the Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} -- {v} == {weight}")
