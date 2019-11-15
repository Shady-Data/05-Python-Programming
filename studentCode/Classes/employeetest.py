# This Program tests the Employee, ProductionWorker, and ShiftSupervisor classes

import EmployeeClass2
import random

def main():
    # Generate a list of ProductionWorkers/ShiftSupervisors
    employees = gen_employees()
    # Sort the employees by shift. Remove this if class lacks get_shift_num() method
    # base Employee class does not have the __shift_num attribute
    employees.sort(key=lambda x: x.get_shift_num())
    # iterate through the employees list
    for employee in employees:
        # Print the common attributes between the classes
        print('\nEmployee ID#:', employee.get_id_num())
        print('\tName:', employee.get_name())
        print('\tShift:', employee.get_shift_num())
        # Check for which class each employee belongs to
        if isinstance(employee, EmployeeClass2.ProductionWorker):
            # print the attributes specific specific to the ProductionWorker class
            print(f'\tHourly pay rate: ${employee.get_hourly_pay():.2f}')
        elif isinstance(employee, EmployeeClass2.ShiftSupervisor):
            # print the attributes specific specific to the ShiftSupervisor class
            print(f'\tSalary: ${employee.get_annual_salary():,.2f}')
            print(f'\tAnnual Production Bonus: ${employee.get_annual_prod_bonus():,.2f}')

def gen_employees():
    amount = random.randint(10,100)
    names_list = ["Dave", "David", "Rob", "Robert", "Tim", "Timothy", "Sue", "Susan", "Jess", "Jessica", 'Tom', 'Thomas', 'Jack', 'Jacob', 'Jerry', "Beth", "Mary", "Melinda"]
    classes = [EmployeeClass2.ProductionWorker, EmployeeClass2.ShiftSupervisor]
    bonuses = [0, 3000, 5000, 7000, 10000]
    rng_employee_ids = []
    result_list = []
    while len(rng_employee_ids) < amount:
        rng = random.randint(10000, 99999)
        if rng not in rng_employee_ids:
            rng_employee_ids.append(rng)
    counter = 0
    while len(result_list) < amount:
        name = random.choice(names_list)
        shift = random.randint(1,3)
        emp_type = random.choice(classes)
        if emp_type == classes[0]:
            hourly_pay = random.randint(10, 20) + random.random()
            employee = emp_type(name, rng_employee_ids[counter], shift, hourly_pay)
        elif emp_type == classes[1]:
            salary = random.randint(60000, 140000)
            employee = emp_type(name, rng_employee_ids[counter], shift, salary)
            bonus = random.choice(bonuses)
            employee.earned_prod_bonus(bonus)
        result_list.append(employee)
        counter += 1

    return result_list

main()
