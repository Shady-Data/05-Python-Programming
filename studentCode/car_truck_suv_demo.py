# This program creates a Car object, a Truck object, and a SUV object

import vehicles

def main():
    # create a Car object
    car = vehicles.Car('Bugatti', 'Veyron', 0, 3000000, 2)

    # create a Truck object
    truck = vehicles.Truck('Dodge', 'Power Wagon', 0, 57000, '4WD')

    # create a SUV object
    suv = vehicles.SUV('Jeep', 'Wrangler', 200000, 5000, 4)

    print('Vehicle Inventory')
    print('=================')

    # Display the car's information
    print('Make: ', car.get_make())
    print('Model: ', car.get_model())
    print('Mileage: ', car.get_mileage())
    print('Price: ', car.get_price())
    print('# of Doors: ', car.get_doors())

    # Display the trucks's information
    print('Make: ', truck.get_make())
    print('Model: ', truck.get_model())
    print('Mileage: ', truck.get_mileage())
    print('Price: ', truck.get_price())
    print('Drive Type: ', truck.get_drive_type())

    # Display the suv's information
    print('Make: ', suv.get_make())
    print('Model: ', suv.get_model())
    print('Mileage: ', suv.get_mileage())
    print('Price: ', suv.get_price())
    print('Passenger Capacity: ', suv.get_pass_cap())

# call the main function
main()