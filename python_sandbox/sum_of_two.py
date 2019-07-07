import random

"""
Find all the indexes of the values sum of which is K

"""

def all_sums_of_two(arr, k):
	seen_keys = {}
	found_indexes = []
	found_values = []
	for i, num in enumerate(arr):
		# if we have a key sum of which plus the current key is K, we store the index of both in the list(set?)
		if k - num in seen_keys:
			found_indexes.append((seen_keys[k-num], i))
			found_values.append(((k-num),num))
		else:
			seen_keys[num] = i
	print ("The indexes are {0}. \n And the values are {1}".format(str(found_indexes), str(set(found_values))))

test_array = list(range(1, 100))
test_array2 = random.sample(range(100), 100)
print(test_array2)
random.shuffle(test_array)
print(test_array)

all_sums_of_two(test_array, 36)

# as it seen on TV
def twoSum(nums, target):
    num_to_index = {}
    for i, num in enumerate (nums):
        if target - num in num_to_index: # if target minus current number equal to one of the previous nums, means the sum if that target
            return [num_to_index[target - num], i] # We have first index of the number if seen dictionary and second the current i
        print (num_to_index)
        num_to_index[num] = i # add number to a list

    return []

# test_number = 29
# test_array = range(1, 100)
# result = twoSum(test_array,test_number)
# print(result)


