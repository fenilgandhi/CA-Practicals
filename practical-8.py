{
    "Author": "Fenil Gandhi",
    "Version": "Python 3.6.2",
    "Description": "Implementation of a knapsack problem using greedy algorithm",
    "Input Parameters": ["List of coins", "Total Change"],
    "Input": [[(100, 10), (150, 20), (200, 30)], 50],
    "Output":
        """
            Value       Weight      Quantity
            100         10          1.0
            150         20          1.0
            200         30          0.667
            Maximum Value possible with given weights is 383.333
        """,
}


def KnapSack(input, max_weight):
    if (len(input) < 1) or (max_weight < input[0][1]):
        return

    # Sort Items based on maximum benefit
    input = sorted(input, key=lambda a: a[0] / a[1], reverse=True)

    total_value = 0
    print("{0}\t\t{1}\t\t{2}".format("Value", "Weight", "Quantity"))
    while (max_weight > 0) and (len(input) > 0):
        # Select a node
        current_value, current_weight = input.pop(0)

        if (current_weight <= max_weight):
            total_value += current_value
            max_weight -= current_weight
            print("{0}\t\t\t{1}\t\t\t1.0".format(current_value, current_weight))
        else:
            partial_value = (current_value / current_weight) * max_weight
            total_value += partial_value
            print("{0}\t\t\t{1}\t\t\t{2}".format(current_value, current_weight, round(max_weight / current_weight, 3), max_weight))
            max_weight = 0
    while (len(input) > 0):
        current_value, current_weight = input.pop(0)
    if (max_weight > 0):
        print("You have {0} units remaining weight".format(max_weight))
    return round(total_value, 3)


if __name__ == '__main__':
    input = [
        (100, 10),
        (150, 20),
        (200, 30),
    ]
    max_value = KnapSack(input, 50)
    print("Maximum Value possible with given weights is {0}".format(max_value))
