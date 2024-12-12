# Implement Queue using Array:

front=-1
rear=-1
size=6
queue=[0,0,0,0,0,0]

# ENQUEUE function:
def enqueue(data):
    global front, rear, queue
    if isFull():
        print("Queue is full")
    elif front==-1:
        front=0
        rear+=1
        queue[rear]=data
    else:
        rear+=1
        queue[rear]=data

# DEQUEUE Function:
def dequeue():
    global rear,queue
    if isEmpty():
        print("Queue is empty")
    else:
        rear=rear-1
        value=queue[0]
        for i in range(1,len(queue)):
            queue[i-1]=queue[i]
        queue[rear+1]=None
        return value

# isFull function:
def isFull():
    global front, rear, size
    return rear==size-1 or front>rear

# IsEmpty function:
def isEmpty():
    global front, rear
    return front==-1

# Peek Fucntion:
def peek():
    if isEmpty():
        print("queue is empty")
    else:
        return queue[front]


enqueue(10)
enqueue(20)
enqueue(30)
enqueue(40)
enqueue(50)
enqueue(56)
dequeue()
print(peek())
print(queue)