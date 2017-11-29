{
    "Author": "Fenil Gandhi",
    "Version": "Python 3.6.2",
    "Description":
        '''Write a program to determine whether or not a character string has an unmatched parenthesis.
        Use a stack. What is the time complexity of your program? Can we replace the stack with a
        queue? ''',
}


import time
import random

def timeit(func):
    def decorated_function(*args):
        a = time.time()
        func(*args)
        b = time.time()
        return (b - a)
    return decorated_function


class Stack():
    def __init__(self):
        self.memory = []

    def push(self):
        self.memory += [0]

    def pop(self):
        return self.memory.pop()

    def length(self):
        return len(self.memory)


def generatestr(length):
    chars = "[]+-<>"
    return "".join([chars[random.randint(0,6)] for _ in range(length)])


@timeit
def solve(string):
    print ("\nSolving " , string)
    # Solve using Stack
    stack = Stack()
    try:
        for c in string:
            print(c, stack.memory)
            if c == "[":
                stack.push()
            elif c == "]":
                stack.pop()
        if stack.length() > 0:
            raise IndexError
    except:
        print("Imbalanced Equation")
    else:
        print("It is perfectly balanced")


if __name__ == '__main__':
    s = generatestr(50)
    solve(s)
