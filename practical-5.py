'''
Implementation of a knapsack problem using dynamic programming.
Input : List of (value, weight) tuple
'''


def KnapSack(input, max_weight):
    if (len(input) < 1) or (max_weight < input[0][1]):
        return

    # Sort Items based on maximum Value
    input = sorted(input, reverse=True)

    total_value = 0
    while (max_weight > 0) and (len(input) > 0):
        # Select a node
        current_value, current_weight = input.pop(0)

        if (current_weight <= max_weight):
            total_value += current_value
            max_weight -= current_weight

    return total_value


if __name__ == '__main__':
    input = [
        (100, 10),
        (150, 20),
        (200, 30),
    ]
    max_value = KnapSack(input, 50)
    print("Maximum Value possible with given weights is {0}".format(max_value))
