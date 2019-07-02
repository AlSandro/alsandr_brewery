#! /usr/bin/env python3

# Vars
my_str = "boo"
my_int = 7
my_bool = True


# Loops

for i in range(10):
	print ('my var in the for loop is ' + str(i))

foo = 0
while foo < 10:
	foo+=1
	if foo%2 == 0:
		continue
	elif foo == 9:
		break
	else:
		print ('my foo is odd' + str(foo))
