class Node:
    def __init__(self, data):
        self.data = data
        self.next=None
        self.prev=None

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
