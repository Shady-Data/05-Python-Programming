'''
3. Person and Customer Classes
    Write a class named Person with data attributes for a person’s name, address, and telephone number. Next, write a class named Customer that is a subclass of the Person class.
    The Customer class should have a data attribute for a customer number and a Boolean data
    attribute indicating whether the customer wishes to be on a mailing list. Demonstrate an
    instance of the Customer class in a simple program.
'''
import PersonClass
import random

def main():
    # Create a list of Person and Customer Objects
    people = gen_people_list()
    # create a mailing list
    mailing_list = [p for p in people if isinstance(p, PersonClass.Customer) and p.get_mailing_list()]
    # iterate through the list
    for obj in people:
        # if the obj is of the Customer class
        if isinstance(obj, PersonClass.Customer):
            # Print the attributes specific to the class
            print('\nCustomer #:', obj.get_customer_num())
            print('\tName:', obj.get_name())
            print('\tMailing List:', obj.get_mailing_list())
        else:
            print('\nName:', obj.get_name())
        # Display the Common Attributes
        print('\tAddress:', obj.get_address())
        print('\tPhone:', obj.get_phone())

    print('\nMailing list:')
    for obj in mailing_list:
        print('\tName: ' + obj.get_name() + '\tAddress: ' + obj.get_address())


def gen_people_list():
    # This function simulates user input by randomly
    # generating Person and Customer objects
    # select the number of objects to generate
    amount = random.randint(10,100)
    # populate lists of information to pull from
    names_list = ["Dave", "David", "Rob", "Robert", "Tim", "Timothy", "Sue", "Susan", "Jess", "Jessica", 'Tom', 'Thomas', 'Jack', 'Jacob', 'Jerry', "Beth", "Mary", "Melinda"]
    classes = [PersonClass.Person, PersonClass.Customer]
    street_names = ['Birch', 'Maple', 'Oak', 'Pine', 'Evergreen', 'Aspen', 'Ash', 'Cherry']
    street_type = ['st', 'dr', 'loop', 'lane', 'blvd']
    rng_customer_ids = []
    mail_choice = [True, False]
    # Create an empty list to store the objects in
    result_list = []
    # generate random unique customer ids
    while len(rng_customer_ids) < amount:
        rng = random.randint(10000, 99999)
        if rng not in rng_customer_ids:
            rng_customer_ids.append(rng)
    # generate the objects until the amount is reached
    while len(result_list) < amount:
        name = random.choice(names_list)
        address = str(random.randint(1, 50000)) + ' ' + random.choice(street_names) + ' ' + random.choice(street_type)
        phone = '555-' + str(random.randint(1000, 9999))
        per_type = random.choice(classes)
        if per_type == classes[0]:
            customer = per_type(name, address, phone)
        elif per_type == classes[1]:
            mail = random.choice(mail_choice)
            customer = per_type(name, address, phone, rng_customer_ids.pop(), mail)
        result_list.append(customer)

    return result_list

# call the main function
main()