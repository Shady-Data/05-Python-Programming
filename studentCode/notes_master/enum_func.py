# enumerate()
# Enumerate iterates over different types of iterable objects and returns both the index and also the value of each item.

# enumerate over some names
names = ['Daniel', 'Joe', 'Jim', 'Travis']
# print(list(enumerate(names)))
# print(list(enumerate(names, start=4)))

# for name in enumerate(names):
#     print(name)

# for count, item in enumerate(names):
#     print(f'Count: {count}, Item {item}')

# for count, item in enumerate(names, 100):
#     print(f'Count: {count}, Item {item}')

# my_string = 'Enumerating is Powerful'
# for idx, ch in enumerate(my_string):
#     print(f'Index if {idx} and character is {ch}')

# dictionary comprehension with enumerate()
my_dict = {k : v for k, v in enumerate(names)}
print(my_dict)
