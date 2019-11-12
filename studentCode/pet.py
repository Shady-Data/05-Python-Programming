# This Program tests the Pet class by instantiating an Pet Class object
# and displays the information in the object back

# import the Pet Class
import PetClass as pet

def main():
    # Prompt for the pets name, animal type, and age
    pet_name = input('Enter the pet\'s name: ').title()
    pet_type = input(f'What type of animal is {pet_name}?: ')
    try:
        pet_age = float(input(f'How old is {pet_name}: '))
    except ValueError:
        pet_age = ''
        while type(pet_age) != float:
            pet_age = input(f'Bad Input!\nPlease enter {pet_name}\'s age: ')
            if pet_age.isdecimal():
                pet_age = float(pet_age)
    
    # instantiate the Pet class object
    my_pet = pet.Pet(pet_name, pet_type, pet_age)

    # display the information using the 'get_' methods
    print('\n\tPet Name:', my_pet.get_name())
    print('\tPet Animal Type:', my_pet.get_animal_type())
    print('\tPet Age:', my_pet.get_age())

# call the main function
main()