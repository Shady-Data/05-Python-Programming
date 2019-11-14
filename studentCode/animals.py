# The Mammal class represents a generic mammal

class Mammal:
    # The __init__ method accepts and argument for the mammal's species
    def __init__(self, species):
        self.__species = species

    def show_species(self):
        print('I am a', self.__species)

    # make_sound method
    def make_sound(self):
        print('Grrrr')

class Dog(Mammal):
    def __init__(self):
        Mammal.__init__(self, 'Dog')

    # This make_sound method overrides the superclasses (mammals) make_sound method
    def make_sound(self):
        print('Woof! Woof!')

class Cat(Mammal):
    def __init__(self):
        Mammal.__init__(self, 'Cat')

    # This make_sound method overrides the superclasses (mammals) make_sound method
    def make_sound(self):
        print('Meow')

def main():
    mammal = Mammal('Bigfoot')
    mammal.show_species()
    mammal.make_sound()

    cat = Cat()
    cat.show_species()
    cat.make_sound()

    dog = Dog()
    dog.show_species()
    dog.make_sound()

main()

