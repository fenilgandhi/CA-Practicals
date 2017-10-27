'''
Implementation of chain matrix multiplication using dynamic programming.
'''
import sys

values = {}


def Matrix_Chain(dimensions):
    n = len(dimensions)

    for i in range(n):
        values[(i, i)] = 0

    for row in range(2, n):
        for i in range(1, n - row + 1):
            j = i + row - 1

            values[(i, j)] = sys.maxsize
            for k in range(i, j):
                mult = values[(i, k)] + values[(k + 1, j)] + dimensions[i - 1] * dimensions[j] * dimensions[k]
                values[(i, j)] = mult if mult < values[(i, j)] else values[(i, j)]

    return values[(1, n - 1)]


if __name__ == '__main__':
    dimensions = [5, 10, 20, 30]
    steps = Matrix_Chain(dimensions)
    print("Mininum Steps to multiply {0} will be {1} steps".format(dimensions, steps))
