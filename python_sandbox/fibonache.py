# Function for recursive Fibonacci number 
  
def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==1: 
        return 0
    # Second Fibonacci number is 1 
    elif n==2: 
        return 1
    else: 
        return (Fibonacci(n-2)+Fibonacci(n-1))
  
def Fibonacci_series(Number):
	if(Number == 0):
		return 0
	elif(Number == 1):
		return 1
	else:
		return (Fibonacci_series(Number - 2)+ Fibonacci_series(Number - 1))


# Python Fibonacci series Program using For Loop

# Find & Displaying Fibonacci series
def fibonacci_iterate(n):
	first_number = 0
	second_number = 1
	fibonacci_sequence = [first_number, second_number]
	for num in range(0, n):
		if(num <= 1):
			next_num = num
		else:
			next_num = first_number + second_number
			first_number,second_number = second_number,next_num
		fibonacci_sequence.append(next_num)
	return fibonacci_sequence



# print(fibonacci_iterate(100))

print(Fibonacci_series(10))


# print(Fibonacci(5))


# for i in range(50, 50):

# 	print(Fibonacci(i))
	# print(Fibonacci(30))
	# print(Fibonacci(100))