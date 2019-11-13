'''
5. RetailItem Class
Write a class named RetailItem that holds data about an item in a retail store. The class
should store the following data in attributes: item description, units in inventory, and price.
Once you have written the class, write a program that creates three RetailItem objects
and stores the following data in them:
​
            Description     Units in Inventory  Price
Item #1     Jacket          12                  59.95
Item #2     Designer Jeans  40                  34.95
Item #3     Shirt           20                  24.95
'''
class RetailItem:
    # define __init__()
    def __init__(self, p_desc, p_units, p_price):
        self.__description = p_desc
        self.__units_in_inventory = p_units
        self.__price = p_price

    # define setters/mutators
    def set_description(self, p_desc):
        self.__description = p_desc

    def set_unitsInInventory(self, p_units):
        self.__units_in_inventory = p_units

    def units_sold(self, p_amount):
        self.__units_in_inventory -= p_amount

    def units_gained(self, p_amount):
        self.__units_in_inventory += p_amount

    def set_price(self, p_price):
        self.__price = p_price

    # define getters
    def get_description(self):
        return self.__description

    def get_unitsInInventory(self):
        return self.__units_in_inventory

    def get_price(self):
        return self.__price
