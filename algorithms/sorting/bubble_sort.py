# bubble sort algorithm

"""
HOW BUBBLE WORKS --
Bubble sort algorithm works by repeatedly swapping current element with
the element next to it if they are not in the correct order. At each 
iteration of traversing left to right, the largest element among the 
unsorted elements is moved to the left/end.

STEPS --
1. get unsorted array
2. find number of elements in the array as it equals to the number of iterations
3. get the first element and compare it with the element next to it (right)
    - if right is larger than left, swap places
    - if right is smaller, do nothing
4. repeat step 3 up until the last element
5. repeat step 2 & 3 until array is sorted, number of iterations = number of elements
in the array
"""

def bubble_sort(arr):
    # get length of array
    arr_len = len(arr)
    
    # first for loop to iterate throught the elements = number of elements
    # this done because after each iteration, the largest element will be
    # added to the end, hence the iteration continues to do the same for 
    # the remaining elements.
    for i in range(arr_len):
        # this is done in order to avoid swapping after the largest element
        # moves to the end of the array
        after_swap = arr_len-i-1
        # second for loop to check and swap current element with the element
        # next to it
        for j in range(after_swap):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

if __name__ == '__main__':
    arr = [5,2,4,8,9]
    print(f"unsorted array : {arr}")
    bubble_sort(arr)
    print(f"sorted array using bubble sort : {arr}")