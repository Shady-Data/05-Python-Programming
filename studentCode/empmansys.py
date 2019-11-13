'''
6. Employee Management System
    This exercise assumes that you have created the Employee class for Programming Exercise 4.
    Create a program that stores Employee objects in a dictionary. Use the employee ID number
    as the key. The program should present a menu that lets the user perform the following actions:
        • Look up an employee in the dictionary
        • Add a new employee to the dictionary
        • Change an existing employee’s name, department, and job title in the dictionary
        • Delete an employee from the dictionary
        • Quit the program
    When the program ends, it should pickle the dictionary and save it to a file. Each time the
    program starts, it should try to load the pickled dictionary from the file. If the file does not
    exist, the program should start with an empty dictionary.
'''

# import the employee class and pickle modules
import EmployeeClass
import pickle

# attempt to load the database
try:
    with open('Employee_database.dat', 'rb') as infile:
        database = pickle.load(infile)
except IOError as e:
    print(e)
    print('Starting new database.')
    database = {}

def main():
    # Generate a menu
    menu = {
        1 : {'desc': 'Look up an employee record', 'func': search_employee},
        2 : {'desc': 'Add new employee(s)', 'func': add_employee},
        3 : {'desc': 'Change an employee record', 'func': search_employee},
        4 : {'desc': 'Delete an employee record', 'func': remove_employee},
        5 : {'desc': 'Exit Program', 'func': terminate}
    }
    # set a variable for menu selection and set it to a defualt value
    menu_select = 0
    # run the menu until exit Program is selected
    while menu_select != 5:
    # continue displaying the menu and prompting for selection until a valid entry is passed
        # display the menu
        print('\n\tMain Menu')
        for entry in menu.keys():
            print('{}: {}'.format(entry, menu[entry]['desc']))
        # get the menu selection
        menu_select = get_menu_selection()
        # if the selection is modify
        if  menu_select == 3:
            # set search modify to True
            menu[menu_select]['func'](p_modify=True)
        elif menu_select in menu.keys():
            # call the menu function
            menu[menu_select]['func']()

# define the get menu selection function
def get_menu_selection():
    try:
        user_input = int(input('\n\tMenu Choice: '))
    except ValueError:
        print('\t\tInvalid input: Choice must be a number.')
        user_input = 0
    return user_input

# define search employee
def search_employee(p_modify=False):
    # generate a menu for how to search for employee
    search_type = {
        1 : {'desc' : 'search for employee by name', 'func': search_by_name},
        2 : {'desc' : 'search for employee by ID', 'func': search_by_id},
        3 : {'desc' : 'Back to main menu'}
    }
    # set a variable for menu selection and set it to a defualt value
    search_select = 0
    # run the menu until exit Program is selected
    while search_select != 3:
        # display the menu
        print('\tSearch Menu')
        for entry in search_type.keys():
            print('{}: {}'.format(entry, search_type[entry]['desc']))
        # get the menu selection
        search_select = get_menu_selection()
        # do no call a menu function if search select == 3
        if search_select != 3 and search_select in search_type.keys():
            # call the menu function
            search_type[search_select]['func'](p_modify)
    
# define the search by employee name
def search_by_name(p_modify):
    # Prompt for the employee name
    search = input('\nEnter the name of the employee record you wish to view: ').title()
    # search through the database
    for employee in database.values():
        if employee.get_name() == search:
            display_info(employee, p_modify)
            break
    print('Returning to the Search Menu')

# define the search by employee id
def search_by_id(p_modify):
    # Prompt for the employee id
    try:
        search = int(input('\nEnter the id of the employee whose record you wish to view: '))
        # search through the database
        if search in database.keys():
            display_info(database[search], p_modify)
        else:
            print(f'\nSearch Complete, but no employee found matching ID#: {search}.')
    except ValueError:
        print('Input failed to convert input to integer')
    print('Returning to the Main Menu')

# define the display infor function
def display_info(p_employee, p_modify):
    # Display the employee information
    print('\nEmployee ID:', p_employee.get_id_num())
    print('\tName:', p_employee.get_name())
    print('\tTitle:', p_employee.get_title())
    print('\tDepartment:', p_employee.get_department())
    if p_modify == True:
        modify_employee(p_employee)

