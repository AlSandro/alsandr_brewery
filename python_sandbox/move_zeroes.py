"""

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
Do not return anything, modify nums in-place instead.

"""

def moveZeroes(self, nums: List[int]) -> None:
    i = 0  # we need that to count number not zeroes
    for num in nums: 
        if num != 0: # if not 0 move to the iterator position (preserve the order)
            nums[i] = num 
            i += 1 # increase counter
            
    nums[i:] = (len(nums)-i)*[0]  # slice from the number of not 0 and replace with 0
    print (nums)

def moveZeroesRemoveAppend(nums: List[int]):
    """
    Interesting solution...
    """
    for i in nums:
        if i == 0:
            nums.remove(i)
            nums.append(0)