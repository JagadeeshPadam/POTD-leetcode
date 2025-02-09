from collections import defaultdict
from sortedcontainers import SortedSet

class NumberContainers:

    def __init__(self):
        self.index_to_number = {}  
        self.number_to_indices = defaultdict(SortedSet)
          
    def change(self, index: int, number: int) -> None:
        if index in self.index_to_number:
            self.number_to_indices[self.index_to_number[index]].discard(index)
        self.index_to_number[index] = number
        self.number_to_indices[number].add(index)

    def find(self, number: int) -> int:
        return next(iter(self.number_to_indices[number]), -1)

# Example Usage:
# obj = NumberContainers()
# obj.change(1, 10)
# obj.change(2, 10)
# print(obj.find(10))  # Output: 1