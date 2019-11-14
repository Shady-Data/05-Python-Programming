# Inheritance

# Inheritance allows a new class to extend an existing class. The new class inherits
# the members of the class it extends

# goto vehicles.py
import vehicles
# goto car_demo.py
# goto car_truck_suv.py

print(help(vehicles.SUV))

# Method Resolution Order
# - Inherited Methods

# suv_object.__dict__ returns a dictionary representation of the object

# isinstance(obj, class) returns True/False
# issubclass(subclass, class) returns True/False