# This program tests the CellPhone class

import CellPhone as cell

def main():
    # Get the phone data
    man = input('Enter the Manufacturer: ')
    mod = input('Enter the Model Number: ')
    retail = float(input('Enter the retail price: '))

    # create an instance of the CellPhone class
    phone = cell.CellPhone(man, mod, retail)

    # diplay the data that was entered
    print('Here is the data that you entered:')
    print('Manufacturer:', phone.get_manufact())
    print('Model Number:', phone.get_model())
    print(f'Retail Price: ${phone.get_retail_price():,.2f}')

# call the main function
main()