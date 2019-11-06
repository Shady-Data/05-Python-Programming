'''3. File Encryption and Decryption
Write a program that uses a dictionary to assign “codes” to each letter of the alphabet. For
example:
codes = { 'A' : '%', 'a' : '9', 'B' : '@', 'b' : '#', etc...}
Using this example, the letter A would be assigned the symbol %, the letter a would be
assigned the number 9, the letter B would be assigned the symbol @, and so forth.
The program should open a specified text file, read its contents, and then use the dictionary to 
write an encrypted version of the file’s contents to a second file. Each character in
the second file should contain the code for the corresponding character in the first file.'''

import string
from random import randint

def file_encryption():
    # Populate a list of all ascii alphanumeric chars
    ascii_printable = []
    for char in string.printable:
        if char.isalnum():
            ascii_printable.append(char)
    
    # create an empty set to store unique rng elements
    encrypt_set = set()
    # continuously add random unicode elements until len(set) == len(acsii printable chars)
    while len(encrypt_set) < len(ascii_printable):
        encrypt_set.add(random_char())
    
    # Populate a dictionary with the ascii printable keys with encrypt_set values
    cypher_dict = {}
    for ind, char in enumerate(encrypt_set):
        cypher_dict[ascii_printable[ind]] = char

    # Store the key in a string // creates an order for decryption later
    encrypt_key_string = ''
    for char in ascii_printable:
        encrypt_key_string += cypher_dict[char]

    # ingest the file to encrypt
    plain_text_list = []
    with open('plain_text.txt', 'r') as in_file:
        for line in in_file.readlines():
            plain_text_list.append(line.rstrip('\n'))

    # encrypt each line in the file
    cypher_text_list = []
    for plain_line in plain_text_list:
        encrypt_line = ''
        for char in plain_line:
            # encrypt the char if the char exists in keys
            if char in cypher_dict.keys():
                encrypt_line += cypher_dict[char]
            else:
                # just add the char if not in the keys
                encrypt_line += char
        cypher_text_list.append(encrypt_line)
    
    # insert the encryption key string randomlin into the list of encrypted lines
    cypher_text_list.insert(randint(0, len(cypher_text_list) - 1), encrypt_key_string)

    # Write to the encrypted lines to a new file
    with open('cypher_text.txt', 'w') as out_file:
        for line in cypher_text_list:
            out_file.write(line + '\n')


def random_char():
    # Gets a random int in the unicode range
    rand = randint(0, 10000)
    while chr(rand) not in string.printable or chr(rand) in string.whitespace or chr(rand) in '.?!,\'\";:':
        rand = randint(0, 10000)
    return chr(rand)

def file_decryption():
    # read the contents of the file to be decrypted
    cypher_text = []
    with open('cypher_text.txt', 'r') as in_file:
        for line in in_file.readlines():
            cypher_text.append(line.strip())

    # generate a list of all ascii alphanumeric chars
    ascii_printable = []
    for char in string.printable:
        if char.isalnum():
            ascii_printable.append(char)
    ascii_printable = ''.join(ascii_printable)
    
    # iterate through the lines to find a len(line) == len(ascii_printable) and len(set(linechars)) == len(ascii_printable)
    # this will find our randomly generated encryption key for the file
    for index, cypher_line in enumerate(cypher_text):
        if len(cypher_line) == len(ascii_printable):
            unique_line_char = set()
            for char in cypher_line:
                unique_line_char.add(char)
            if len(unique_line_char) == len(ascii_printable):
                encryption_key = cypher_line
                del cypher_text[index]

    # gernerated the dictionary for decryption
    plain_dict = {}
    for ind, char in enumerate(encryption_key):
        plain_dict[char] = ascii_printable[ind]

    # iterate through the cypher text's lines to decrypt them
    plain_text = []
    for cypher_line in cypher_text:
        plain_line = ''
        for char in cypher_line:
            # add the decrypted char if char is in keys
            if char in plain_dict.keys():
                plain_line += plain_dict[char]
            else:
                # add the char if the char is not in keys
                plain_line += char
        plain_text.append(plain_line)
    
    # open a file to write to and write the plain_text lines to the file
    with open('d_plain_text.txt', 'w') as out_file:
        for line in plain_text:
            out_file.write(line + '\n')

file_encryption()
# file_decryption()