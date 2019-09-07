#! /usr/bin/env python3


import random

test_array = random.sample(range(100), k=10)
# Vars
# my_str = "boo"
# my_int = 7
# my_bool = True


# # Loops

# for i in range(10):
# 	print ('my var in the for loop is ' + str(i))

# foo = 0
# while foo < 10:
# 	foo+=1
# 	if foo%2 == 0:
# 		continue
# 	elif foo == 9:
# 		break
# 	else:
# 		print ('my foo is odd' + str(foo))

def buble_sort(arr):

	for sorted_range in range (len(arr)-1, 0, -1):
		for i in range (sorted_range):
			if arr[i] > arr[i+1]:
				arr[i], arr[i+1] = arr[i+1],arr[i]

	return arr


def sorting_sort(arr):
	for i in range (len(arr)):
		min_ind = i
		for j in range(i+1,len(arr)):
			if arr[j] < arr[min_ind]:
				min_ind = j
		arr[i], arr[min_ind] = arr[min_ind], arr[i]
	return arr

intergra = 129837289137912

def reverse_int(integr):
	return_int = 0
	while integr > 0:
		return_int = return_int*10 + integr%10
		integr //= 10
	return return_int

def rotate_int_arr(arr, steps):

	for i in range(steps):
		arr.insert(0,arr.pop())
	return arr



print(reverse_int(intergra))
print(test_array)
print(rotate_int_arr(test_array, 4))
print(sorting_sort(test_array))
print(buble_sort(test_array))
arr = [10,4,8,9,3,17,2,19]