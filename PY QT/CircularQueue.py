front=-1
rear=-1
size=6
Circular_queue=[None,None,None,None,None,None]

# Cicular Enqueue Function:
def enqueueData(num):
    global front, rear, size, Circular_queue
    if ((rear+1)%size==front):
        print("Circular Queue is full\n")
    elif front==-1 :
        front=0
        rear=rear+1
        Circular_queue[rear]=num
    else:
        rear=(rear+1)%size
        Circular_queue[rear]=num

# Circular Dequeue Fucntion:
def dequeueData():
    global front, rear, size, Circular_queue
    if front==-1:
        print("Circular Queue is empty\n")
    elif front==rear:
        front=-1
        rear=-1
    else:
        temp=Circular_queue[front]
        Circular_queue[front]=None
        front=(front+1)%size
        return temp

enqueueData(3)
enqueueData(5)
enqueueData(7)
enqueueData(9)
enqueueData(11)
enqueueData(13)
print(dequeueData())
enqueueData(55)



print(Circular_queue)

    
