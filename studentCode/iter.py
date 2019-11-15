# Python iterators

# myList = [1,2,3,4]
# for item in myList:
#     print(item)

def traverse(iterable):
    it = iter(iterable)
    while True:
        try:
            item = next(it)
            print(item)
        except StopIteration:
            break

L1 = [1,2,3]
it = iter(L1)
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

print(next(it))
print(next(it))
print(next(it))
# print(next(it))

# iter(100)