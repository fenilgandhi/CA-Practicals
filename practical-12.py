{
    "Author": "Fenil Gandhi",
    "Version": "Python 3.6.2",
    "Description": "Implement LCS problem",
    "Input Parameters": "2 String Sequences",
    "Input": ["abcef", "pqrabcdef"],
    "Output": "The Longest Common Subsequence between 'abcef' and 'pqrabcdef' is abcef of 5 characters",
}


def LCS(x, y):
    subsequence = ''
    if len(x) > len(y):
        x, y = y, x

    solution = [0] + [0] * len(x)
    prev = solution
    if x[0] == y[0]:
        subsequence += y[0]

    for j in range(len(y)):
        for i in range(1, len(x) + 1):
            if (x[i - 1] == y[j]):
                solution[i] = max(0, prev[i - 1] + 1)
            else:
                solution[i] = max(solution[i - 1], solution[i])

        if solution != prev:
            subsequence += y[j]
        prev = solution[:]

    print("The Longest Common Subsequence between \"{0}\" and \"{1}\" is {2} of {3} characters".format(x, y, subsequence, solution[-1]))


if __name__ == '__main__':
    LCS("abcef", "pqrabcdef")
