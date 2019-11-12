'''
2. Car Class
    Write a class named Car that has the following data attributes:
        • __year_model (for the car’s year model)
        • __make (for the make of the car)
        • __speed (for the car’s current speed)
        The Car class should have an __init__ method that accept the car’s year model and make
        as arguments. These values should be assigned to the object’s __year_model and __make
        data attributes. It should also assign 0 to the __speed data attribute.
        The class should also have the following methods:
        • accelerate
        The accelerate method should add 5 to the speed data attribute each time it is
        called.
        • brake
        The brake method should subtract 5 from the speed data attribute each time it is called.
        • get_speed
        The get_speed method should return the current speed.
    Next, design a program that creates a Car object, and then calls the accelerate method
    five times. After each call to the accelerate method, get the current speed of the car and
    display it. Then call the brake method five times. After each call to the brake method, get
    the current speed of the car and display it.
'''
class Car:
    # define the __init__ method with model year and make
    def __init__(self, p_modelYear, p_make):
        self.__year_model = p_modelYear
        self.__make = p_make
        self.__speed = 0

    # define the accelerate method
    def accelerate(self):
        # add 5 to the speed attribute
        self.__speed += 5

    # define the brake method
    def brake(self):
        # if speed attribute is >= 5
        if self.__speed >= 5:
            # subtract 5 from the speed attribute
            self.__speed -= 5

    # define the get_speed method
    def get_speed(self):
        return self.__speed