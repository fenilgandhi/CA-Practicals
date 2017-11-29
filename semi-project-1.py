{
    "Author": "Fenil Gandhi",
    "Version": "Python 3.6.2",
    "Description":
        '''List the factors that may influence the space complexity of a program.
            Write a recursive and nonrecursive function to compute n!
            Compare the space requirements of nonrecursive function with those of recursive version.''',
    "Input": "3000!"
    "Output": {
        "recursive_factorial": {"memory": "15.902 Mb", "runTime": "13.890 ms", },
        "non_recursive_factorial": {"memory": "12.878 Mb", "runTime": "14.874 ms", }

    }
}

'''
Factors affecting the space complexity of a program
'''
import sys
sys.setrecursionlimit(3050)


def recursive_factorial(n):
    if n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)


def non_recursive_factorial(n):
    ans = 1
    while(n > 1):
        ans *= n
        n -= 1
    return ans


if __name__ == '__main__':
    n = 3000
    recursive_factorial(n)
    non_recursive_factorial(n)
