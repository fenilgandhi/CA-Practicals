"""
Implementation of a knapsack problem using greedy algorithm
Input : List of (value, weight) tuple
"""


def KnapSack(input, max_weight):
    if (len(input) < 1) or (max_weight < input[0][1]):
        return

    # Sort Items based on maximum benefit
    input = sorted(input, key=lambda a: a[0] / a[1], reverse=True)

    total_value = 0
    while (max_weight > 0) and (len(input) > 0):
        # Select a node
        current_value, current_weight = input.pop(0)

        if (current_weight <= max_weight):
            total_value += current_value
            max_weight -= current_weight
            print("(value : {0} , weight : {1} , amount_taken : 1.0, weight_left : {2}".format(current_value, current_weight, max_weight))
        else:
            partial_value = (current_value / current_weight) * max_weight
            total_value += partial_value
            print("(value : {0} , weight : {1} , amount_taken : {2}, weight_left : {3}".format(current_value, current_weight, max_weight / current_weight, max_weight))
            max_weight = 0
    while (len(input) > 0):
        current_value, current_weight = input.pop(0)
        print("(value : {0} , weight : {1} , amount_taken : 0.0".format(current_value, current_weight))
    if (max_weight > 0):
        print("You have {0} remaining weight".format(max_weight))
    return total_value


if __name__ == '__main__':
    input = [
        (151, 150),
        (150, 150),
    ]
    max_value = KnapSack(input, 1500)
    print("Maximum Value possible with given weights is {0}".format(max_value))
