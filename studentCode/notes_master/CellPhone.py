"""
Wireless Solutions, Inc. is a business that sells cell phones and wireless service. 
You are a programmer in the company’s IT department, and your team is designing a program to manage
all of the cell phones that are in inventory. You have been asked to design a class that represents 
a cell phone. The data that should be kept as attributes in the class are as follows:
​
    • The name of the phone’s manufacturer will be assigned to the __manufact attribute.
    • The phone’s model number will be assigned to the __model attribute.
    • The phone’s retail price will be assigned to the __retail_price attribute.
​
The class will also have the following methods:
    • An __init__ method that accepts arguments for the manufacturer, model number,
    and retail price.
    • A set_manufact method that accepts an argument for the manufacturer. This
    method will allow us to change the value of the __manufact attribute after the object has been created, if necessary.
    • A set_model method that accepts an argument for the model. This method will allow
    us to change the value of the __model attribute after the object has been created, if
    necessary.
    • A set_retail_price method that accepts an argument for the retail price. This
    method will allow us to change the value of the __retail_price attribute after the
    object has been created, if necessary.
    • A get_manufact method that returns the phone’s manufacturer.
    • A get_model method that returns the phone’s model number.
    • A get_retail_price method that returns the phone’s retail price.
"""
class CellPhone:
    # define the __init__ method  with 3 attributes
    def __init__(self, p_manufacturer, p_model, p_msrp):
        self.__manufact = p_manufacturer
        self.__model = p_model
        self.__retail_price = p_msrp

    # define set_manufact to modify the __manufact attribute, if necessary
    def set_manufact(self, p_manufact):
        self.__manufact = p_manufact

    # define set_model to modify the __model attribute, if necessary
    def set_model(self, p_model):
        self.__model = p_model

    # define set_retail_price to modify the __retail_price attribute, if necessary
    def set_retail_price(self, p_msrp):
        self.__retail_price = p_msrp

    # define get_manufact to return the __manufact attribute
    def get_manufact(self):
        return self.__manufact

    # define get_model to return the __model attribute
    def get_model(self):
        return self.__model

    # define get_retail_price to return the __retail_price attribute
    def get_retail_price(self):
        return self.__retail_price