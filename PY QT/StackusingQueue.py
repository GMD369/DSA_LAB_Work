from queue import Queue

class StackUsingQueue:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, item):
        """Pushes an item onto the stack."""
        self.queue1.put(item)

    def pop(self):
        """Removes the top item from the stack and returns it."""
        if self.queue1.empty():
            return "Stack is empty"
        
        # Move all elements except the last one to queue2
        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())
        
        # The last element of queue1 is the top element of the stack
        top_item = self.queue1.get()

        # Swap queue1 and queue2 so queue1 has the updated elements
        self.queue1, self.queue2 = self.queue2, self.queue1

        return top_item

    def peek(self):
        """Returns the top item without removing it."""
        if self.queue1.empty():
            return "Stack is empty"

        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())
        
        # Get the last item, which is the top of the stack
        top_item = self.queue1.get()
        self.queue2.put(top_item)

        # Swap queue1 and queue2 again to preserve state
        self.queue1, self.queue2 = self.queue2, self.queue1

        return top_item

    def is_empty(self):
        """Checks if the stack is empty."""
        return self.queue1.empty()

    def size(self):
        """Returns the size of the stack."""
        return self.queue1.qsize()


# Example usage:
stack = StackUsingQueue()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop())  # Output: 30
print(stack.peek())  # Output: 20
print(stack.pop())  # Output: 20
print(stack.is_empty())  # Output: False
print(stack.size())  # Output: 1
print(stack.pop())  # Output: 10
print(stack.is_empty())  # Output: True
