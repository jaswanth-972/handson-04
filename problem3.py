from typing import List

def remove_dups(arr: List[int]) -> List[int]:
    """
    Remove duplicates from a sorted list and return a new list with unique elements.

    Args:
        arr (List[int]): A sorted list of integers which may contain duplicates.

    Returns:
        List[int]: A new list containing only unique elements from the input list.
    """
    if not arr:
        return []

    # Initialize the list with the first element
    unique_elements = [arr[0]]

    # Traverse the array and add only unique elements
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            unique_elements.append(arr[i])

    return unique_elements

# Example usage:
array1 = [2, 2, 2, 2, 2]
array2 = [1, 2, 2, 3, 4, 4, 4, 5, 5]

print("Unique elements in array1:", remove_dups(array1))
# Output: [2]

print("Unique elements in array2:", remove_dups(array2))
# Output: [1, 2, 3, 4, 5]
