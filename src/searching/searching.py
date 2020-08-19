def linear_search(arr, target):
    # Your code here
    print(arr)
    for i,v in enumerate(arr):
        if v == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    if len(arr)== 0:
        return -1

    top = len(arr) -1
    bottom = 0
    middle = 0
    while bottom <= top:
        middle = (top+bottom)  // 2
        if arr[middle] > target:
            top = middle -1
        elif arr[middle] < target:
            bottom = middle +1
        else:
            return middle



 # not found

ar = [i for i in range(1,11)]
print(binary_search(ar,7))
print(ar)
