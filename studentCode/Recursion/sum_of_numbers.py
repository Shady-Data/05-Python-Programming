'''
6. Sum of Numbers
    Design a function that accepts an integer argument and returns the sum of all the integers from 1 up 
    to the number passed as an argument. For example, if 50 is passed as an argument, the function will 
    return the sum of 1, 2, 3, 4, . . . 50. Use recursion to calculate the sum.
'''

def main():
    # get the stop number
    stop_num = int(input('Enter the number to stop at: '))

    # print the return of the sum_of_nums function with stop_num as an argument
    print(sum_of_nums(stop_num))
    # Debug check print sum of ints in range + 1
    # print(sum([x for x in range(stop_num + 1)]))

# Define sum_of_nums() function
# parameters: p_stop
def sum_of_nums(p_stop):
    # base case:
    if p_stop == 0:
        return 0
    # recursive case:
    else:
        return p_stop + sum_of_nums(p_stop - 1)

# Call the main function
main()