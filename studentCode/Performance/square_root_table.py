'''
4. 
    (The sqrt function) Write a program that prints the following table
    using your knowledge of loops and the sqrt function in the math module.
    Make sure your table is neat by using print formatting methods we've learned. 
​
        Number  Square Root
        0       0.0000
        1       1.0000
        2       1.4142
        ...
        18      4.2426
        20      4.4721
'''

# import the square root function from the math module
from math import sqrt

def main():
    # Create a list of numbers to iterate through for the table
    numbers = [x for x in range(21)]
    # Create a list of square roots for each number in the numbers list
    square_roots = [sqrt(x) for x in numbers]
    # print the table headers
    print('------------------------')
    print('| Number | Square Root |')
    print('------------------------')
    # iterate through both the numbers and square roots at the same time
    for num, root in zip(numbers, square_roots):
        # print the number and the cooresponding square root
        print(f'|{num:^8}|{root:^13.4f}|')
    # print the last line of the table
    print('------------------------')

# call the main function
main()