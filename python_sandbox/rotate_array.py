class RotateArray:

	# def __init__(self, nums, k):
		# self.nums = nums
		# self.k = k
       

	def rotateArray (self, nums, k):

		"""
		rotate the array number (k) of steps
		
		Solution. Slice the array 

		"""

		split_index = len(nums) - k 

		nums[:] = nums[split_index:] + nums[:split_index]

		return nums

arry = [3, 7, 9, 10, 12, 9]
rotte = RotateArray()
print(rotte.rotateArray(arry, 3))