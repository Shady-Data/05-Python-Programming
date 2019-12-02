'''
2.
    (Locate the largest element) Write the following function that returns the location
    of the largest element in a two-dimensional list:
    
    def locateLargest(a):
        The return value is a one-dimensional list that contains two elements. These
        two elements indicate the row and column indexes of the largest element in the
        two-dimensional list. Write a test program that prompts the user to enter a 
        two-dimensional list and displays the location of the largest element in the list. 
    
    Here is a sample run(You don't have to mimic this, this is just a guide):
​
        Enter the number of rows in the list: 3
        Enter a row: 23.5  35  2    10
        Enter a row: 4.5   3   45   3.5
        Enter a row: 35    44  5.5  11.6
        The location of the largest element is at (1,2)
'''

import string

def main():
    # intialize a blank list to store the lists in
    matrix = []
    # Get the user's input for the number of rows in the list
    num_rows = get_num_rows()
    # continually call num_rows until an integer greater than 0 is returned
    while num_rows <= 0:
        num_rows = get_num_rows()
    # iterate for each row
    for row in range(1, num_rows + 1):
        # Append row lists to the matrix until the number of rows has been obtained
        matrix.append(get_row(row))
    # Get the largest value in each row
    largest_in_row = [max(row) for row in matrix]
    # Get the index of the largest value in all rows
    row_index = largest_in_row.index(max(largest_in_row))
    # Get the index of the largest item in the row within the matrix
    col_index = matrix[row_index].index(max(largest_in_row))
    # print the location of the largest item
    print(f'The location of the largest element is at ({row_index},{col_index})')

def get_num_rows():
    # get user input for the number of rows and convert it to an integer
    try:
        num_rows = int(input('Enter the number of rows in the list: '))
    # if the conversion to integer fails, print an error message and set number of rows to -1
    except ValueError:
        print('Invalid input: the number of rows must be an integer greater than 0!')
        # S
        num_rows = -1
    return num_rows

def get_row(p_row):
    # initialze an empty list to store row values
    row = []
    # Populate an invalid character list
    invalid_list = [char for char in string.printable if char not in string.digits]
    # Set a variable to check for a stop condition to stop requesting input
    cont = True
    # contiually gather input until non-digit char is entered
    print(f'Enter row {p_row}: ')
    while cont == True:
        try:
            user_input = input('data: ')
            # check if user input contains a non-digit char
            if user_input in invalid_list or user_input == '':
                # set the cont flag to False to terminate the loop
                cont = False
            # check if the input is a float, exclude a '.' char
            elif '.' in user_input and len(user_input) > 1:
                # convert the user_input to a float and append the value to the row list
                row.append(float(user_input))
            else:
                # otherwise conver the user input to an integer and append it to the list
                row.append(int(user_input))
        except ValueError as e:
            print(e)
            print('Something went wrong\nExitting loop and returning current row contents')
            break
    # return the row list after the while loop exits
    return row

# call the main function
main()