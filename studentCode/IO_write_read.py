# # This program writes three lines of data to a file
# def io_write():
#     '''
#     */WIP REPLACE THIS!!!/*docstring placeholder
#     '''
#     # open a file name philosophers.txt
#     f = open('C:\\Users\\student\\Documents\\Curriculum\\IDFCourseNotes\\Coursework\\philosophers.txt', 'w')

#     # write the named of the three philosophers
#     f.write('John Locke\n')
#     f.write('David Hume\n')
#     f.write('Edward Burke\n')

#     # close the file handle
#     f.close()

# # call the main function
# io_write()

# # This program reads the reads the philosophers.txt file
# def io_read():
#     # open the file name philosophers.txt
#     f = open('C:\\Users\\student\\Documents\\Curriculum\\IDFCourseNotes\\Coursework\\philosophers.txt', 'r')

#     # read the file's contents
#     f_contents = f.read()

#     # close the file
#     f.close()

#     # print the contents in memory
#     print (f_contents)

# # call the main function
# io_read()

# # This program reads the reads the philosophers.txt file
# def io_readline():
#     # open the file named philosophers.txt
#     f = open('C:\\Users\\student\\Documents\\Curriculum\\IDFCourseNotes\\Coursework\\philosophers.txt', 'r')

#     # read one line at a time
#     line1 = f.readline()
#     line2 = f.readline()
#     line3 = f.readline()

#     # Strip the newline from each string
#     line1 = line1.rstrip('\n')
#     line2 = line2.rstrip('\n')
#     line3 = line3.rstrip('\n')

#     # close the file
#     f.close()

#     # print the data that was read
#     print(line1)
#     print(line2)
#     print(line3)

# # call the main function
# io_readline()

# # writes to sales.txt
# def io_write_sales():
#     # open the file named sales.txt
#     f = open('C:\\Users\\student\\Documents\\Curriculum\\IDFCourseNotes\\Coursework\\sales.txt', 'w')

#     # write or append to the file
#     f.write('1000.0\n2000.0\n3000.0\n4000.0\n5000.0\n')

#     # close the file
#     f.close

# io_write_sales()

# # This Program prompts the user for sales amounts and writes those amounts to sales.txt
# def io_loop_write():
#     # Prompt user for the number days of sales to be entered
#     num_days = int(input('for how many days do you have sales? '))
#     # open sales2.txt
#     sales_file = open('C:\\Users\\student\\Documents\\Curriculum\\IDFCourseNotes\\Coursework\\sales2.txt', 'w')

#     # iterate for each day in range 1 to days + 1
#     for count in range(1, num_days + 1):
#         # Prompt user for the day's sales
#         sales = float(input("Enter the sales for the day # " + str(count) + ": "))
#         # Write the data to sales2.txt
#         sales_file.write(str(sales) + '\n')
#     # close the file
#     sales_file.close()
#     print ('Data written to sales2.txt')

# # call main
# io_loop_write()

# # This program reads the all of the values in sales2.txt
# def io_loop_read():
#     # open sales2.txt
#     sales_file = open('C:\\Users\\student\\Documents\\Curriculum\\IDFCourseNotes\\Coursework\\sales.txt', 'r')

#     # Read the first line of the file, but don't convert to a number yet
#     # We still need to check for an empty string
#     line = sales_file.readline()

#     # As long as an empty string is not returned from readline, continue processing
#     while line != '':
#         # convert line to a float
#         amount = float(line)
#         # format and display the data
#         print(f'${amount:.2f}')
#         # read the next line of data
#         line = sales_file.readline()
#     # close the file
#     sales_file.close()

# # call io_loop_read
# io_loop_read()


# # This program reads a user specified file
# def display_file():
#     #
#     filename = input('Enter the filename: ')
#     #
#     try:
#         # open sales2.txt
#         in_file = open(filename, 'r')

#         # Read the data in the file
#         contents = in_file.read()
#         #
#         print(contents)

#         in_file.close
#     except IOError:
#         print("An error occurred trying to read the file", filename)

# # call io_loop_read
# display_file()