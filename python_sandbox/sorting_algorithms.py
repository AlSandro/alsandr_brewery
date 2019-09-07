import random

"""
Insertion Sort
"""

def insertion_sort(array_int):
        
    for i in range(len(array_int)): # count through array
        cursor = array_int[i] # selected int 
        pos = i #reset position each time to the counter
        
        while pos > 0 and array_int[pos - 1] > cursor:
            # Swap the number down the list
            array_int[pos] = array_int[pos - 1]
            pos = pos - 1
            print (array_int)
        # Break and do the final swap
        array_int[pos] = cursor 

    return array_int


def selection_sort(arr):

	for i in range (len(arr)): # sorted range
		minimum = i # this will shift the sorted part each time
		for j in range( i + 1, len(arr)): # not sorted range
			if arr[j] < arr[minimum]:
				minimum = j
		arr[minimum],arr[i] = arr[i],arr[minimum]
	return arr
    # for i in range(len(arr)):
    #     minimum = i
        
    #     for j in range(i + 1, len(arr)):
    #         # Select the smallest value
    #         if arr[j] < arr[minimum]:
    #             minimum = j

    #     # Place it at the front of the 
    #     # sorted end of the array
    #     arr[minimum], arr[i] = arr[i], arr[minimum]
            
    

random_array = []
for i in range(5):
	random_array.append(random.randint(0, 20))
print(random_array)
# print(insertion_sort(random_array))
print(selection_sort(random_array))