# This program uses recursion to find the GCD (Greatest Common Divisor)
# of the two numbers

# if x can be evenly divided by y, then gcd(x, y) = y
# otherwise, gcd(x, y) = gcd(y, remainder of x/y)

def main():
    # Get two numbers
    num1 = int(input('Enter an integer: '))
    num2 = int(input('Enter another integer: '))

    # Display the GCD
    print('The greatest common divisor of')
    print('the two numbers is', gcd(num1, num2))

# The gcd function returns the greatest common divisor
# of two numbers

def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)

# Call the main function
main()