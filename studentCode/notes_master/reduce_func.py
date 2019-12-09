# reduce()
# Recieves 2 arguments, function and iterable
# returns a single value
# good fo rolling computation to sequential pairs of value
# in a list

# reduce comes from the functools module
import functools

# define our function
def mult(x, y):
    print("x = ", x, "y = ", y)
    return(x*y)

# apply reduce to our function
fact = functools.reduce(mult, range(1,4))
print('Factortial of 3 is', fact)

product = 1
mylist = [1,2,3,4]
# for num in mylist:
#     product = product * num
# print(product)

# using reduce
from functools import reduce
product = reduce((lambda x, y: x*y), mylist)
print(product)