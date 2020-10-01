def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    start = 0
    end = (len(arr)-1)

    found = False
    while end >= start and not found:
        middle_int = (start + end) // 2
        if arr[middle_int] == target:
            found = True
            return middle_int
        else:
            if target < arr[middle_int]:
                end = middle_int - 1
            if target > arr[middle_int]:
                start = middle_int + 1
    return -1  # not found
