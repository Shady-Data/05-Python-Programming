"""4. Unique Words
Write a program that opens a specified text file and then displays a list of all the unique
words found in the file.
Hint: Store each word as an element of a set
​"""

from pprint import pprint

def unique_words():
    # initialize the set variable
    unique = set()
    # open the file to be read
    read_file = open('state_capitals.txt', 'r')
    # iterate through each line in the file
    for line in read_file.readlines():
        # read and split each line into the set (replace calls are specific to file referenced)
        unique.update(line.rstrip('\n').replace(':', '').replace(',', '').replace("\'", "").split(' '))
    # close the file
    read_file.close()
    # Print the unique words
    pprint(unique)

unique_words()