import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--test_int', 
					default=123456789,
					action='store', 
					dest='simple_int',
                    help='an integer for the test')

parser.add_argument('--test_string',
					default='abracadabra',
					action='store',
					dest='simple_string',
                    help='a string for the test')

args = parser.parse_args()


"""

"""

def reverse_int_classic(some_integer: int):
	reverse_int = 0
	is_negative = some_integer < 0 # make sure to convert negative back 
	some_integer = abs(some_integer)
	while some_integer != 0: 
		reverse_int = reverse_int*10 + some_integer%10
		some_integer = some_integer // 10
	return reverse_int if not is_negative else -reverse_int


print(reverse_int_classic(int(args.simple_int)))