# filter()
# Takes in two arguments, function and an iterable
# Only returns items in the list that are True

def isPrime(x):
    for n in range(2, x):
        if x % n == 0:
            return False
    return True

filterObject = filter(isPrime, range(10))
print('Prime numbers between 1-10: ', list(filterObject))

# filter applied with lambda

filterObject2 = filter(lambda x: x % 2 == 0, range(10))
print(list(filterObject2))

# filter on a random list
randomlist = [1, 'a', 0, False, True, '0']
filteredList = filter(None, randomlist)
print('The filtered elements are ')
for element in filteredList:
    print(element)