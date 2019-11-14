'''
7. Cash Register
    This exercise assumes that you have created the RetailItem class for Programming
    Exercise 5. Create a CashRegister class that can be used with the RetailItem class. The
    CashRegister class should be able to internally keep a list of RetailItem objects. The
    class should have the following methods:
        • A method named purchase_item that accepts a RetailItem object as an argument.
        Each time the purchase_item method is called, the RetailItem object that is passed as
        an argument should be added to the list.
        • A method named get_total that returns the total price of all the RetailItem objects
        stored in the CashRegister object’s internal list.
        • A method named show_items that displays data about the RetailItem objects stored
        in the CashRegister object’s internal list.
        • A method named clear that should clear the CashRegister object’s internal list.
    Demonstrate the CashRegister class in a program that allows the user to select several
    items for purchase. When the user is ready to check out, the program should display a list
    of all the items he or she has selected for purchase, as well as the total price.
'''
# import the retail items class
import RetailItemClass

class CashRegister:
    # define the __init__()
    def __init__(self):
        self.__retail_items = []

    # define setters
    def purchase_item(self, p_retailItem):
        self.__retail_items.append(p_retailItem)

    def clear(self):
        self.__retail_items = []

    # define getters
    def get_total(self):
        # initialize a total accumalator
        total = 0.0
        # iterate though each retail item in the list
        for item in self.__retail_items:
            # add the price to the total accumalator
            total += item.get_price()
        # return the total
        return total
    
    def show_items(self):
        # iterate through the retail items
        for ind, item in enumerate(self.__retail_items):
            # display the description and price
            print(f'Item {ind + 1}:')
            print('\tDescription: ', item.get_description())
            print(f'\tPrice: ${item.get_price():,.2f}')

