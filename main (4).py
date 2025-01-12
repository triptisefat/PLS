# Static Array: Size and storage are determined at compile time.
# Python lists don't have true static arrays, but we can simulate a fixed-size array.
static_array = [0] * 5  # Fixed size of 5

print("Static Array:", static_array)

# Fixed Stack-Dynamic Array: Size is determined at runtime, but it doesn't change.
def fixed_stack_dynamic_array(size):
    array = [0] * size
    return array

size = 3
fixed_array = fixed_stack_dynamic_array(size)
print("Fixed Stack-Dynamic Array:", fixed_array)

# Stack-Dynamic Array: Both size and storage can change during execution.
stack_dynamic_array = []  # Start with an empty list
stack_dynamic_array.append(1)
stack_dynamic_array.append(2)
print("Stack-Dynamic Array:", stack_dynamic_array)

# Fixed Heap-Dynamic Array: Size is determined at runtime and allocated on the heap.
# In Python, all lists are allocated on the heap, but we simulate fixed size.
fixed_heap_dynamic_array = [0] * size  # Size determined at runtime
print("Fixed Heap-Dynamic Array:", fixed_heap_dynamic_array)

# Heap-Dynamic Array: Both size and storage can change dynamically.
heap_dynamic_array = []  # Start with an empty list
heap_dynamic_array.append(10)
heap_dynamic_array.append(20)
heap_dynamic_array.append(30)
print("Heap-Dynamic Array:", heap_dynamic_array)

# Demonstrating changing the size dynamically
heap_dynamic_array.pop()  # Removing an element
heap_dynamic_array.extend([40, 50])  # Adding more elements
print("Updated Heap-Dynamic Array:", heap_dynamic_array)
