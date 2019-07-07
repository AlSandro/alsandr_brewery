"""

Find Single Number in the list of duplicates

"""
def singleNumber(nums: int):
    elem = 0
    no_duplicates = []
    for num in nums:
        if num not in no_duplicates:
            no_duplicates.append(num)
        else:
            no_duplicates.remove(num)
        
    return no_duplicates.pop()

mult_numbers_list = [1, 2, 3, 5, 6, 2, 3, 6, 1]
print(singleNumber(mult_numbers_list))