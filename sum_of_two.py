
# as it seen on TV
def twoSum(nums, target):
    num_to_index = {}
    for i, num in enumerate (nums):
        if target - num in num_to_index: # if target minus current number equal to one of the previous nums, means the sum if that target
            return [num_to_index[target - num], i] # We have first index of the number if seen dictionary and second the current i
        print (num_to_index)
        num_to_index[num] = i # add number to a list

    return []

test_number = 29
test_array = range(1, 100)
result = twoSum(test_array,test_number)
print(result)
