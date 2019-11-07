"""
8. Name and Email Addresses
Write a program that keeps names and email addresses in a dictionary as key-value pairs.
The program should display a menu that lets the user look up a person’s email address, add
a new name and email address, change an existing email address, and delete an existing
name and email address. The program should pickle the dictionary and save it to a file
when the user exits the program. Each time the program starts, it should retrieve the dictionary from the file and unpickle it.​
"""

import pickle

def main():
    global database
    # try to open the datastore
    try:
        with open('datastore.dat', 'rb') as in_file:
            database = pickle.load(in_file)
    except IOError:
        # if file is missing or does not exist, display the error and start a new database
        print('File has been moved or corrupted.\nInitializing new database:\n')
        database = {}
    
    # Populate a menu for operations
    menu = {
        1 : {'description' : 'Search for an email by a name', 'function' : find_email},
        2 : {'description' : 'Add a new Name and email address', 'function' : add_email},
        3 : {'description' : 'Modify an existing email address', 'function' : modify_email},
        4 : {'description' : 'Remove an entry from the database', 'function' : delete_database_entry},
        5 : {'description' : 'Finish/Quit'}
    }
    # set a flag to continue gathering input for database operations
    menu_select = 0
    # Continuously accept input until user finishes
    while menu_select != 5:
        # add a blank line before the menu print
        print()
        # Display the menu
        for key in menu.keys():
            print(' {} : {}'.format(key, menu[key]['description']))
        # get the user input for their menu option
        menu_select = get_menu_entry()
        # Prompt again until a valid input within the menu keys is entered
        while menu_select not in menu.keys():
            print('Invalid selection')
            menu_select = get_menu_entry()
        # skip function call if menu entry is the same as while loop exit
        if menu_select != 5:
            # call the menu's function
            menu[menu_select]['function']()

    # open the file to write the database to
    with open('datastore.dat', 'wb') as out_file:
        pickle.dump(database, out_file)


def get_menu_entry():
    # Prompt user for menu choice and convert it to an int
    try:
        user_input = int(input('\nEnter the number of the menu option: '))
    except ValueError:
        print('Invalid entry: keyboard input failed to convert to integer')
        # set user_input to 0 for main loop to re-prompt
        user_input = 0
    # return the user_input
    return user_input

def find_email():
    # Prompt user for a name, checks if the name is in the database, and prints the email if the key exists
    search = input('Enter the name of the person whose email you wish to find: ').title()
    # check if the name is in the database keys
    if search in database.keys():
        # print the person's email
        print(f'\n{search}\'s email:\t{database[search]}')
    else:
        # display no user found in keys
        print(f'\n{search} could not be found.')

def add_email():
    # Prompt user for a name and email and add them to the database
    add_name = input('Enter the name to be added: ').title()
    # verify that the name is not in the database keys, otherwise prompt for name again with a unique identifier
    while add_name in database.keys() and add_name != '':
        add_name = input('Name already exists in the database!\nPlease try again or press enter to exit: ').title()
    # if add_name is blank, do nothing otherwise
    if add_name != '':
        # Prompt for the email address to be added
        database[add_name] = input(f'Enter {add_name}\'s email address: ')
    
def modify_email():
    # Prompt user for a name, checks if the name is in the database, and modifies the email if the key exists
    search = input('Enter the name of the person whose email you wish to modify: ').title()
    # check if the name is in the database keys
    if search in database.keys():
        # Prompt for the new email address
        database[search] = input(f'Enter the new email address for {search}: ')
    else:
        # display no user found in keys
        print(f'\n{search} could not be found.')

def delete_database_entry():
    # Prompt user for a name, checks if the name is in the database, and deletes the entry if the key exists
    search = input('Enter the name of the person whose email you wish to delete: ').title()
    # check if the name is in the database keys
    if search in database.keys():
        # Prompt the user if they really want to delete the entry
        confirmation = input(f'Do you really wish to delete the entry {search}: {database[search]} from the database? (y/n): ')
        # if confirmed yes
        if confirmation.lower() == 'y' or confirmation.lower() == 'yes':
            # delete the entry
            del database[search]

# Call the main function
main()