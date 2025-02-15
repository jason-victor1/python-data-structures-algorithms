# A Node is like a treasure box. Each box holds a treasure (data)
# and a secret note (pointer) telling you where the next box is.
class Node:
    def __init__(self, data, next=None):
        # Store the treasure in this box
        self.data = data
        # This is the secret note pointing to the next treasure box.
        # If there's no next box, it's None.
        self.next = next

    def __repr__(self):
        # When you look at this box, show the treasure inside it.
        return repr(self.data)


# The LinkedList is the treasure hunt map.
# It keeps track of where the first box is (head) and, if needed,
# where the last box is (tail) for fast appending.
class LinkedList:
    def __init__(self):
        # Initially, there are no treasure boxes in our hunt.
        self.head = None
        # No last box either. Keeping track of tail helps to quickly add a new box at the end.
        self.tail = None

    def is_empty(self):
        # Check if there are any treasure boxes.
        # If there's no head box, the hunt is empty.
        return self.head is None

    def push(self, data):
        """Insert a new treasure box at the beginning (like adding a new starting box in a stack)."""
        # Create a new treasure box with the given treasure.
        # Its secret note (pointer) is set to the current first box.
        new_node = Node(data, self.head)
        # Now, the new box becomes the very first box on the treasure map.
        self.head = new_node
        # If there were no boxes before, this new box is both the first and the last.
        if self.tail is None:
            self.tail = new_node

    def pop(self):
        """Remove the treasure box at the beginning (like taking the top box from a stack or the front box from a queue)."""
        # If there are no boxes, you cannot take one away.
        if self.is_empty():
            raise IndexError("pop from empty LinkedList")
        # Remember the treasure inside the first box.
        data = self.head.data
        # Remove the first box by making the next box become the new first box.
        self.head = self.head.next
        # If there are no more boxes, update tail as well.
        if self.head is None:
            self.tail = None
        # Return the treasure that was in the removed box.
        return data

    def offer(self, data):
        """Add a new treasure box at the end (like placing a new box at the end of your treasure hunt, useful for a queue)."""
        # Create a new treasure box with the given treasure.
        new_node = Node(data)
        # If there are no boxes yet, this new box becomes both the first and the last.
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            # Otherwise, update the secret note of the current last box to point to this new box.
            self.tail.next = new_node
            # Now, the new box becomes the last one on the map.
            self.tail = new_node

    def poll(self):
        """Remove the first treasure box (another name for taking from the front, same as pop())."""
        return self.pop()

    def __iter__(self):
        # This allows us to go on a tour through our treasure boxes.
        current = self.head  # Start with the first box.
        while current:
            # Show the treasure inside the current box.
            yield current.data
            # Follow the secret note to the next box.
            current = current.next

    def __repr__(self):
        # Create a pretty treasure map showing all boxes in order,
        # with an arrow ("->") connecting the treasures.
        return " -> ".join(str(item) for item in self)


# ----------------------- Demonstration -----------------------
if __name__ == "__main__":
    # ---------------- Using as a Queue (First-In, First-Out) ----------------
    # Imagine you line up treasure boxes in the order they are found.
    queue = LinkedList()
    # Add treasure boxes at the end of the treasure hunt.
    queue.offer("A")
    queue.offer("B")
    queue.offer("C")
    queue.offer("D")
    queue.offer("F")
    # When you print the queue, it shows the boxes in the order they were added.
    print("Queue:", queue)  # Expected Output: A -> B -> C -> D -> F

    # ---------------- Using as a Stack (Last-In, First-Out) ----------------
    # Now imagine you stack treasure boxes on top of each other.
    stack = LinkedList()
    # Add treasure boxes at the beginning of the stack.
    stack.push("A")
    stack.push("B")
    stack.push("C")
    stack.push("D")
    stack.push("F")
    # When you print the stack, the most recent box is on top.
    print("Stack before pop:", stack)  # Expected Output: F -> D -> C -> B -> A
    # Remove the top treasure box (the one at the beginning).
    print("Popped:", stack.pop())       # This removes "F"
    # The stack now shows the remaining boxes.
    print("Stack after pop:", stack)     # Expected Output: D -> C -> B -> A
