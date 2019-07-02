#! /usr/bin/env python3

"""
Task. Reverse string, classic way, no python slicing 

"""
def reverse_string_classic(some_string = 'abracadabra'):
	char_list = list(some_string)
	for i in range(len(char_list) // 2): # run the loop half of the list size 
		temp = char_list[i] # temporarily store left char 
		char_list[i] = char_list[len(char_list) - i - 1 ] # take character form the right and assign instead of the left
		char_list[len(char_list) - i - 1 ] = temp # assign the temporary "left" char back

	return ''.join(char_list)

def reverse_string_slicing(some_string = 'abracadabra'):
	return some_string[::-1]
    
def if_palindrome():
	return True
word_to_reverse = "HELLO WORLD"

print(word_to_reverse)
print (reverse_string_classic(word_to_reverse))
print (reverse_string_slicing(word_to_reverse))
print (reverse_string_classic())