'''
 7. (Largest rows and columns) Write a program that randomly fills in 0s and 1s into
a matrix, prints the matrix, and finds the rows and columns with the most
1s. Here is a sample run of the program:
0011
0011
1101
1010
The largest row index: 2
The largest column index: 2, 3
​'''

def largest_rows_columns():
    # building the matrix
    # initialize the list for the matrix to work in
    matrix = []
    # grab a random integer between 2 and 10, inclusive, to determine the size of the matrix
    SIZE = randint(2,10)
    # iterate through a range up to the rng size variable
    for build_row in range(SIZE):
        # set an empty string to begin building the binary pattern
        m_row = []
        # iterate through a range of the matrix size constant to build the columns entry
        for build_columns in range(SIZE):
            # append a random integer (0, 1) to the row pattern
            m_row.append(randint(0, 1))
        # append the built row to the matrix
        matrix.append(m_row)
    
    # for better formatting add a blank print statement
    print('')
    # Iterate through each row to print the matrix
    for print_row in matrix:
        # Initialize a variable to represent the matrix in string format
        row_str_rep = ''
        # iterate for each element in the row
        for print_char in print_row:
            # add the string value of the element to the string
            row_str_rep += str(print_char)
        # display the rows, one row per line
        print(row_str_rep)

    # reading the matrix
    # initialize a new list to store the results of ones in each row
    calc_rows = []
    # initialize a new list/accumalator to store the results of ones in each column
    calc_columns = [0] * SIZE

    # iterate over each row in the matrix
    for row in matrix:
        # sum the row and append it to calc_rows list
        calc_rows.append(sum(row))
        # Iterate ovet each element in the row to get the column count
        for index in range(len(row)):
            # if element in index == 1 ; do nothing if element != 1
            if row[index] == 1:
                # increment the column counter
                calc_columns[index] += 1

    # assign the max of calcs rows to a variable
    highest_row = max(calc_rows)
    # Check if only one occurance of max value in row
    if calc_rows.count(highest_row) > 1:
        # initial a counter to keep track of removed indexes
        removed_count = 0
        # initialize a list to store multiple indexes
        max_rows = []
        # continuously pull and del indexes until the count of max value == 0
        while calc_rows.count(highest_row) > 0:
            # assign the first index of the max of calc_rows to a variable
            max_val_index = calc_rows.index(highest_row)
            # append the first max value index to the list + the counter of removed indexes
            max_rows.append(str(max_val_index + removed_count))
            # del the index of the first max value
            del(calc_rows[max_val_index])
            # increment counter of removed indexes
            removed_count += 1
        # convert the list to a string for printing
        string_rep_rows = ', '.join(max_rows)
        # print the rows with the greatest value
        print(f'\nlargest row indexes: {string_rep_rows}')
    # if only 1 instance
    else:
        # Display the largest row
        print(f'\nlargest row index: {calc_rows.index(highest_row)}')
    # assign the max of calcs columns to a variable
    highest_column = max(calc_columns)
    # check if only 1 occurance of max value in column
    if calc_columns.count(highest_column) > 1:
        # initial a counter to keep track of removed indexes
        removed_count = 0
        # initialize a list to store multiple indexes
        max_columns = []
        # continuously pull and del indexes until the count of max value == 0
        while calc_columns.count(highest_column) > 0:
            # assign the first index of the max of calc_rows to a variable
            max_val_index = calc_columns.index(highest_column)
            # append the first max value index to the list + the counter of removed indexes
            max_columns.append(str(max_val_index + removed_count))
            # del the index of the first max value
            del(calc_columns[max_val_index])
            # increment counter of removed indexes
            removed_count += 1
        # convert the list to a string for printing
        string_rep_columns = ', '.join(max_columns)
        # print the columns with the greatest value
        print(f'largest column indexes: {string_rep_columns}')
    # if only 1 instance
    else:
        # Display the largest column
        print(f'largest column index: {calc_columns.index(highest_column)}')

largest_rows_columns()