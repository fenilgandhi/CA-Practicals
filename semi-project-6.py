{
    "Author": "Fenil Gandhi",
    "Version": "Python 3.6.2",
    "Description":
        "Write a program that implement divide and conquer method to find the maximum and minimum of n elements. Use recursion to implement the divide and conquer scheme.",
}

import random 

def recursive_max_min(array):
    if len(array) < 2:
        return {"min" : array[0] , "max" : array[0] }
    else:
        mid = len(array) // 2
        return {
        	"max" : max( recursive_max(array[:mid]) , recursive_max(array[mid:]) ),
        	"min" : min( recursive_min(array[:mid]) , recursive_min(array[mid:]) )
        }
        


if __name__ == '__main__':
	array = [random.randint(0,1000) for _ in range(100)]
	ans = recursive_max_min(array)
	print (array , ans , sep="\n")