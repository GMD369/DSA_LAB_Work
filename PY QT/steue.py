class Steue:
    def __init__(self):
        # Initialize three stacks
        self.stack1 = []
        self.stack2 = []
        self.stack3 = []

    def push(self, item):
        # Add an item to stack1 (initial input)
        self.stack1.append(item)

    def split_stack(self):
        # Move half of stack1's elements to stack2 and half to stack3
        half_size = len(self.stack1) // 2
        while len(self.stack1) > half_size:
            self.stack2.append(self.stack1.pop())
        while self.stack1:
            self.stack3.append(self.stack1.pop())
            
    def queue_enqueue(self, item):
        # Queue-like enqueue operation on stack3
        self.stack3.append(item)  # Insert at the start to maintain queue order

    def queue_dequeue(self):
        # Queue-like dequeue operation on stack3
        if self.stack3:
            return self.stack3.pop(0)  # Remove from the end to maintain queue order
        else:
            return None

    def restore_stack1(self):
        # Move all elements from stack2 back to stack1
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def stack_pop(self):
        # Stack-like pop operation on stack1
        if self.stack1:
            return self.stack1.pop()
        else:
            return None

    def display(self):
        # Display contents of all stacks for tracking
        print("Stack 1:", self.stack1)
        print("Stack 2:", self.stack2)
        print("Stack 3:", self.stack3)


# Example Usage
steue = Steue()

# Add items to stack1
for i in range(1, 11):
    steue.push(i)

print("Initial state:")
steue.display()

# Split stack1 into stack2 and stack3
steue.split_stack()
print("\nAfter splitting:")
steue.display()

# Perform queue operations on stack3
steue.queue_enqueue(99)
print("\nAfter enqueueing 99 in stack3:")
steue.display()

print("\nDequeueing from stack3:")
steue.queue_dequeue()
steue.display()

# Restore stack1 with stack2's elements
steue.restore_stack1()
print("\nAfter restoring stack1 from stack2:")
steue.display()

# Stack operation on stack1
print("\nPop from stack1:")
steue.stack_pop()
steue.display()
