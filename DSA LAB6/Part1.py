# Singular LinkedList:
class Node:
    def __init__(self, data):
        self.data = data
        self.next=None
        self.prev=None
    
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

linklist=LinkedList()
linklist.insertAt_First(23)
linklist.insertAt_First(12)
linklist.insertAT_last(34)
linklist.insertAT_last(44)
linklist.printList()


linklist.deleteAt_first()
linklist.printList()

linklist.deleteAt_last()
linklist.printList()


linklist.insertAT_last(36)
linklist.insertAT_last(46)
linklist.searchAndDelete(36)
linklist.printList()


# Circular LinkedList:
class Circular_linkedList:
    def __init__(self):
        self.head = None
    
    # Insert at first:
    def insert_at_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next=self.head
        else:
            new_node.next=self.head 
            current=self.head
            while(current.next!=self.head):
                current=current.next
            current.next=new_node
            self.head=new_node

    # insert at last:
    def insert_at_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next=self.head
        else:
            current=self.head
            while(current.next!=self.head):
                current=current.next
            current.next=new_node
            new_node.next=self.head

    # delete at first:
    def delete_at_first(self):
        val=self.head
        if self.head is None:
            return
        if self.head.next==self.head:
            self.head=None
        self.head=self.head.next
        current=self.head
        while(current.next!=val):
            current=current.next
        current.next=self.head

    # delete node from last:
    def delete_at_last(self):
        if self.head is None:
            return
        if self.head.next==self.head:
            self.head=None
            return
        current=self.head
        while(current.next.next!=self.head):
            current=current.next
        current.next=self.head


    # Print all nodes:
    def print_list(self):
        current = self.head
        while True:
            print(current.data, end="<->")
            current = current.next
            if current == self.head:
                break
        print(f"{self.head.data}(head)") 

    # length of list:
    def length(self):

        if self.head is None:
            return 0
        
        current = self.head
        count = 0
        while True:
            count += 1
            current = current.next
            if current == self.head:
                break
        return count
    
    # node search and delete:
    def search_and_delete(self, val):
        if self.head is None:
            return
        current=self.head
        prev=None
        if current.data==val:
            if current.next==self.head:
                self.head=None
            else:
                while current.next !=self.head:
                    current=current.next
                current.next=self.head.next
                self.head=self.head.next
                return
        
        while current.next!=self.head:
            prev=current
            current=current.next
            if current.data==val:
                prev.next=current.next
                return
            
     # Insert After:
    def insert_after(self, val, new_val):
            if self.head is None:
                return
            new_node=Node(new_val)
            current=self.head
            while True:
                if current.data==val:
                    new_node.next=current.next
                    current.next=new_node
                    break
                current=current.next
                if current==self.head:
                    break


cll=Circular_linkedList()

cll.insert_at_first(1)
cll.insert_at_first(34)
cll.insert_at_first(99)
cll.insert_at_last(56)
cll.insert_at_last(78)
cll.insert_after(78,45)
cll.print_list()
print("Length of circular linkedList",cll.length())

cll.search_and_delete(99)
cll.print_list()
print("Length of circular linkedList",cll.length())


cll.delete_at_first()
cll.print_list()
print("Length of circular linkedList",cll.length())

cll.delete_at_last()
cll.print_list()
print("Length of circular linkedList",cll.length())

