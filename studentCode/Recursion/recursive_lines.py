'''
3. Recursive Lines
    Write a recursive function that accepts an integer argument, n. The function should display
    n lines of asterisks on the screen, with the first line showing 1 asterisk, the second line
    showing 2 asterisks, up to the nth line which shows n asterisks.
'''

def main():
    # Get an intger for the number of lines to print
    num_lines = int(input('Enter the number of lines to print: '))

    # call the recursive_lines function with the start of 1 and end of num_lines
    recursive_lines('*', num_lines)

# define the recursive_lines function
# parameters: str pat, int num_lines 
def recursive_lines(p_pat, p_stop):
    # base case if len(p_pat) == p_stop
    if len(p_pat) == p_stop:
        print(p_pat)
    else:
    # print the pattern and return recursive lines p_pat + '*', p_stop
        print(p_pat)
        return recursive_lines(p_pat + '*', p_stop)

# Call the main function
main()