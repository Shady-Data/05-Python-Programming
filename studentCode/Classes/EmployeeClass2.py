'''
1. Employee and ProductionWorker Classes
    Write an Employee class that keeps data attributes for the following pieces of information:
        • Employee name
        • Employee number
    Next, write a class named ProductionWorker that is a subclass of the Employee class. The
    ProductionWorker class should keep data attributes for the following information:
        • Shift number (an integer, such as 1, 2, or 3)
        • Hourly pay rate
    The workday is divided into two shifts: day and night. The shift attribute will hold an integer value representing the shift that the employee works. The day shift is shift 1 and the
    night shift is shift 2. Write the appropriate accessor and mutator methods for each class.
    Once you have written the classes, write a program that creates an object of the
    ProductionWorker class and prompts the user to enter data for each of the object’s data
    attributes. Store the data in the object and then use the object’s accessor methods to retrieve
    it and display it on the screen.
'''

class Employee:
    def __init__(self, p_name, p_id_num):
        self.__name = p_name
        self.__id_num = p_id_num

    def set_name(self, p_name):
        self.__name = p_name

    def set_id_num(self, p_id_num):
        self.__id_num = p_id_num

    def get_name(self):
        return self.__name

    def get_id_num(self):
        return self.__id_num

class ProductionWorker(Employee):
    def __init__(self, p_name, p_id_num, p_shift_num, p_hourly_pay):
        super().__init__(p_name, p_id_num)
        self.__shift_number = p_shift_num
        self.__hourly_pay_rate = p_hourly_pay

    def set_shift_num(self, p_shift_num):
        self.__shift_number = p_shift_num
    
    def set_hourly_pay(self, p_hourly_pay):
        self.__hourly_pay_rate = p_hourly_pay

    def get_shift_num(self):
        return self.__shift_number

    def get_hourly_pay(self):
        return self.__hourly_pay_rate

'''
2. ShiftSupervisor Class
    In a particular factory, a shift supervisor is a salaried employee who supervises a shift. In
    addition to a salary, the shift supervisor earns a yearly bonus when his or her shift meets
    production goals. Write a ShiftSupervisor class that is a subclass of the Employee class
    you created in Programming Exercise 1. The ShiftSupervisor class should keep a data
    attribute for the annual salary and a data attribute for the annual production bonus that a
    shift supervisor has earned. Demonstrate the class by writing a program that uses a
    ShiftSupervisor object.
'''

class ShiftSupervisor(Employee):
    def __init__(self, p_name, p_id_num, p_shift_num, p_annual_salary):
        super().__init__(p_name, p_id_num)
        self.__shift_number = p_shift_num
        self.__annual_salary = p_annual_salary
        self.__annual_prod_bonus = 0

    def set_shift_num(self, p_shift_num):
        self.__shift_number = p_shift_num

    def set_annual_salary(self, p_annual_salary):
        self.__annual_salary = p_annual_salary

    def set_annual_prod_bonus(self, p_bonus):
        self.__annual_prod_bonus = p_bonus

    def salary_raise_by_percent(self, p_percent_increase):
        if p_percent_increase < 1:
            self.__annual_salary = self.__annual_salary + (self.__annual_salary * p_percent_increase)
        else:
            self.__annual_salary = self.__annual_salary + (self.__annual_salary * (p_percent_increase/100))
    
    def salary_lower_by_percent(self, p_percent_decrease):
        if p_percent_decrease < 1:
            self.__annual_salary = self.__annual_salary - (self.__annual_salary * p_percent_decrease)
        else:
            self.__annual_salary = self.__annual_salary - (self.__annual_salary * (p_percent_decrease/100))

    def salary_raise_by_amount(self, p_raise_amount):
        self.__annual_salary += p_raise_amount

    def salary_lower_by_amount(self, p_lower_amount):
        self.__annual_salary += p_lower_amount

    def earned_prod_bonus(self, p_bonus):
        self.__annual_prod_bonus += p_bonus

    def get_annual_salary(self):
        return self.__annual_salary

    def get_annual_prod_bonus(self):
        return self.__annual_prod_bonus

    def get_shift_num(self):
        return self.__shift_number

        