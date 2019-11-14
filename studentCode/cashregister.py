'''
Demonstrate the CashRegister class in a program that allows the user to select several
items for purchase. When the user is ready to check out, the program should display a list
of all the items he or she has selected for purchase, as well as the total price.
'''

# import the cash register and retail item class modules
import CashRegisterClass
import RetailItemClass as ri
from random import randint

# generate a list of retail item to test with
items = {
    'Jacket': {'desc': 'Jacket', 'units' : 12, 'price' : 59.95},
    'Designer Jeans': {'desc': 'Designer Jeans', 'units' : 40, 'price' : 34.95},
    'Shirt': {'desc': 'Shirt', 'units' : 20, 'price' : 24.95}
    }
# Create and empty list to store the items
retail_items = []
# generate an object for each entry
for key in items.keys():
    # add the object to the list
    retail_items.append(ri.RetailItem(items[key]['desc'], items[key]['units'], items[key]['price']))

def main():
    # Instanstiate a Class Register object
    register = CashRegisterClass.CashRegister()

    # add an item to the cash register
    register.purchase_item(retail_items[randint(0, 2)])

    # display the items in the register
    # register.show_items()

    # add 5 more items to the register
    for x in range(5):
        register.purchase_item(retail_items[randint(0, 2)])

    print('Show items before clear:')
    # Display the details of the items purchased
    register.show_items()

    # display the total of the items
    print(f'\n\tTotal: ${register.get_total():,.2f}')

    # clear the register
    register.clear()

    print('\nShow Items after clear:')
    # display the items in the register
    register.show_items()


# call the main function
main()