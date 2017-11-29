{
    "Author": "Fenil Gandhi",
    "Version": "Python 3.6.2",
    "Description":
        '''Write a program that implements change making solution. Assume that the cashier has currency notes in the denominations Rs. 100, Rs. 50, Rs. 20, Rs. 10, Rs. 5 and Rs. 1 in addition to coins .Program should include a method to input the purchase amount and the amount given by the customer as well as method to output the amount of change and a breakdown by denomination.Apply greedy algorithm at the cahier side that is give less number of coins if sufficient currency of that denomination available.''',
    "coins" :  [1, 5, 10, 20, 50, 100],
    "Input" : "(coins, purchase amount, paid amount)",
    "Output" : "(Change breakdown)",
}


def Making_Change_Greedy(total_coins, amount):
    quantity = {}
    for coin in sorted(total_coins, reverse=True):
    	if amount < coin: 
    		quantity[coin] = 0
    	quantity[coin] = amount // coin
    	amount = amount % coin
    
    print(["Rs.{0}\t{1} coins\n".format(c,v) for c,v in quantity.items()])


if __name__ == '__main__':
    coins = [1, 2, 5, 10]
    purchase_amount = int(input("Purchase Amount : "))
    paid_amount = int(input("Paid Amount : "))
    Making_Change_Greedy( coins, paid_amount - purchase_amount )