'''
7. Recursive Power Method
    Design a function that uses recursion to raise a number to a power. The function should
    accept two arguments: the number to be raised and the exponent. Assume that the exponent is a 
    nonnegative integer.
'''

def main():
    # get the number and power the number should be raised to
    num = int(input('Enter the base number: '))
    power = int(input('Enter the power to raise the first number to: '))

    # print the return of the recursive_power function with num and power as arguments
    print(recursive_power(num, power))
    # Debug print the num**power
    # print(num ** power)

def recursive_power(p_num, p_power):
    # base case: p_power == 1 return p_num
    if p_power == 1:
        return p_num
    else:
        # recursive case: return p_num * recursive_power(p_num, p_power - 1)
        return p_num * recursive_power(p_num, p_power - 1)

# Call the main function
main()