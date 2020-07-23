# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    # starting at the beginning of `a` and `b`
    # compare the next value of each
    # add smallest to `merged_arr`
    #Declare index arrays
    arrA_index = 0
    arrB_index = 0
    #For each element
    for i in range(elements):
        #Increment index and merge if the arrays lengths are not yet reached
        if arrA_index < len(arrA) and arrB_index < len(arrB):
            if arrA[arrA_index] <= arrB[arrB_index]:
                merged_arr[i] = arrA[arrA_index]
                arrA_index += 1
            else:
                merged_arr[i] = arrB[arrB_index]
                arrB_index += 1
        elif arrA_index < len(arrA) and arrB_index is len(arrB):
            merged_arr[i] = arrA[arrA_index]
            arrA_index += 1
        else:
            merged_arr[i] = arrB[arrB_index]
            arrB_index += 1

    

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # recursively call merge_sort() on LHS
    # recursively call merge_sort() on RHS
    # merge sorted pieces
     #Repeatedly divide the original collection in half until we reach the base case
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        left = merge_sort(left)
        right = merge_sort(right)
        return merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here
