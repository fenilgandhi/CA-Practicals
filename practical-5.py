{
    "Author": "Fenil Gandhi",
    "Version": "Python 3.6.2",
    "Description": "Implementation of a knapsack problem using dynamic programming",
    "Input Parameters ": ["List of (value, weight) tuple", "Maximum Weight"],
    "Input": [[(100, 10), (150, 20), (200, 30)], 50],
    "Output":
        """
            Value       Weight      Quantity
            200         30          1.0
            150         20          1.0
            100         10          0.0
            Maximum Value possible with given weights is 350
        """,
}


def KnapSack(input, max_weight):
    if (len(input) < 1) or (max_weight < input[0][1]):
        return

    # Sort Items based on maximum Value
    input = sorted(input, reverse=True)

    total_value = 0
    print("{0}\t\t{1}\t\t{2}".format("Value", "Weight", "Quantity"))
    while (len(input) > 0):

        # Select a node
        current_value, current_weight = input.pop(0)

        if (current_weight <= max_weight):
            total_value += current_value
            max_weight -= current_weight
            print("{0}\t\t{1}\t\t1.0".format(
                current_value, current_weight))
        else:
            print("{0}\t\t{1}\t\t0.0".format(
                current_value, current_weight))

    return total_value


if __name__ == '__main__':
    input = [
        (100, 10),
        (150, 20),
        (200, 30),
    ]
    max_value = KnapSack(input, 50)
    print("Maximum Value possible with given weights is {0}".format(max_value))
