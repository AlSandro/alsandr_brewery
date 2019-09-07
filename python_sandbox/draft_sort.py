import random

# def selection_sort(arr):
# 	for i in range(len(arr)):
# 		min_index = i
# 		for j in range (i+1, len(arr)):
# 			if arr[j] < arr [min_index]:
# 				min_index = j

# 		arr[min_index], arr[i] = arr[i], arr[min_index]

# 	return arr



arr = [10,4,8,9,3,17,2,19]
arr2 = [17,2,19,10,4,8,9,3]

# def bunble_sort(arr):
# 	for sorted in range(len(arr)-1, 0, -1):
# 		for i in range(sorted):
# 			if arr[i] > arr[i+1]:
# 				arr[i], arr[i+1] = arr[i+1],arr[i]
# 	return arr

# print(bunble_sort(arr))

def select_sort(arr):
	for i in range(len(arr)): # start main loop i in range of the list length
		min = i # set index of minum values as i and shift the sorted area each time
		for j in range(i+1, len(arr)): # another loop, with same len but starting i+1, thus it doesn't touch the sorted part
			if arr[j] < arr[min]: # if the value of any member of the list is smaller than current value at index [min], 
				min = j # change the current min to the index
		arr[min],arr[i] = arr[i], arr[min] # swap values

	return arr


print(select_sort(arr))


"""
return numbers sum of which can make the n
"""


def pairSum(arr, n):
	seen = set() # set to stack seen elements 
	pairs = set() # set to store pairs which make sum 

	for num in arr:
		match = n - num
		if match not in seen:
			seen.add(num)
		else:
			pairs.add( (max(match, num), min(match, num)) )
	return pairs


# n = random.randrange(1, 99)
# test_array = random.sample(range(100), k=100)

# print(pairSum(test_array, n))


# """
# Take an array and find maximum sum of the array. Streaming sum.
# """

# def largestSum(arr):
# 	if le(arr) < 1:
# 		return print('there is nothing to count')

# 	max_sum = current_sum = arr[0]

# 	for num in arr[1:]:
# 		current_sum = max(current_sum + num, num)
# 		max_sum = max(current_sum, max_sum)

# 	return max_sum



"""
Reverse a string

start  = "This is the best"

finish =  "best is the This" 

"""

# def reverseStrings(str):

# 	lis = str.split()
# 	lis = lis[::-1]
# 	print(lis)
# 	return " ".join(reversed(str.split()))

# print (reverseStrings("This is the best"))

arr = [10,4,8,9,3,17,2,19]
arr2 = [17,2,19,10,4,8,9,3]

# def if_array_rotation_of_array(arr, arr2):
# 	if len(arr) != len(arr2):
# 		return False

# 	key = arr[0]
# 	key_index = 0




# print(if_array_rotation_of_array(arr, arr2))
# test_string = "Clint Eastwoood"

# def isAnagramm(ana, gram):
# 	str1 = ana.replace(' ', '').lower() # just to fix the strings
# 	str2 = gram.replace(' ', '').lower() # just to fix the strings
# 	print(str1, str2) 


# 	count = {}

# 	for s in str1:
# 		if s not in count:
# 			count[s] = 1
# 		else: 
# 			count[s] += 1
# 	for s in str2:
# 		if s not in count:
# 			count[s] = 1
# 		else:
# 			count[s] -= 1

# 	if sum(count.values()) == 0:
# 		return True
# 	else:
# 		return False

# print(isAnagramm("themorsecode","themorsecode"))

"""

# print (sum(selection_sort(arr))) 


# def customReplace(string_to_replace, take_char, replace_with):
# 	temp = list(string_to_replace)
# 	for i in range(len(string_to_replace)):
# 		if temp[i] not in take_char:
# 			temp[i] = replace_with
# 	return ''.join(temp)

# alpha_list = []

# for i in range(ord("A"),ord("z")):
# 	alpha_list.append(chr(i))

# print(customReplace("sakjadsjk kdj iqwu iad989(&*y89n(* 89 (*(**( 89 89 AWDJKAHDKAWD", alpha_list, " "))

# print (range(ord("A"),ord("z")))

"""