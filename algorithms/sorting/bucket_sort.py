# bucket sort algorithm

"""
steps --
-- 1. create unsorted array
-- 2. 
-- 3. 
-- 4. use another sorting algorithm to sort out the elements in each bucket
    -- use insertion sorting i think
-- 5. gather all elements from each bucket
"""

def bucket_sorting(array, no_of_buckets):
	# get max and min element in array
	max_element = max(array)
	min_element = min(array)

	# calculate range
	calc_range = (max_element - min_element) / no_of_buckets

	# create temp array
	temp = []

	# create empty buckets which will be used to store elements from unsorted array
	for i in range(no_of_buckets):
		temp.append([])

	# distribute elements from unsorted array into buckets
	for i in range(len(array)):
		diff = (array[i] - min_element) / calc_range - int((array[i] - min_element) / calc_range)

		if(diff == 0 and array[i] != min_element):
			temp[int((array[i] - min_element) / calc_range) - 1].append(array[i])

		else:
			temp[int((array[i] - min_element) / calc_range)].append(array[i])

	# sort the elements in each buckets individually
	for i in range(len(temp)):
		if len(temp[i]) != 0:
			temp[i].sort()

	# gather all elements from all the buckets to get sorted array
	k = 0
	for lst in temp:
		if lst:
			for i in lst:
				array[k] = i
				k = k+1

if __name__ == "__main__":
	arr = [1,1,1,2,2,3,3,4,5,6]
	no_of_buckets = 10
	bucket_sorting(arr, no_of_buckets)
	print("sorted array : " + str(arr))
	