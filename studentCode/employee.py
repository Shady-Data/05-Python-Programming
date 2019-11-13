# This program tests the Employee class by generating 3 objects and
# displaying their contained information

from random import randint
# import the employee class
import EmployeeClass

def main():
    # get the list of objects to display
    employees = get_employees(3)
    # display the information
    display_employees(employees)

# define the get employees function
def get_employees(p_amount):
    # Create and empty list to store the objects generated
    result_list = []
    # Prompt for p_amount objects information
    for emp in range(1, p_amount + 1):
        print(f'\nEmployee entry {emp}:')
        name = input('Enter the employee\'s name: ').title()
        department = input(f'What department is {name} assigned?: ')
        title = input(f'{name}\'s work title?: ')
        # grab a randomly generated 5-digit employee id
        id_num = randint(10000, 99999)

        # add the data to an emplyee object
        employee = EmployeeClass.Employee(name, id_num, department, title)
        # add the object to the returning list
        result_list.append(employee)
    # return the list of employee objects
    return result_list

# define the display employees
def display_employees(p_list):
    # iterate through the list
    for employee in p_list:
        # Display the employee's information
        print(f'\nEmployee ID: {employee.get_id_num()}')
        print(f'\tName: {employee.get_name()}')
        print(f'\tTitle: {employee.get_title()}')
        print(f'\tDepartment: {employee.get_department()}')

# call the main function
main()

