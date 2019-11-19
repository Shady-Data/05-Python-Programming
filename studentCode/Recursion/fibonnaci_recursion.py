# This program uses recursion to print numbers
# from the Fibonnaci series

def main():
    print('The first 10 numbers in the')
    print('Fibonnaci Series are:')

    for number in range(0, 10):
        print(fibonnaci(number))

def fibonnaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)

# print(fibonnaci(3))

# Call the main function
main()