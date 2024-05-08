# radix sort algorithm

"""
STEPS --

1. get array to sort
2. create function to sort array using counting algo
    a. sort elements based on the unit place
    b. sort elements based on the tens place
    c. sort elements based on the hundreds place
3. create function for radix algorithm
    a. get max value in the array, e.g. 691
    b. find number of digit in the max value, 691 -> 3
    c. loop through the array 3 times 
4. counting sort algorithm is called inside the radix algorithm
"""

def radix_sort(arr):
    max_val = max(arr)
    len_val = len(str(max_val))
    place = 1

    for i in range(len_val):
        counting_sort(arr,place)
        place = place*10

def counting_sort(array,place):
    print(f"array to sort : {array}")
    # create count array & temp array 
    count = [0]*10
    temp = [0]*len(array)

    # count for each element at their own index in count array
    for i in range(0, len(array)):
        # logic to get digits according to the place (unit,tenth,hundreds,etc)
        floor = array[i]//place
        mod = floor % 10
        count[mod] += 1
    print(f"count for each element = {count}")
    
    # obtain cummulative values of count array
    for i in range(1, len(count)):
        count[i] = count[i-1] + count[i]
    print(f"cummulative values = {count}")

    # the values in the unsorted array will act as the index in the
    # count array to obtain the value to be used as index-1 in
    # sorted array
    for i in range(len(array)):
        # store values from unsorted array to be used as index
        # -- take only units values
        floor = array[i]//place
        mod = floor % 10
        # use the units index in the count array to obtain the value-1
        val_from_count = count[mod]-1
        count[mod] = val_from_count

        # use value-1 as the index to store value from unsorted in sorted
        # -- store the entire value, not just the unit value
        temp[val_from_count] = array[i]

    # copy values from temp array into original array
    for i in range(len(temp)):
        array[i] = temp[i]

    print(f"sorted array : {array}\n")

if __name__ == '__main__':
    arr = [124,236,525,452,641]
    radix_sort(arr)
    # expected output 1 - 641,452,124,525,236
    # expected output 2 - 124,525,236,641,452
    # expected output 3 - 124,236,452,525,641