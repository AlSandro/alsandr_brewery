import random

def countDuplicates(nums: int):
	unique_counter = 0 # start counting unique chars
	for i in range(len(nums)): # iterate through the array
	    if i == 0 or nums[i] != nums[i-1]: #condition, if not first element, and the element not equal previous e.g. unique
	        nums[unique_counter] = nums[i] # assign the current to previous
	        unique_counter += 1 # increment the counter for the not duplicated
	print(nums[:unique_counter])        
	return unique_counter

random_array = []
for i in range(20):
	random_array.append(random.randint(0, 20))

print (random_array)
random_array.sort()
print ( 'the length of the unique list is ' + str(len(set(random_array))))
print (countDuplicates(random_array))
print (countDuplicatesSet(random_array))
countDuplicatesSet