'''
1. 
    (Remove text) Write a program that removes all the occurrences of a specified
    string from a text file named pointsOfAuthority.txt. Your program should prompt the user to enter 
    a filename and a string to be removed.
'''

import re

def main():
    # get the filename to be read from
    filename = input('What file needs to be cleaned: ')
    # open the file and read the contents into a list
    with open(filename, 'r') as in_file:
        contents = []
        for line in in_file.readlines():
            contents.append(line.rstrip())

    # close the file as necessary
    # get the str to be removed
    # compile the regex for the search
    remove_str = re.compile(input('Enter the string to be removed: '), re.I)
    # iterate through the file contents
    # for ind, line in enumerate(contents):
    for ind, line in enumerate(contents):
        contents[ind] = remove_str.sub('', line) + '\n'
        # enumerate through each word in the line
        # temp_line = line.split()
        # for word in temp_line:
            # remove the word is the search string is matched
            # if word.lower() == remove_str:
                # temp_line.remove(word)
        # return the temp_line to a string
        # temp_line = ' '.join(temp_line)
        # replace the lines in contents with the new line
        # contents[ind] = temp_line + '\n'
    # write a new file without the string with -clean added in
    with open(filename.split('.')[0] + '-cleaned.' + filename.split('.')[1], 'w') as out_file:
        out_file.writelines(contents)

    # close the file as necessary

# call the main function
main()