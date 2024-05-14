# insertion sorting algorithm

"""
HOW INSERTION WORKS --
Insertion algorithm works by iteratively inserting each element of the unsorted 
array into the correct position in the sorted portion of the array.

STEPS --
1. get unsorted array
2. set first element of array as sorted
3. get the second element and compare it with the first element, if smaller place it before it
4. now, first and second elements are both sorted
5. get the third element and compare it with the elements on the left of it, if smaller than an 
element then place it just after that element
6. do the same for every unsorted element
"""

def insertion_sort(arr):
    print(f"unsorted array : {arr}")

    # get length of array
    arr_len = len(arr)

    # compare the current element, starting with the second element,
    # with every element before it
    for i in range(1, arr_len):
        # store the first element in the unsorted array
        key = arr[i]
        # store index of the element before the unsorted array
        j = i-1

        # compare key with elements from the sorted list & place it at the correct place
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            arr[j] = key
            j = j-1
            
    print(f"sorted array : {arr}")



if __name__ == "__main__":
    arr = [4,2,5,3,1,8,7,6,10,9]
    insertion_sort(arr)