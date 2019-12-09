# lambda function
# Temporary one liner anonymous functions
square = lambda x : x**2
# print(square(6))
# print(square(7))


sum = lambda x, y, z : x + y + z
# print(sum(5, 10, 15))

# map() function
# calls the specified function and applies it to each item of an iterable

# def square(x):
#     return x*x

numbers = [1, 2, 3, 4, 5]
sqrList = map(square, numbers)
# print(next(sqrList))
# print(next(sqrList))
# print(next(sqrList))
# print(next(sqrList))
# print(next(sqrList))
# print(next(sqrList))

tens = [10, 20, 30, 40, 50]
indx = [1, 2, 3, 4, 5]
# pow() is a python builtin function
powers = list(map(pow, tens, reversed(indx)))
print(powers)