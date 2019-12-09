import random
class Coin:

    # the __init__ method is called whe the object is initialized (assigned to a variable)
    def __init__(self):
        # self.attibute are specific to that object
        # __attribute is private and can/should only be modifiable by class methods
        self.__sideup = 'Heads'

    # The __str__ method returns a string
    # indicating the object's state
    def __str__(self):
        return f'{self.__sideup} is showing'

    # methods are functions defined within a class
    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = 'Tails'

    def get_sideup(self):
        return self.__sideup