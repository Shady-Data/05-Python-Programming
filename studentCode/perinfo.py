# This program tests the personal information class by creating 3 objects
# and display their information

# import the personal information class
import PIClass

def main():
    # build the list personal information
    pi_list = get_list(3)
    # display the information
    display_list(pi_list)

# define the get list function
def get_list(p_amount):
    # create an empty list
    result_list = []
    # Prompt for information p_amount times
    for count in range(1, p_amount + 1):
        print(f'\nPerson {count}:')
        name = input('Enter the individual\'s name: ').title()
        address = input(f'Enter {name}\'s address: ')
        age = int(input(f'How old is {name}? '))
        phone = input(f'Enter {name}\'s phone number: ')

        # creat the personal information object with the information
        perinfo = PIClass.PersonalInformation(name, address, age, phone)
        # add the object to the list being returned
        result_list.append(perinfo)

    # return the resulting list
    return result_list

def display_list(p_list):
    # iterate through the list
    for index, perinfo in enumerate(p_list):
        # print the person's personal information
        print(f'\nEntry {index + 1}:')
        print(f'Name: {perinfo.get_name()}')
        print(f'Address: {perinfo.get_address()}')
        print(f'Age: {perinfo.get_age()}')
        print(f'Phone #: {perinfo.get_phone()}')

# Call the main function
main()