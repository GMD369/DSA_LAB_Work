class Node:
    def __init__(self, data):
        self.data = data
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    # Node Insert At first:
    def insertAt_First(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        new_node.next=self.head
        self.head = new_node

    # Node Insert At last:
    def insertAT_last(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        currNode=self.head
        while currNode.next != None:
            currNode=currNode.next
        currNode.next=new_node

    # Node delete from first:
    def deleteAt_first(self):
        if self.head is None:
            return
        self.head=self.head.next


    # Node delete from last:
    def deleteAt_last(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head=None
        second_last=self.head
        last=self.head.next
        while last.next is not None:
            second_last=second_last.next
            last=last.next
        second_last.next=None

    # first search node and delete it:
    def searchAndDelete(self, data):
        current=self.head
        previous=None
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True
            previous=current
            current=current.next
        return False

    # Print Nodes in LinkedList format:
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")

    # Length of linked list:
    def length(self):
        total=0
        temp=self.head
        while temp:
            total+=1
            temp=temp.next
        return total


linklist=LinkedList()
linklist.insertAt_First(23)
linklist.insertAt_First(12)
linklist.insertAT_last(34)
linklist.insertAT_last(44)
linklist.printList()
print("Length of linkedList",linklist.length())


linklist.deleteAt_first()
linklist.printList()
print("Length of linkedList",linklist.length())

linklist.deleteAt_last()
linklist.printList()
print("Length of linkedList",linklist.length())


linklist.insertAT_last(36)
linklist.insertAT_last(46)
linklist.searchAndDelete(36)
linklist.printList()
print("Length of linkedList",linklist.length())