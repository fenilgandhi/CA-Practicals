"""	
Implementation of making a change problem using dynamic programming
"""


def Making_Change_Problem(total_change, coins):

    ways = [1] + [0] * total_change

    for coin in coins:
        for i in range(coin, total_change + 1):
            ways[i] += ways[i - coin]

    return ways[total_change]


if __name__ == '__main__':
    coins = [1, 2, 5, 10]
    total_change = 100
    possible_ways = Making_Change_Problem(total_change, coins)
    print( "Possible Changes for {0} using {1} coins are {2}".format(total_change, coins, possible_ways) )
