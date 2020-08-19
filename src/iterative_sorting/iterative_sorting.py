# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for n in range(cur_index, len(arr)):
            if arr[n] < arr[smallest_index]:
                smallest_index = n
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    t = True
    while t:
        t = False
        for i in range(len(arr) -1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                t = True

    print(t)





    return arr

def bubble_sort_ranged(arr,num):
    # Your code here
    t = True
    while t:
        t = False
        for i in range(num):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                t = True

    print(t)





    return arr

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# print(bubble_sort_ranged(arr1,5))
from collections import Counter
'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the
buckets.

What is the time and space complexity of the counting sort algorithm?
'''

def linear_search(arr, target):
    # Your code here
    # print(arr)
    for v in arr:
        if v == target:
            return True

    return False

def counting_sort(arr, maximum=None):
    # Your code here
    from collections import Counter
    mydict = Counter(arr)
    ar = []
    for i in range(0,maximum+1):
        if i in arr:
            ar.append(mydict.get(i)*[i])

    ar = [ num for lis in ar for num in lis]

    return ar

arr2 = [1, 1, 3, 3, 2, 2, 4,4, 4, 4]

counting_sort(arr2, 4)

def is_palindrome(string):
    # if the length of the string is greater than 1 we must return the true
    if len(string) <= 1:
        return True
    # create a list of each character in the string
    charlist = [char for char in string]
    # pop the first letter
    start = charlist.pop(0)
    # pop the last letter
    end = charlist.pop(-1)
    # if the first and last characters dont match its not a palindrome
    if start != end:
        return False
    # else return the recursed value of charlist
        # (without its beginning and ending letters)
    # until the string is only one or no letters
    # or
    # until start and end differ
    else:
        s = ""
        return is_palindrome(s.join(charlist))






    # if len(string) == 0:
    #     return string
    # comparing = ""
    # charlist = [c for c in string]
    # while charlist:
    #     comparing+= charlist.pop(-1)


    # return comparing == string

print(is_palindrome('hhh'))