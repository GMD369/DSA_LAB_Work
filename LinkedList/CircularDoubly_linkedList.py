class Node:
    def __init__(self, data):
        self.data = data
        self.next=None
        self.prev=None

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

