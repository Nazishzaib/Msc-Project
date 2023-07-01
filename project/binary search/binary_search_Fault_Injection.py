# Description:binary search algorithm with a fault
# fault: fault is at line 11, array[mid] == target + 1
def binary_search(array, target):
    if len(array) == 0:
        return -1
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2 
        if array[mid] == target + 1: # fault
            return mid
        elif array[mid] < target: 
            left = mid + 1
        else:
            right = mid - 1
    return -1











