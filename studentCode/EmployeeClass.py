'''
4. Employee Class
    Write a class named Employee that holds the following data about an employee in attributes: 
    name, ID number, department, and job title.
    Once you have written the class, write a program that creates three Employee objects to
    hold the following data:
​
Name            ID Number       Department      Job Title
Susan Meyers    47899           Accounting      Vice President
Mark Jones      39119           IT              Programmer
Joy Rogers      81774           Manufacturing   Engineer
​
The program should store this data in the three objects and then display the data for each
employee on the screen.
'''

class Employee:
    # define the __init__ method
    def __init__(self, p_name, p_id, p_depart, p_title):
        self.__name = p_name.title()
        self.__id_num = p_id
        self.__department = p_depart.title()
        self.__title = p_title.title()

    # Define setters
    def set_name(self, p_name):
        self.__name = p_name.title()

    def set_id_num(self, p_id):
        self.__id_num = p_id

    def set_department(self, p_depart):
        self.__department = p_depart.title()

    def set_title(self, p_title):
        self.__title = p_title.title()

    # define getters
    def get_name(self):
        return self.__name
        
    def get_id_num(self):
        return self.__id_num
        
    def get_department(self):
        return self.__department
        
    def get_title(self):
        return self.__title
        
