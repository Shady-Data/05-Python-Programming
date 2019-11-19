# function definition
def recursive_factorial(n):
    # base case
    if n == 0:
        return 1
    # recursive case
    else:
        return n * recursive_factorial(n - 1)

print(recursive_factorial(4))