{
    "Author": "Fenil Gandhi",
    "Version": "Python 3.6.2",
    "Description":
        "Write a program for 0/1 knapsack problem using this heuristic : Pack the knapsack in non increasing order of profit density",
}


def KnapSack(input, max_weight):
    if (len(input) < 1) or (max_weight < input[0][1]):
        return

    # Sort Items based on maximum benefit
    input = sorted(input, key=lambda a: a[1], reverse=True)

    total_value = 0
    print("{0}\t\t{1}\t\t{2}".format("Value", "Weight", "Quantity"))
    while (len(input) > 0):
        # Select a node
        current_value, current_weight = input.pop(0)

        if (current_weight <= max_weight):
            total_value += current_value
            max_weight -= current_weight
            print("{0}\t\t\t{1}\t\t\t1.0".format(
                current_value, current_weight))
        else:
            print("{0}\t\t\t{1}\t\t\t0.0".format(
                current_value, current_weight))
    if (max_weight > 0):
        print("You have {0} units remaining weight".format(max_weight))
    return round(total_value, 3)


if __name__ == '__main__':
    input = [
        #Weight, Profit
        (100, 10),
        (150, 20),
        (200, 30),
    ]
    max_value = KnapSack(input, 50)
    print(
        "Maximum Value possible using given heuristic is {0}".format(max_value))
