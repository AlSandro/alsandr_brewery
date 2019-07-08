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


def sort_buble(arr):

	for unsorted in range(len(arr)-1, 0, -1):
		for i in range(unsorted):
			if arr[i] > arr[i+1]:
				arr[i], arr[i+1] = arr[i+1], arr[i]
	return arr

def sort_select(arr):
	"""
	make one large loop going through all the elements. each time it moves forward leaving already sorted elements from min
	add minimum_index, which will chage when we run through second loop and insert the el with min value to the first loop [i]
	add second (small) loop to iterate within the unsorted part
	"""
	for i in range(len(arr)):
		min_ind = i
		for j in range( i + 1, len(arr)): # not sorted range
			if arr[j] < arr[min_ind]:
				min_ind = j
		arr[min_ind], arr[i] = arr[i], arr[min_ind]

	return arr



def mirror_a_list(arr):
	middle = len(arr)//2
	print(arr[:middle:-1], arr[:middle])
	arr[:] = arr[:middle:-1] + arr[:middle]
	return arr 

print (mirror_a_list([10, 15, 4, 7, 19, 3, 10, 0, -2, 18, -20]))

# print(Fibonacci(5))


# for i in range(50, 50):

# 	print(Fibonacci(i))
	# print(Fibonacci(30))
	# print(Fibonacci(100))