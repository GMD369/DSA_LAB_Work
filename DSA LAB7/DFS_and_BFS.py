class Node:
    def __init__(self,name):
        self.name=name
        self.neighbours=[]
        self.visited=False
        self.entryTime=0
        self.finishTime=0

# Depth First search:
def dfs(node,currentTime):
    node.entryTime=currentTime
    node.visited=True
    currentTime+=1
    print(node.name,end=" ")
    for neigh in node.neighbours:
        if neigh.visited==False:
            currentTime=dfs(neigh,currentTime)
    node.finishTime=currentTime
    currentTime+=1
    return currentTime

# Breadth First Search:
def bfs(node):
    queue=[]
    node.visited=True
    queue.append(node)
    while queue:
        temp=queue.pop(0)
        print(temp.name,end=" ")
        for neigh in temp.neighbours:
            if neigh.visited==False:
                neigh.visited=True
                queue.append(neigh)
                

node1=Node("1")
node2=Node("2")
node3=Node("3")
node4=Node("4")
node5=Node("5")
node6=Node("6")
node7=Node("7")
node8=Node("8")

# Graph connections:
node1.neighbours=[node2,node3]
node2.neighbours=[node4,node5]
node3.neighbours=[node6,node7]
node7.neighbours=[node8]

currentTime=1
print("DFS: ")
dfs(node1,currentTime)
# print("BFS: ")
# bfs(node1)

# nodes=[node1,node2,node3,node4,node5,node6,node8]

# for node in nodes:
#     print(f"Name: {node.name}, Entry Time: {node.entryTime}, finishTime: {node.finishTime}")



