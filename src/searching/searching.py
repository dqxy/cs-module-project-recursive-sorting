# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if end >= start:
        #Split the list if the end is greater
        mid = (start + end) // 2
        #Return if found
        if arr[mid] == target:
            return mid
        #Keep searching if in the top half
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid)
            #Keep searching if in the bottom half
        else:
            return binary_search(arr, target, mid , end)
        #Not Found
    else:
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass