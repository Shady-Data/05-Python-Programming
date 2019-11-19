'''
1. Recursive Printing
    Design a recursive function that accepts an integer argument, n, and prints the numbers 1
    up through n.
'''

def main():
    # Get an integer to print numbers up to
    stop_num = int(input('At what number do you want this program to stop at: '))
    # call the recursive print number and pass the stop number
    recursive_print(1, stop_num)

# define the recursive_print function the start parameter the stop parameter
def recursive_print(p_start, p_stop):
    # base case, print 1
    if p_start == p_stop:
        print(p_stop)
    # recursive case
    else:
        print(p_start)
        return recursive_print(p_start + 1, p_stop)

# call the main function
main()