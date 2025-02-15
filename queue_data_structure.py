# Import deque from the collections module to create a queue
from collections import deque


def main():
    # ---------------------------------------------------------
    # Queue Data Structure Implementation using deque
    #
    # A Queue follows the FIFO (First-In, First-Out) principle:
    #  - Enqueue: Add an item to the end of the queue (using append())
    #  - Dequeue: Remove and return the item from the front of the queue (using popleft())
    #  - Peek: Look at the front item without removing it (using indexing: queue[0])
    #  - Empty Check: Verify if the queue is empty (using len(queue) == 0)
    #
    # Real-life examples of queues:
    #  - Keyboard Buffer: Characters appear in the order pressed
    #  - Printer Queue: Print jobs are processed in order
    #  - Breadth-first search: Traversal of nodes level by level in graphs or trees
    # ---------------------------------------------------------

    # Create an empty queue using deque
    queue = deque()

    # Check if the queue is empty. Initially, it should be empty, so len(queue) == 0 returns True.
    print("Is queue empty?", len(queue) == 0)

    # Enqueue items onto the queue (similar to queue.offer() in Java)
    # Items are added in the following order and will be processed in that same order.
    queue.append("Karen")
    queue.append("Chad")
    queue.append("Steve")
    queue.append("Harold")

    # Print the entire queue. Converting the deque to a list makes it easier to view.
    print("Current queue:", list(queue))

    # Peek at the front of the queue without removing it.
    # This checks if the queue is not empty and then accesses the first element.
    if queue:
        print("Front of queue (peek):", queue[0])
    else:
        print("Queue is empty.")

    # Dequeue items from the queue (similar to queue.poll() in Java)
    # popleft() removes and returns the element from the front of the queue.
    dequeued_item = queue.popleft()  # Removes "Karen"
    print("Dequeued item:", dequeued_item)

    # Additional operation:
    # Check if a specific element (e.g., "Harold") is in the queue, similar to queue.contains() in Java.
    print("Is 'Harold' in queue?", "Harold" in queue)

    # Print the updated state of the queue after one dequeue operation.
    print("Updated queue:", list(queue))


# Entry point check:
#
# The following conditional ensures that the main() function is executed only when the script is run directly.
# Explanation:
# - __name__ is a special variable in Python that gets defined for every module.
# - When the module is run directly, __name__ is set to '__main__'.
# - When the module is imported into another script, __name__ is set to the module's name.
#
# Thus, if this script is run directly (for example: python script.py), the condition will be True,
# and main() will be executed. If it is imported as a module, main() will not run automatically.
if __name__ == '__main__':
    main()
