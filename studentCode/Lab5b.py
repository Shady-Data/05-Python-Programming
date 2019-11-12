'''
Create a Simple Super hero class. Some attributes you will need:

- Hero Name
- Real Name
- Power(s)
- etc

Requirements
- Adhere to PEP8 and utilize proper and efficient code
- Utilize an __init__()
- Ensure variables are correct type (class vs instance variables)
- Utilize methods:
    - start to format your class using getters and setters
- Create an instance of your class. Populate it with data utilizing an init and/or getters and setters
'''

class SuperHero:
    # define the __init__ for the class
    def __init__(self, p_heroName, p_realName, p_powers=['Unknown']):
        self.__hero_name = p_heroName.title()
        self.__real_name = p_realName.title()
        self.__powers = [] + p_powers
        self.format_powers()

    # define setters
    def set_hero_name(self, p_heroName):
        self.__hero_name = p_heroName.title()

    def set_real_name(self, p_realName):
        self.__real_name = p_realName.title()

    def set_power(self, p_powers):
        # if p_powers is a list
        if type(p_powers) == list:
            # iterate through each power
            for power in p_powers:
                # check if the power is already list
                if power.title() not in self.__powers:
                    # if not in the powers list, append it
                    self.__powers.append(power.title())
        # else if p_powers is a string
        elif type(p_powers) == str:
            # check if the power is already list
            if p_powers.title() not in self.__powers:
                # if not in the powers list, append it
                self.__powers.append(p_powers.title())

    # define getters
    def get_hero_name(self):
        return self.__hero_name

    def get_real_name(self):
        return self.__real_name

    def get_powers(self):
        return self.__powers

    # format the powers list to be uniform title case
    def format_powers(self):
        # enumerate though the powers listing
        for index, power in enumerate(self.__powers):
            # replace the power inplace with title case
            self.__powers[index] = power.title()

    # remove a power from the list
    def remove_power(self, p_power):
        # check if p_power is in the powers list
        if p_power.title() in self.__powers:
            self.__powers.remove(p_power.title())

def main():
    # initialize a superhero class
    hero = SuperHero('Superman', 'Clark Kent', ['Super Strength', 'flight', 'Super Hearing'])

    print(hero.get_powers())
    print('Oops. forgot to some powers')
    hero.set_power(['Laser Vision', 'freezing breath'])
    print(hero.get_powers())
    print('What! He\'s super tough as well!')
    hero.set_power('Super Tough')
    hero.remove_power('flight')
    print(hero.get_powers())
    print('Did I remember to add flight?')
    hero.set_power('flight')
    print(hero.get_powers())



main()
