# counting sort algorithm
# links - https://www.programiz.com/dsa/counting-sort

""" 
STEPS --
1 -- get unsorted array
2 -- find the max element in the unsorted array
3 -- create a 'count' array length of max+1
4 -- get the count of each element in the array -- store in a count array
5 -- get cummulative value of the count array
6 -- the values in the count array correspond to the index in the sorted array 
(example - value 4 in unsorted array, so find the value at index 4 in the count array, 
that value-1 is then the index of value 4 in a the sorted array)
7 -- if there are similar values in the unsorted array, the value/count in the 
count array that corresponds to the similar values needs to be added by 1 
"""


def counting_sort(array):
    print(f"array to sort : {array}")
    # get max val, create count array & temp array 
    max_val = max(array)
    count = [0]*(max_val+1)
    temp = [0]*len(array)

    # count for each element at their own index in count array
    for i in array:
        count[i] += 1
    print(f"count for each element = {count}")
    
    # obtain cummulative values of count array
    for i in range(1, len(count)):
        count[i] = count[i-1] + count[i]
    print(f"cummulative values = {count}")

    # the values in the unsorted array will act as the index in the
    # count array to obtain the value to be used as index-1 in
    # sorted array
    for i in range(len(array)):
        current_element = array[i]
        value_from_count = count[current_element]-1
        count[current_element] = value_from_count
        temp[value_from_count] = current_element

    # copy values from temp array into original array
    for i in range(len(temp)):
        array[i] = temp[i]

    print(f"\nsorted array : {array}")

if __name__ == '__main__':
    array = [3,2,4,5,1,1,5,4,2,6,7,8,5]
    counting_sort(array)
