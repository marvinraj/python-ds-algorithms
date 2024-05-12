# selection sort algorithm

"""
HOW SELECTION WORKS --
Selection sort algorithm is described as an in-place comparison based algorithm that divides 
an array into 2 parts, sorted is on the left side and unsorted on the right side. After each
iteration, the algorithm selects the smallest element from the unsorted portion of the list
and swaps it with the first element of the unsorted part.

STEPS --
1. get unsorted array
2. set first element as the min value
3. loop through the second element to the last element to find the smallest value and then
swap it with the first element
4. hence, now the first element of the array is the sorted part
5. now, compare second element with all elements after it, find the smallest and swap with it
6. repeat step 5 until all sorted
"""

def selection(arr):
    print(f"unsorted array : {arr}")

    # get array length
    arr_len = len(arr)

    # loop through every element
    for i in range(arr_len):
        # get min value, which is i
        min_index = i
        # loop through second element until last element
        for j in range(i+1, arr_len):
            # if current element smaller min value, min index = current element index
            if arr[j] < arr[min_index]:
                smallest_index = j
                min_index = smallest_index

        # swap current element with smallest element
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp

        # view array after each iteration
        # print(f"when i = {i} : {arr}") 

    print(f"sorted array : {arr}")
    
if __name__ == '__main__':
    arr = [5,4,2,3,1,7,11,9,10]
    # i = 0
    # [1,4,2,3,5]
    # i = 1
    # [1,2,4,3,5]
    # i = 2
    # [1,2,3,4,5]
    selection(arr)