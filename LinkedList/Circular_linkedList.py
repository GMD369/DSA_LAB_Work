class Node:
    def __init__(self, data):
        self.data = data
        self.next=None

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


