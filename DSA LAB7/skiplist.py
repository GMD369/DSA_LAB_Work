import random

class Node:
    def __init__(self, key, level):
        self.key = key
        self.forward = [None] * (level + 1)  # Array of forward pointers for each level

class SkipList:
    def __init__(self, max_level, p):
        self.max_level = max_level  # Maximum levels for the skip list
        self.p = p  # Probability for level generation
        self.header = Node(-1, max_level)  # Header node
        self.level = 0  # Current level of the skip list

    def random_level(self):
        """Generate a random level for a new node."""
        lvl = 0
        while random.random() < self.p and lvl < self.max_level:
            lvl += 1
        return lvl

    def insert(self, key):
        """Insert a new key into the skip list."""
        update = [None] * (self.max_level + 1)
        current = self.header

        # Traverse the skip list to find the insertion point
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        # Get the next node at level 0
        current = current.forward[0]

        # If the key is not already in the list
        if not current or current.key != key:
            # Generate a random level for the new node
            new_level = self.random_level()

            # If the new level is greater than the current level, update the header
            if new_level > self.level:
                for i in range(self.level + 1, new_level + 1):
                    update[i] = self.header
                self.level = new_level

            # Create the new node
            new_node = Node(key, new_level)

            # Update the forward pointers
            for i in range(new_level + 1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

    def search(self, key):
        """Search for a key in the skip list."""
        current = self.header
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
        current = current.forward[0]

        # Check if the current node is the desired key
        if current and current.key == key:
            return True
        return False

    def delete(self, key):
        """Delete a key from the skip list."""
        update = [None] * (self.max_level + 1)
        current = self.header

        # Traverse the skip list to find the node to be deleted
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        # Get the node to be deleted
        current = current.forward[0]

        if current and current.key == key:
            # Update forward pointers to remove the node
            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]

            # Reduce the level of the skip list if necessary
            while self.level > 0 and not self.header.forward[self.level]:
                self.level -= 1

    def display(self):
        """Display the skip list."""
        print("Skip List:")
        for i in range(self.level + 1):
            print(f"Level {i}: ", end="")
            current = self.header.forward[i]
            while current:
                print(current.key, end=" ")
                current = current.forward[i]
            print()

# Example Usage
if __name__ == "__main__":
    skiplist = SkipList(max_level=4, p=0.5)
    skiplist.insert(3)
    skiplist.insert(6)
    skiplist.insert(7)
    skiplist.insert(9)
    skiplist.insert(12)
    skiplist.insert(19)
    skiplist.insert(17)
    skiplist.insert(26)

    skiplist.display()

    print("\nSearch for 19:", skiplist.search(19))  # True
    print("Search for 25:", skiplist.search(25))  # False

    skiplist.delete(19)
    print("\nAfter deleting 19:")
    skiplist.display()
