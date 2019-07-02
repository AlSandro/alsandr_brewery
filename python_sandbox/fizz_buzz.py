
"""
Fizz Buzz

Starting 1 count to the 'number'
Add Fizz if number divisible on 3
Add Buzz is number divisible on 5
Add FizzBuzz if divisible by both 
Add the number if none of the above true

"""

def fizzBuzz(number):
	fizz_buzz_list = [] # define empty list to be used inside of the loop
	for num in range(1, number+1): # catch. start from 1 not from 0, like the range start by default!
		fizz = (num % 3 == 0) # define fizz condition
		buzz = (num % 5 == 0) # define buzz condition
		if fizz and buzz:
			fizz_buzz_list.append('FizzBuzz')
		elif fizz:
			fizz_buzz_list.append('Fizz')
		elif buzz:
			fizz_buzz_list.append('Buzz')
		else:
			fizz_buzz_list.append(str(num))
	return fizz_buzz_list

print(fizzBuzz(50))