'''
2. Recursive Multiplication
    Design a recursive function that accepts two arguments into the parameters x and y. The
    function should return the value of x times y. Remember, multiplication can be performed
    as repeated addition as follows:
    7 X 4 = 4 + 4 + 4 + 4 + 4 + 4 + 4
    (To keep the function simple, assume that x and y will always hold positive nonzero
    integers.)
'''

def main():
    # get the two number inputs to get a product for
    num1 = int(input('Enter an integer: '))
    num2 = int(input('Enter another integer: '))

    # display the result of the recursive multiply function with the 2 numbers as arguments
    print(recurs_multi(num1, num2))

# define the recurs_multi function
# parameters are an int number and int times
def recurs_multi(p_num, p_times):
    # base case return num
    if p_times == 1:
        return p_num
    # recursive case return num + recurs_multi(num, times - 1)
    else:
        return p_num + recurs_multi(p_num, p_times - 1)

# Call the main function
main()