# Doubly LinkedList:
class Doubly_LinkedList:
    def __init__(self):
        self.head=None
    
    # Insert node at First:
    def insert_at_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # Show all nodes:
    def print_Doubly_linked_list(self):
        current = self.head
        while current:
            print(current.data, end="<->")
            current = current.next
        print("None")

    # length of Doubly LinkedList:
    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    
    # Node insert at Last:
    def insert_Atlast(self,data):
        new_Node=Node(data)
        if self.head is None:
            self.head=new_Node
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=new_Node
        new_Node.prev=last

    # Node delete at last:
    def delete_at_last(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head=None
            return
        else:   
            second_last=self.head
            last=self.head.next
            while last.next:
                second_last=last
                last=last.next
            second_last.next=None
            
    # Node delete at first:
    def delete_at_First(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head=None
            return
        else:
            self.head=self.head.next
            self.head.prev=None

    # first search node and then delete it:
    def search_delete(self, data):
        current = self.head
        previous=None
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                    current.prev=previous
                else:
                    self.head = current.next
                    current.prev=None
                return True
            previous = current
            current = current.next
        return False
    
    # show all nodes in reverse:
    def show_reverse(self):
        current=self.head
        while current and current.next:
            current=current.next
        
        while current:
            print(current.data,end="<->")
            current=current.prev
        print("None")

    # Node Insert after:
    def insert_after(self, prev_data, new_data):
        current = self.head
        while current and current.data!=prev_data:
            current = current.next
        if current is None:
            print(f"previous Node {prev_data} is not found")
            return
        new_node = Node(new_data)
        new_node.next = current.next
        current.next=new_node
        new_node.prev = current

        if new_node.next:
            new_node.next.prev = new_node

        




Dbl=Doubly_LinkedList()

Dbl.insert_at_first(10)
Dbl.insert_at_first(20)
Dbl.insert_at_first(30)
Dbl.insert_Atlast(40)
Dbl.insert_Atlast(89)
Dbl.insert_after(30,67)
Dbl.print_Doubly_linked_list()
print("Length of Doubly:",Dbl.length())
Dbl.show_reverse()

Dbl.delete_at_last()
Dbl.print_Doubly_linked_list()
print("Length of Doubly:",Dbl.length())

Dbl.delete_at_First()
Dbl.print_Doubly_linked_list()
print("Length of Doubly:",Dbl.length())

Dbl.search_delete(10)
Dbl.print_Doubly_linked_list()
print("Length of Doubly:",Dbl.length())


# Doubly Circular LinkedList:
class DoublyCircular_LinkedList:
    def __init__(self):
        self.head = None

    # append node:
    def append(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.head.next=self.head
            self.head.prev=self.head
        else:
            current=self.head
            while current.next!=self.head:
                current=current.next
            current.next=new_node
            new_node.prev=current
            new_node.next=self.head
            self.head.prev=new_node

    # Show all nodes:
    def display(self):
        current=self.head
        while True:
            print(current.data, end="<-> ")
            current=current.next
            if current==self.head:
                break
        print(self.head.data,"(Head)")

    # Insert After:
    def insert_after(self, prev_node_data, new_data):
        new_node = Node(new_data)
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while True:
            if current.data == prev_node_data:
                new_node.prev = current
                new_node.next = current.next
                current.next=new_node
                new_node.next.prev = new_node
                break
            current=current.next
            if current==self.head:
                print(f"prev Node {prev_node_data} not Found!")
                break

    # Search and Delete:
    def search_delete(self, data):
        current = self.head
        if self.head is None:
            print("List is empty")
            return
        while True:
            if current.data == data:
                if current.next==self.head and current.prev ==self.head:
                    self.head=None
                else:
                    if current==self.head:
                       self.head=self.head.next
                
                    current.prev.next=current.next
                    current.next.prev=current.prev
                return
            current = current.next
            if current == self.head:
                print(f"Node {data} not Found!")
                break
    # length of list:
    def length(self):
        count=0
        if self.head is None:
            return count
        count=1
        current=self.head
        while current.next!=self.head:
            count+=1
            current=current.next
        return count

        


dcl=DoublyCircular_LinkedList()

dcl.append(1)
dcl.append(2)
dcl.append(4)
dcl.append(77)
dcl.display()
print(f"length of list is: {dcl.length()}" )

dcl.insert_after(77,56)
dcl.display()
print(f"length of list is: {dcl.length()}" )

dcl.search_delete(2)
dcl.display()
print(f"length of list is: {dcl.length()}" )


