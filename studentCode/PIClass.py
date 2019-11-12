'''
3. Personal Information Class
    Design a class that holds the following personal data: name, address, age, and phone number. Write 
    appropriate accessor and mutator methods. Also, write a program that creates
    three instances of the class. One instance should hold your information, and the other two
    should hold your friends’ or family members’ information.
'''
class PersonalInformation:
    # define the __init__ method with name, address, age and phone number attributes
    def __init__(self, p_name, p_address, p_age, p_phone):
        self.__name = p_name
        self.__address = p_address
        self.__age = p_age
        self.__phone = p_phone

    # define setters/mutators
    def set_name(self, p_name):
        self.__name = p_name

    def set_address(self, p_address):
        self.__address = p_address