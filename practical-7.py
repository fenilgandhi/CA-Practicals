{
    "Author": "Fenil Gandhi",
    "Version": "Python 3.6.2",
    "Description": "Implementation of making a change problem using dynamic programming",
    "Input Parameters": ["List of coins", "Total Change"],
    "Input": [5, 10, 20, 30],
    "Output": "Mininum Steps to multiply [5, 10, 20, 30] will be 4000 steps",
}


def Making_Change_Problem(total_change, coins):
    ways = [[] for i in range(total_change+1)]
    for coin in coins:
        ways[coin] += [ [coin] ]
        for i in range(coin+1, total_change + 1):
            ways[i] += [ m + [coin] for m in ways[i-coin] ]
    return ways[total_change]


if __name__ == '__main__':
    coins = [1, 2, 5, 10]
    total_change = 20
    possible_ways = Making_Change_Problem(total_change, coins)
    print("There are {3} Possible Changes for Rs.{0} using {1} coins are \n{2}".format(total_change, coins, "\n".join(map(str, possible_ways)) , len(possible_ways)))
