# zip() function
# This is a good way to take 2 different sequences of
# data and pair them together

# set up 2 lists
prices = [72.51, 9.27, 153.74, 30.23, 53.00]
names = ["CAT", 'GE', 'MSFT', 'AA', 'IBM']

# use for loop and zip() to pair lists together
for name, price in zip(names, prices):
    print(name, '=', price)
