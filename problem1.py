import heapq
from typing import List

def merge_sorted(arrays: List[List[int]]) -> List[int]:
    min_heap = []
    result = []

    # Initialize the heap with the first element from each non-empty array
    for i, array in enumerate(arrays):
        if array:  # Ensure the array is not empty
            heapq.heappush(min_heap, (array[0], i, 0))  # (value, array index, element index)

    # Extract the smallest element from the heap and add the next element from the same array
    while min_heap:
        value, array_index, element_index = heapq.heappop(min_heap)
        result.append(value)

        # If there's a next element in the same array, push it into the heap
        if element_index + 1 < len(arrays[array_index]):
            next_value = arrays[array_index][element_index + 1]
            heapq.heappush(min_heap, (next_value, array_index, element_index + 1))

    return result

# Example usage:
arrays1 = [
    [1, 3, 5, 7],
    [2, 4, 6, 8],
    [0, 9, 10, 11]
]
arrays2 = [
    [1, 3, 7],
    [2, 4, 8],
    [9, 10, 11]
]
arrays3 = []  # Test with an empty list
arrays4 = [[], [], []]  # Test with a list of empty arrays

print("Merged array 1:", merge_sorted(arrays1))
# Expected Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print("Merged array 2:", merge_sorted(arrays2))
# Expected Output: [1, 2, 3, 4, 7, 8, 9, 10, 11]

print("Merged array 3:", merge_sorted(arrays3))
# Expected Output: []

print("Merged array 4:", merge_sorted(arrays4))
# Expected Output: []
