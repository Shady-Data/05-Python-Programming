'''
5. Word Frequency
Write a program that reads the contents of a text file. The program should create a dictionary in which the keys are the individual words found in the file and the values are the
number of times each word appears. For example, if the word “the” appears 128 times,
the dictionary would contain an element with 'the' as the key and 128 as the value.
The program should either display the frequency of each word or create a second file
containing a list of each word and its frequency
'''

def word_frequency():
    # initialze a blank dictionary to fill
    words = {}
    # open the file to read
    in_file = open('plain_text.txt', 'r')
    # iterate through each line in the file
    for line in in_file.readlines():
        # iterate each word in the line
        for word in line.replace(',', '').replace('.', '').replace('\'', '').replace('!', '').replace('?', '').split():
            # Check if the word is in the words dictionary keys
            if word in words.keys():
                # increment the value of the word by 1
                words[word] += 1
            else:
                # set the value 1 to the words[word] key
                words[word] = 1
    # close the file being read
    in_file.close()

    # open a file to write the count to
    out_file = open('plain_text_word_count.txt', 'w')
    # iterate through the dictionary
    for word, count in words.items():
        # write the word and the count to the file, one entry per line
        out_file.write(f'{word}: {count},\n')
    # close the file being written to
    out_file.close()

word_frequency()