# define the modify employee function
def modify_employee(p_employee):
    # Generate a menu to determine what to modify
    modify = {
        1 : {'desc' : 'Modify Name', 'func': p_employee.set_name, 'get' : p_employee.get_name},
        2 : {'desc' : 'Modify Department', 'func': p_employee.set_department, 'get' : p_employee.get_department},
        3 : {'desc' : 'Modify Title', 'func': p_employee.set_title, 'get' : p_employee.get_title},
        4 : {'desc' : 'Modify Employee ID#', 'func': p_employee.set_id_num, 'get' : p_employee.get_id_num},
        5 : {'desc' : 'Return to Search Menu'}
    }
    # set a variable for menu selection and set it to a default value
    modify_select = 0
    # run the menu until exit Program is selected
    print()
    while modify_select != 5:
        # display the employee info
        display_info(p_employee, False)
        # display the menu
        print('\tModify menu')
        for entry in modify.keys():
            print('{}: {}'.format(entry, modify[entry]['desc']))
        # get the menu selection
        modify_select = get_menu_selection()
        # do no call a menu function if search select == 5
        if modify_select != 5 and modify_select != 4 and modify_select in modify.keys():
            # Prompt for the replacement entry
            replace = input('\nReplace {} with :'.format(modify[modify_select]['get']())).title()
            # get confirmation
            confirm = input('\nConfirm replacing {} with {} (y/n): '.format(modify[modify_select]['get'](), replace))
            # if confirmation == yes
            if confirm == 'y' or confirm =='yes':
                # call the menu function
                modify[modify_select]['func'](replace)
        # if changing employee's ID
        elif modify_select == 4:
            try:
                replace = int(input('\nReplace {} with : '.format(modify[modify_select]['get']())))
                # get confirmation
                confirm = input('\nConfirm replacing {} with {} (y/n): '.format(modify[modify_select]['get'](), replace))
                # if confirmation == yes
                if confirm == 'y' or confirm =='yes':
                    # remove the old employee from the database
                    database.pop(p_employee.get_id_num())
                    # call the menu function
                    modify[modify_select]['func'](replace)
                    # add the employee back to the database with the new ID number
                    database[p_employee.get_id_num()] = p_employee
            except ValueError:
                print('Error')

# define the add employee function
def add_employee():
    # prompt for how many employees to add
    try:
        amount = int(input('\nHow many new employees do you wish to add? '))
    except ValueError:
        print('Input error: falied to convert input to integer')
        print('defaulting to amount to 1')
        amount = 1
    # Prompt user for input for each employee
    for count in range(amount):
        print(f'\nAdd Employee {count + 1}:')
        try:
            id_num = int(input('Enter the Employee\'s ID#: '))
            # check if the number is already in use
            while id_num in database.keys():
                # prompt for a new number if it is
                id_num = int(input('\tID# already in use!\nEnter a valid Employee ID#: '))
            name = input('\tNew Employee\'s Name: ').title()
            depart = input('\tDepartment?: ').title()
            title = input('\tTitle?: ').title()
            # create the employee record from the information entered
            employee = EmployeeClass.Employee(name, id_num, depart, title)
            # add the employee record to the database using the employee id as the key
            database[id_num] = employee
        # if value error occurs when prompting for new employee information
        except ValueError as e:
            # display and error message and return to the main menu
            print(f'\nAn error occured when adding a new employee.\n{e}\nReturning to the main menu.')

def remove_employee():
    # prompt for the employee ID num to remove
    try:
        id_num = int(input('Enter the Employee ID# you wish to remove: '))
        # if the id is in the database keys
        if id_num in database.keys():
            # display the employee's record
            display_info(database[id_num], False)
            # prompt for confirmation
            confirm = input('Remove Employee (y/n)?: ')
            # if yes
            if confirm == 'y' or confirm =='yes':
                # remove the employee
                database.pop(id_num)
                # display record removed message
                print('Employee record has been removed')
    except ValueError:
        print('Invalid input: Returning to the main menu')

# define the terminate function
def terminate():
    print('\nTerminating session...')
    print('Saving current database...')
    # pickle and save the database
    with open('Employee_database.dat', 'wb') as outfile:
        pickle.dump(database, outfile)

    print('Database Saved!')
    print('Exiting program!')

# Call the main function
main()