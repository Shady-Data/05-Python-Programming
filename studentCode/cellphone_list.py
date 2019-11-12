# This program creates 5 CellPhone objects and stores them in a list

import CellPhone as cell

def main():
    # Get a list of CellPhones
    phones = make_list(5)

    # Display the data in the list
    print('\nHere is the data that you entered:')
    display_list(phones)


def make_list(p_amount):
    # get p_amount phones and adds it to a list
    # Create an empty list
    phone_list = []
    # get p_amount phones
    for count in range(1, p_amount + 1):
        # get the data for each phones
        print(f'\nPhone Number {count}:')
        man = input('Enter the Manufacturer: ')
        mod = input('Enter the Model Number: ')
        retail = float(input('Enter the retail price: '))

        # create an instance of the CellPhone class
        phone = cell.CellPhone(man, mod, retail)
        # add the phone instance to the list
        phone_list.append(phone)

    # return the phone list
    return phone_list

def display_list(p_list):
    # display all phones from the list
    for ind, phone in enumerate(p_list):
        print(f'\nPhone Entry {ind + 1}:')
        print('Manufacturer:', phone.get_manufact())
        print('Model Number:', phone.get_model())
        print(f'Retail Price: ${phone.get_retail_price():,.2f}')

# call the main function
main()