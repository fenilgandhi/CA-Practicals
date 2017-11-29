{
    "Author": "Fenil Gandhi",
    "Version": "Python 3.6.2",
    "Description": '''The array a[0:9]=[4,2,6,7,1,0,9,8,5,3] is to be sorted using insertion sort.
            Show the best case, average case and worst case analysis.''',
}

import time

def timeit(func):
    def decorated_function(*args):
        a = time.time()
        func(*args)
        b = time.time()
        print("Time taken is {0}".format( b-a ))
    return decorated_function

@timeit
def InsertionSort(input):
    for i in range(len(input)):
        while ((i > 0) and (input[i] < input[i - 1])):
            input[i], input[i - 1] = input[i - 1], input[i]
            i -= 1
    return input


if __name__ == '__main__':
	array = [4,2,6,7,1,0,9,8,5,3]
	InsertionSort(array)
	