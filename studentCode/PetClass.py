'''
1. Pet Class
    Write a class named Pet, which should have the following data attributes:
        • __name (for the name of a pet)
        • __animal_type (for the type of animal that a pet is. Example values are ‘Dog’, ‘Cat’,
        and ‘Bird’)
        • __age (for the pet’s age)
        The Pet class should have an __init__ method that creates these attributes. It should also
        have the following methods:
        • set_name
        This method assigns a value to the __name field.
        • set_animal_type
        This method assigns a value to the __animal_type field.
        • set_age
        This method assigns a value to the __age field.
        • get_name
        This method returns the value of the name field.
        • get_type
        This method returns the value of the type field.
        • get_age
        This method returns the value of the age field.
    Once you have written the class, write a program that creates an object of the class and
    prompts the user to enter the name, type, and age of his or her pet. This data should be
    stored as the object’s attributes. Use the object’s accessor methods to retrieve the pet’s name,
    type, and age and display this data on the screen.
'''
class Pet:
    # define __init__() with name, animal type, and age attributes
    def __init__(self, p_petName, p_petType, p_petAge):
        self.__name = p_petName.title()
        self.__animal_type = p_petType.title()
        self.__age = p_petAge

    # define the setters
    def set_name(self, p_petName):
        self.__name = p_petName.title()

    def set_animal_type(self, p_petType):
        self.__animal_type = p_petType.title()

    def set_age(self, p_petAge):
        self.__age = p_petAge
    
    # define the getters
        # define the setters
    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age