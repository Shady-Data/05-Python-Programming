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

    # test_sal(employees)

def test_sal(employees):
    supervisors = [s for s in employees if isinstance(s, EmployeeClass2.ShiftSupervisor)]
    for shiftsup in supervisors:
        salary_mods = [shiftsup.salary_raise_by_percent, shiftsup.salary_lower_by_percent, shiftsup.salary_raise_by_amount, shiftsup.salary_lower_by_amount, shiftsup.earned_prod_bonus]
        modifier = random.choice(salary_mods)
        print('--------------------')
        if modifier == salary_mods[0] or modifier == salary_mods[1]:
            salary = shiftsup.get_annual_salary()
            whole = random.randint(1, 5)
            percent = whole/100
            print('Salary before Mod:', shiftsup.get_annual_salary())
            print('Modifier selected: ' + str(modifier) + ' by ' + str(percent) + '%')
            if modifier == salary_mods[0]:
                exp_salary = int(salary + (salary * percent))
            elif modifier == salary_mods[1]:
                exp_salary = int(salary - (salary * percent))
            else:
                print('Error')
                exp_salary = 0
            print(f'\n\tExpected return: ${exp_salary:,}')
            modifier(percent)
            print('After percent execution:', shiftsup.get_annual_salary())
            print('Setting salary back to:', salary)
            shiftsup.set_annual_salary(salary)
            print('Modifier selected: ' + str(modifier) + ' by ' + str(whole))
            modifier(whole)
            print('After whole number execution:', shiftsup.get_annual_salary())
            print('Setting salary back to:', salary)
            shiftsup.set_annual_salary(salary)
        elif modifier == salary_mods[2] or modifier == salary_mods[3]:
            salary = shiftsup.get_annual_salary()
            amount = random.randint(1000, 20000)
            print('Salary before Mod:', shiftsup.get_annual_salary())
            print('Modifier selected: ' + str(modifier) + ' by ' + str(amount))
            if modifier == salary_mods[2]:
                exp_salary = salary + amount
            elif modifier == salary_mods[3]:
                exp_salary = salary - amount
            else:
                print('Error')
                exp_salary = 0
            print(f'\n\tExpected return: ${exp_salary:,}')
            modifier(amount)
            print('After Excution:', shiftsup.get_annual_salary())
            print('Setting salary back to:', salary)
            shiftsup.set_annual_salary(salary)
        elif modifier == salary_mods[4]:
            bonus = shiftsup.get_annual_prod_bonus()
            earned = random.randint(1000,5000)
            print('Modifier selected: ' + str(modifier) + ' by ' + str(earned))
            print('Bonus before modification:', shiftsup.get_annual_prod_bonus())
            exp_bonus = bonus + earned
            print(f'\n\tExpected return: ${exp_bonus:,}')
            modifier(earned)
            print('After Execution:', shiftsup.get_annual_prod_bonus())
            print('Setting bonus back to:', bonus)
            shiftsup.set_annual_prod_bonus(bonus)




def gen_employees():
    # This function simulates expected user input and generates a list of ProductionWorker and ShiftSupervisor objects
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
