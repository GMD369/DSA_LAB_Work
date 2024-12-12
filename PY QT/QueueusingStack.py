class QueueUsingStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        """Enqueues an item to the queue."""
        self.stack1.append(item)

    def dequeue(self):
        """Dequeues the front item from the queue and returns it."""
        if not self.stack2:  # If stack2 is empty, move elements from stack1
            if not self.stack1:  # If both stacks are empty, the queue is empty
                return "Queue is empty"
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def front(self):
        """Returns the front item without removing it."""
        if not self.stack2:  # If stack2 is empty, move elements from stack1
            if not self.stack1:  # If both stacks are empty, the queue is empty
                return "Queue is empty"
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def is_empty(self):
        """Checks if the queue is empty."""
        return not self.stack1 and not self.stack2

    def size(self):
        """Returns the size of the queue."""
        return len(self.stack1) + len(self.stack2)


# Example usage:
queue = QueueUsingStack()


queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.dequeue())  # Output: 10
print(queue.front())    # Output: 20
print(queue.dequeue())  # Output: 20
print(queue.is_empty()) # Output: False
print(queue.size())     # Output: 1
print(queue.dequeue())  # Output: 30
print(queue.is_empty()) # Output: True
print(queue.dequeue())  # Output: "Queue is empty"
queue.enqueue(40)
print(queue.size()) 

print(queue.size())
print(queue.dequeue())  
print(queue.front()) 