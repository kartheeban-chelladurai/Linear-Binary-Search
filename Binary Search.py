def binary_search(arr, target):
    """
    Perform binary search on a sorted array.
    
    Args:
        arr: Sorted list of elements
        target: Element to search for
    
    Returns:
        Index of target if found, otherwise -1
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def binary_search_recursive(arr, target, left=0, right=None):
    """
    Perform binary search recursively on a sorted array.
    
    Args:
        arr: Sorted list of elements
        target: Element to search for
        left: Left boundary index
        right: Right boundary index
    
    Returns:
        Index of target if found, otherwise -1
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


# Test cases
if __name__ == "__main__":
    sorted_array = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78]
    
    print("Binary Search - Iterative")
    print(f"Array: {sorted_array}")
    print(f"Search for 23: Index {binary_search(sorted_array, 23)}")
    print(f"Search for 5: Index {binary_search(sorted_array, 5)}")
    print(f"Search for 100: Index {binary_search(sorted_array, 100)}")
    
    print("\nBinary Search - Recursive")
    print(f"Search for 23: Index {binary_search_recursive(sorted_array, 23)}")
    print(f"Search for 5: Index {binary_search_recursive(sorted_array, 5)}")
    print(f"Search for 100: Index {binary_search_recursive(sorted_array, 100)}")
