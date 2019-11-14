'''
3. Person and Customer Classes
    Write a class named Person with data attributes for a person’s name, address, and telephone number. Next, write a class named Customer that is a subclass of the Person class.
    The Customer class should have a data attribute for a customer number and a Boolean data
    attribute indicating whether the customer wishes to be on a mailing list. Demonstrate an
    instance of the Customer class in a simple program.
'''

class Person:
    def __init__(self, p_name, p_address, p_phone):
        self.__name = p_name
        self.__address = p_address
        self.__phone = p_phone

    def set_name(self, p_name):
        self.__name = p_name

    def set_address(self, p_address):
        self.__address = p_address

    def set_phone(self, p_phone):
        self.__phone = p_phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

class Customer(Person):
    def __init__(self, p_name, p_address, p_phone, p_customer_num, p_mailing_list):
        Person.__init__(self, p_name, p_address, p_phone)
        self.__customer_num = p_customer_num
        if p_mailing_list == 'y' or p_mailing_list == 'yes' or p_mailing_list == True:
            self.__mailing_list = True
        else:
            self.__mailing_list = False

    def set_customer_num(self, p_customer_num):
        self.__customer_num = p_customer_num

    def set_mailing_list(self, p_mailing_list):
        if p_mailing_list == 'y' or p_mailing_list == 'yes' or p_mailing_list == True:
            self.__mailing_list = True
        else:
            self.__mailing_list = False

    def get_customer_num(self):
        return self.__customer_num

    def get_mailing_list(self):
        return self.__mailing_list