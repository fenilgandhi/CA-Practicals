'''
Implementation and Time analysis of linear and binary search algorithm
'''
import time


def sorted_array(size):
	return [i for i in range(size)]


def timeit(func):
	def decorated_function(*args):
		a = time.time()
		index, depth = func(*args)
		b = time.time()
		return (b - a, depth)
	return decorated_function


def print_formatted(name, input_sizes, time_taken):
	print(" " * 60, "{0:^50s}".format(name), "-" * 55, sep="\n")
	print("| {0:^10s} | {1:^10s} | {2:^10s} |".format("Input", "Time", "Depth"))
	print("-" * 55)
	for i in range(len(input_sizes)):
		print("| {0:>10d} | {1:>10f} | {2:>10d} |" .format(input_sizes[i], time_taken[i][0], time_taken[i][1]))
	print("-" * 55, end="\n\n")


@timeit
def BinarySearch(array, query):
	low = 0
	high = len(array) - 1

	i = 0
	while (low <= high):
		mid = (low + high) // 2
		i += 1
		midval = array[mid]
		if (midval < query):
			low = mid + 1
		elif(midval > query):
			high = mid
		else:
			return (mid, i)
	return -1


@timeit
def LinearSearch(array, query):
	index = 0
	for element in array:
		if (query == element):
			return (index, index)
		else:
			index += 1


if __name__ == '__main__':
	input_sizes = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000]

	# Binary Search
	time_taken = []
	for each_input in input_sizes:
		array = sorted_array(each_input)
		time_taken.append(BinarySearch(array, array[-1]))
	print_formatted("Binary Search", input_sizes, time_taken)

	# Linear Search
	time_taken = []
	for each_input in input_sizes:
		array = sorted_array(each_input)
		time_taken.append(LinearSearch(array, array[-1]))
	print_formatted("Linear Search", input_sizes, time_taken)


'''
						RESULTS
-------------------------------------------------------
                  Binary Search                   
-------------------------------------------------------
|   Input    |    Time    |   Depth    |
-------------------------------------------------------
|         10 |   0.000005 |          4 |
|         50 |   0.000004 |          6 |
|        100 |   0.000005 |          7 |
|        500 |   0.000006 |          9 |
|       1000 |   0.000006 |         10 |
|       5000 |   0.000007 |         13 |
|      10000 |   0.000010 |         14 |
|      50000 |   0.000030 |         16 |
|     100000 |   0.000019 |         17 |
-------------------------------------------------------

                                                            
-------------------------------------------------------
                  Linear Search                   
-------------------------------------------------------
|   Input    |    Time    |   Depth    |
-------------------------------------------------------
|         10 |   0.000009 |          9 |
|         50 |   0.000006 |         49 |
|        100 |   0.000009 |         99 |
|        500 |   0.000045 |        499 |
|       1000 |   0.000093 |        999 |
|       5000 |   0.000485 |       4999 |
|      10000 |   0.000985 |       9999 |
|      50000 |   0.005016 |      49999 |
|     100000 |   0.010332 |      99999 |
-------------------------------------------------------


'''