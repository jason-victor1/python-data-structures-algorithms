# Create an empty stack using a list.
# In Python, lists are versatile and can act as stacks using append() and pop() methods.
stack = []

# Check if the stack is empty.
# len(stack) returns the number of elements in the list.
# If it's zero, then the stack is empty (True).
print("Is stack empty?", len(stack) == 0)  # Expected output: True initially

# Push items onto the stack (similar to stack.push() in Java).
# The append() method adds an element to the end of the list.
# In our stack, the end of the list is considered the top.
# Add "Minecraft" to the bottom of the stack (first pushed)
stack.append("Minecraft")
stack.append("Skyrim")      # Add "Skyrim" above "Minecraft"
stack.append("DOOM")        # Add "DOOM" above "Skyrim"
stack.append("Borderlands")  # Add "Borderlands" above "DOOM"
stack.append("FFVII")       # Add "FFVII" as the topmost element

# Print the entire stack.
# This displays the list in the order the items were added.
print("Current stack:", stack)

# Pop the top item off the stack.
# The pop() method removes and returns the last element of the list (the top of the stack).
my_fav_game = stack.pop()  # Removes "FFVII" from the top of the stack.
print("Popped game:", my_fav_game)

# Peek at the top of the stack without removing it.
# We check if the stack is not empty; if it's not, stack[-1] returns the last element.
if stack:
    print("Top of stack:", stack[-1])
else:
    print("Stack is empty.")

# Define a function to search for an item within the stack.
# This function simulates Java's stack.search() behavior.
# It returns the 1-indexed position from the top of the stack (i.e., the top item is position 1).
# If the target is not found, it returns -1.


def search_stack(stack, target):
    try:
        # Reverse the stack using slicing (stack[::-1]).
        # Reversing makes the top of the stack the first element (index 0) in the new list.
        # Then, .index(target) searches for the target in this reversed list and returns its 0-indexed position.
        # +1 converts the 0-indexed result to 1-indexed.
        position = stack[::-1].index(target) + 1
        return position  # Return the 1-indexed position of the target.
    except ValueError:
        # If the target is not found, .index() raises a ValueError.
        # In this case, we return -1 to indicate the target is not present in the stack.
        return -1


# Example search:
# Attempt to search for "Fallout76" in the current stack.
search_result = search_stack(stack, "Fallout76")
print("Search result for 'Fallout76':", search_result)
# Expected output:
# "Search result for 'Fallout76': -1" since "Fallout76" is not in the stack.
