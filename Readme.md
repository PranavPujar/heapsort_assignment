# MinHeap Implementation in Python

This project implements a generic MinHeap data structure in Python. The MinHeap is a binary heap that maintains the heap property where each parent node is less than or equal to its children, based on a given key function.

## Features

- Generic implementation that can work with any data type
- Efficient operations using bit manipulation for parent/child relationships
- Supports custom key functions for determining element priority
- Includes basic heap operations: build, add, pop, and heapify

## Usage

### Basic Usage

```python
from min_heap import MinHeap

# Create a MinHeap for integers
int_heap = MinHeap()
int_heap.build([4, 10, 3, 5, 1])

# Pop the minimum element
min_value = int_heap.pop()  # Returns 1

# Add a new element
int_heap.add(2)
```

### Custom Objects

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create a MinHeap of Person objects, using age as the key
person_heap = MinHeap(key=lambda p: p.age)
person_heap.build([
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 35)
])

youngest = person_heap.pop()  # Returns Person("Bob", 25)
```

## Implementation Details

- The heap is implemented as a list, where for any element at index i:
  - Its parent is at index (i-1) >> 1
  - Its left child is at index (i<<1) + 1
  - Its right child is at index (i<<1) + 2

- The `heapify` method maintains the heap property by recursively comparing and swapping elements.
- The `build` method constructs a heap from an arbitrary list in O(n) time.
- The `add` method inserts a new element and sifts it up to its correct position.
- The `pop` method removes and returns the minimum element, then restructures the heap.

## Time Complexity

- Build: O(n)
- Add: O(log n)
- Pop: O(log n)
- Heapify: O(log n)

Where n is the number of elements in the heap.

## Notes

This implementation uses Python's type hinting for better code documentation and IDE support. The heap is generic and can work with any comparable data type or custom objects with a provided key function.