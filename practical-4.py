{
    "Author": "Fenil Gandhi",
    "Version": "Python 3.6.2",
    "Description": "Implementation and Time analysis of factorial program using iterative and recursive method",
    "Input": [1, 5, 10, 20, 30, 40, 50, 100, 500, 1000, 3000],
    "Output":
        """
            ---------------------------
            |   Iterative Factorial   |
            ---------------------------
            |   Input    |    Time    |
            ---------------------------
            |          1 | 0.00000167 |
            |          5 | 0.00000215 |
            |         10 | 0.00000286 |
            |         20 | 0.00000477 |
            |         30 | 0.00000644 |
            |         40 | 0.00000858 |
            |         50 | 0.00001097 |
            |        100 | 0.00002360 |
            |        500 | 0.00020289 |
            |       1000 | 0.00066137 |
            |       3000 | 0.00470996 |
            ---------------------------

            ---------------------------
            |    Recursive Factorial  |
            ---------------------------
            |   Input    |    Time    |
            ---------------------------
            |          1 | 0.00000334 |
            |          5 | 0.00000548 |
            |         10 | 0.00000525 |
            |         20 | 0.00000834 |
            |         30 | 0.00001192 |
            |         40 | 0.00001502 |
            |         50 | 0.00002003 |
            |        100 | 0.00004601 |
            |        500 | 0.00072169 |
            |       1000 | 0.00112271 |
            |       3000 | 0.00597692 |
            ---------------------------
        """,
}

import time
import sys

sys.setrecursionlimit(3050)


def timeit(func):
    def decorated_function(*args):
        a = time.time()
        func(*args)
        b = time.time()
        return (b - a)
    return decorated_function


def iterative_factorial(n):
    ans = 1
    while (n > 1):
        ans = ans * n
        n -= 1
    return ans


def recursive_factorial(n):
    if (n > 1):
        return n * recursive_factorial(n - 1)
    else:
        return 1


def print_formatted(name, input_sizes, time_taken):
    print(" " * 60, "{0:^50s}".format(name), "-" * 55, sep="\n")
    print("| {0:^10s} | {1:^10s} |".format("Input", "Time"))
    print("-" * 55)
    for i in range(len(input_sizes)):
        print("| {0:>10d} | {1:>2.8f} |".format(input_sizes[i], time_taken[i]))
    print("-" * 55, end="\n\n")


# Decorating Recursive Functions
timed_iterative_factorial = timeit(iterative_factorial)
timed_recursive_factorial = timeit(recursive_factorial)

if __name__ == '__main__':
    input_sizes = [1, 5, 10, 20, 30, 40, 50, 100, 500, 1000, 3000]

    # Iterative Approach
    time_taken = []
    for each_input in input_sizes:
        time_taken.append(timed_iterative_factorial(each_input))
    print_formatted("Iterative Factorial", input_sizes, time_taken)

    # Recursive Approach
    time_taken = []
    for each_input in input_sizes:
        time_taken.append(timed_recursive_factorial(each_input))
    print_formatted("Recursive Factorial", input_sizes, time_taken)
