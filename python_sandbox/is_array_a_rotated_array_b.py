
arr = [10,4,8,9,3,17,2,19]
arr2 = [17,2,19,10,4,8,9,3]


def rotate_array(arr, k):
	for i in range(k):
		temp = arr.pop()
		arr.insert(0,temp)

	return arr



def sort_arr(arr):
	for i in range(len(arr)):
		sorted = i
		for j in range(i+1, len(arr)):
			if arr[j] < arr[sorted]:
				sorted = j
		arr[sorted], arr[i] = arr[i], arr[sorted]

	return arr



"""

figure out is array two is rotated array one

for example:
arr = [10,4,8,9,3,17,2,19]
arr2 = [17,2,19,10,4,8,9,3]

arr2 == arr with elements rotated


# """
# def if_array_rotation_of_array(arr, arr2):
# 	if len(arr) != len(arr2):
# 		print("I ran in #1")
# 		return False

# 	key = arr[0]
# 	key_index = 0
# 	key_index = arr2.index(key)

# 	if arr[:key_index] == arr2[key_index:] and arr2[:key_index] == arr1[key_index:]
	# for i in range (len(arr2)): 
	# 	print(arr2[i],key)
	# 	if arr2[i] == key:
	# 		print ("I ran in #2")
	# 		key_index = i
	# 		break

	# if key_index == 0:
	# 	print ("I ran in #3")
	# 	return False

	# for x in range(len(arr)):
	# 	arr2_index = (key_index + x) % len(arr)
	# 	if arr[x] != arr2[arr2_index]:
	# 		print ("I ran in #4")
	# 		return False

	# return True
	# counter = 0
	# for x in arr[key_index:]:
	# 	print(x,arr2[counter])
	# 	if x == arr2[counter]:
	# 		counter += 1
	# 	else:
	# 		return False

	# return True

print (rotate_array(arr, 2))

print(sort_arr(arr))

# ind = 3

# print (arr[:(len(arr)-ind)], arr2[ind:])

# print (arr2[:ind], arr[(len(arr)-ind):])


# print(if_array_rotation_of_array(arr, arr2))