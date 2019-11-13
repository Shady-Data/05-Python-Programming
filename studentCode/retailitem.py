# This program tests the retail item class by generating 3 object of the class
# and displaying the contained information

# import the class
import RetailItemClass as ri

def main():
    # Populate the given data into dictionary/list
    items = {
        'Jacket': {'desc': 'Jacket', 'units' : 12, 'price' : 59.95},
        'Designer Jeans': {'desc': 'Designer Jeans', 'units' : 40, 'price' : 34.95},
        'Shirt': {'desc': 'Shirt', 'units' : 20, 'price' : 24.95}
        }

    # Create and empty list to store the items
    retail = []
    # generate an object for each entry
    for key in items.keys():
        # add the object to the list
        retail.append(ri.RetailItem(items[key]['desc'], items[key]['units'], items[key]['price']))

    # iterate through the list
    for retail_item in retail:
        # display the details
        print('\nDescription:', retail_item.get_description())
        print('\tUnits in Inventory:', retail_item.get_unitsInInventory())
        print('\tPrice: ${}'.format(retail_item.get_price(), ',.2f'))

# call the main function
main()