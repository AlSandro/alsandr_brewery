
import re

"""

Given an array, what is the most frequently occuring element

"""

def most_frequent(arr):
	dict_char = {}
	elem = None
	max_val = 0
	for c in arr: 
		if c in dict_char:
			dict_char[c] += 1

		else: 
			dict_char[c] = 1

		if dict_char[c] > max_val:
			elem = c
			max_val = dict_char[c]

	return elem, max_val

def all_unique(arr):  # and possibly not duplicates? using set()
	count = {}
	list_dupl = []
	for c in arr: 
		if c in count:
			count[c] += 1
			list_dupl.append(c)
		else: 
			count[c] = 1
	unique = set(arr) - set(list_dupl)  # find difference berween set of unique in original array and the duplicates array
	return unique

"""
Given a string all char unique

Return True or false if string if all characters unique

"""

pattern  = re.compile('[^\w]')
test_string = 'ash&*, +JKO : W jk eoumnq lwp'
def unique(test_string):
	temp = re.sub(pattern, '', test_string)
	return len(set(temp)) == len(temp)

# pattern  = re.compile('[^a-zA-Z0-9\\\/]|_')


# print(unique(test_string))

string_list  =  list("dhsak masdmn sakjdh ka sjdh klk oidsc kjhdkjashdkjasdkj haskjd haskjdas dkhlkj")

# for i in string_list:
# 	print ('The var is %s, %s' % (i,'boo'))  # old format
# 	print ('The var is {1}, {0}'.format(i,'foo')) # new format


def sort_me(arr):

	for sorted in range(len(arr)-1, 0, -1):
		for i in range(sorted):
			if arr[i] > arr[i+1]:
				arr[i],arr[i+1] = arr[i+1],arr[i]
	print (arr)

def sort_me_sort(arr):
	for i in range(len(arr)):
		min_ind = i
		for j in range(1, len(arr)):
			if arr[j] < arr[min_ind]:
				min_ind = j

		arr[min_ind], arr[i] = arr[i],arr[min_ind]
	print (arr)



sort_me_sort([3, 4, 8, 1, 9, 6])
# print ("\n".join(string_list))

# print (unique('ash&*, +JKO : W jk eoumnq lwp'))

# string_for_count = "dhsakmasdmnsakjdh ka sjdh klkoidsc kjhdkjashdkjasdkjhaskjdhaskjdasdkhlkj"

# array_for_count = list(string_for_count.replace(' ', ''))

# print(array_for_count)

# print (all_not_duplicates(array_for_count))