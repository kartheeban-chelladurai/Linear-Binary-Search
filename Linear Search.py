def linear_search(arr, target):
    """
    Linear search algorithm to find target in array.
    Returns index if found, otherwise -1.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Test the function
if __name__ == "__main__":
    # Example array
    arr = [5, 2, 8, 1, 9, 3, 7]
    target = 8
    
    result = linear_search(arr, target)
    
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in array")

