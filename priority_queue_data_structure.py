# Import the built-in queue module which provides the PriorityQueue class.
import queue

# Create a PriorityQueue instance.
# A PriorityQueue in Python is implemented using a min-heap.
# In a min-heap, every parent node is less than or equal to its child nodes,
# ensuring that the smallest element (according to natural order) is always at the root.
pq = queue.PriorityQueue()

# Adding elements to the queue.
# Although the elements are added in this order ("B", "C", "A", "F", "D"),
# the PriorityQueue automatically rearranges them based on their natural order.
# Since strings are compared alphabetically, "A" is the smallest, followed by "B", "C", "D", then "F".
pq.put("B")
pq.put("C")
pq.put("A")
pq.put("F")
pq.put("D")

# Removing and printing elements in priority order.
# The loop 'while not pq.empty()' runs as long as there are items in the queue.
# In each iteration, the 'get()' method removes and returns the smallest element from the queue,
# according to the min-heap property. This ensures that the elements are printed in alphabetical order.
while not pq.empty():
    print(pq.get())
