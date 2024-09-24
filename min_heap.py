from typing import TypeVar, List, Callable

T = TypeVar('T')

class MinHeap:
    def __init__(self, key: Callable[[T], float] = lambda x: x):
        self.heap, self.key = [], key

    def parent(self, i: int) -> int:
        return (i - 1) >> 1

    def left(self, i: int) -> int:
        return (i << 1) + 1

    def right(self, i: int) -> int:
        return (i << 1) + 2

    def heapify(self, i: int) -> None:
        smallest, n = i, len(self.heap)
        for child in (self.left(i), self.right(i)):
            if child < n and self.key(self.heap[child]) < self.key(self.heap[smallest]):
                smallest = child
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def build(self, arr: List[T]) -> None:
        self.heap = arr
        for i in range(len(arr) // 2 - 1, -1, -1):
            self.heapify(i)

    def pop(self) -> T:
        if not self.heap:
            raise IndexError("Empty heap")
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify(0)
        return root

    def add(self, item: T) -> None:
        self.heap.append(item)
        self._sift_up(len(self.heap) - 1)

    def _sift_up(self, i: int) -> None:
        while i > 0 and self.key(self.heap[self.parent(i)]) > self.key(self.heap[i]):
            p = self.parent(i)
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            i = p

def main():
    # Test with int and float
    for type_name, data in [("Integer", [4, 10, 3, 5, 1]), 
                            ("Float", [4.5, 10.2, 3.8, 5.1, 1.7])]:
        heap = MinHeap()
        print(f"\n{type_name} Heap:")
        heap.build(data)
        print(f"Initial: {heap.heap}")
        print(f"Pop: {heap.pop()}, After pop: {heap.heap}")
        new_val = 2 if type_name == "Integer" else 2.3
        heap.add(new_val)
        print(f"After adding {new_val}: {heap.heap}")

    # Test with custom object
    class Person:
        def __init__(self, name: str, age: int):
            self.name, self.age = name, age
        def __repr__(self):
            return f"Person({self.name},{self.age})"

    people = [Person(n, a) for n, a in [
        ("Alice", 30), ("Bob", 25), ("Charlie", 35), 
        ("David", 20), ("Eve", 28)
    ]]
    
    person_heap = MinHeap(key=lambda p: p.age)
    print("\nCustom Object Heap:")
    person_heap.build(people)
    print(f"Initial: {person_heap.heap}")
    print(f"Pop: {person_heap.pop()}, After pop: {person_heap.heap}")
    person_heap.add(Person("Frank", 22))
    print(f"After adding Frank(22): {person_heap.heap}")

if __name__ == "__main__":
    main()