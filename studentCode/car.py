# This program tests the car class by instantiating a Car class object
# sending accelerate and brake methods, and displays current speed

import CarClass as car

def main():
    # Prompt for the year model and make
    year_model = input('Enter the Year/Model of the vehicle: ')
    make = input('Enter the make of the vehicle: ')

    # create the Car class object
    auto = car.Car(year_model, make)

    # call the accelerate method 5x
    for _ in range(5):
        auto.accelerate()
        print('Current speed is', auto.get_speed())

    # call the brake method 5x
    for _ in range(5):
        auto.brake()
        print('Current speed is', auto.get_speed())

# call the main function
main()