"""
6. File Analysis
Write a program that reads the contents of two text files and compares them in the following ways:
• It should display a list of all the unique words contained in both files.
• It should display a list of the words that appear in both files.
• It should display a list of the words that appear in the first file but not the second.
• It should display a list of the words that appear in the second file but not the first.
• It should display a list of the words that appear in either the first or second file but not both.
Hint: Use set operations to perform these analyses.
"""

from pprint import pprint

def file_analysis():
    # create empty variables to store the information too
    file_1_unique = set()
    file_2_unique = set()
    # open the first file to be read
    with open('plain_text.txt', 'r') as file_1:
        # iterate through the lines of the file
        for line in file_1.readlines():
            # strip the new line, split the line by ' ', and add the resulting list to the file_1_unique set
            file_1_unique.update(line.rstrip().replace(',', '').replace('.', '').replace('\'', '').replace('!', '').replace('?', '').split(' '))
    # open the second file to be read
    with open('d_plain_text.txt', 'r') as file_2:
        # iterate through the lines of the file
        for line in file_2.readlines():
            # strip the new line, split the line by ' ', and add the resulting list to the file_2_unique set
            file_2_unique.update(line.rstrip().replace(',', '').replace('.', '').replace('\'', '').replace('!', '').replace('?', '').split(' '))

    # Populate a new set that contains all of the unique elements in both sets
    all_unique_elements = file_1_unique | file_2_unique
    # Populate a new set with the with the contents that are commone in both files unique sets
    common_elements = file_1_unique & file_2_unique
    # Populate a new set with contents that are only in file 1's set
    file_1_only_elements = file_1_unique - file_2_unique
    # Populate a new set with contents that are only in file 1's set
    file_2_only_elements = file_2_unique - file_1_unique
    # Populate a new set with all of the unique elements that are in 1 or the other set, but not contained in both sets
    combined_differences = file_1_only_elements | file_2_only_elements

    # Display the results
    print('All unique words in both files: ')
    pprint(all_unique_elements)
    print('\nUnique words common to both files: ')
    pprint(common_elements)
    print('\nUnique words only in the first file: ')
    pprint(file_1_only_elements)
    print('\nUnique words only in the second file: ')
    pprint(file_2_only_elements)
    print('\nUnique words that are in either file, but not in both files: ')
    pprint(combined_differences)

file_analysis()