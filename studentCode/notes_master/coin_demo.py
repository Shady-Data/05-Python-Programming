import coin

def main():
    # Create an object from the Coin class
    my_coin = coin.Coin()
    # print(type(my_coin))

    my_coin.sideup = 'Tails'

    # display the side of the coin
    # print('Side up is', my_coin.get_sideup())
    print(my_coin)

    # toss the coin
    print("Tossing the coin....")
    my_coin.toss()

    # get the side of the coin again
    # print('Side up is', my_coin.get_sideup())
    print(my_coin)

    print(my_coin.sideup)

main()