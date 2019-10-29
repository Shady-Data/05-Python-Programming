"""
Lab 2G: Planets Exercise
Recommended Version: Python 2.7

Instructions:
-Follow TODO's below
"""


planet_string = "Mercury|Venus|Earth|Mars|Jupiter|Saturn|Uranus|Neptune"
planet_list = planet_string.split('|')
#TODO: Convert planets_string to a list, save it to planet_list.

def log_planets():
    print("Here is a list of the planets:")
    for planet in planet_list:
        print(planet)
    print("----------------\n\n")

log_planets()

print 'Adding "The Sun" to the beginning of the planets list.'
planet_list.insert(0, "The Sun")
#TODO: Perform action above
log_planets()

print 'Adding "Pluto" to the end of the planets list.'
planet_list.append("Pluto")
#TODO: Perform action above
log_planets()

print 'Removing "The Sun" from the beginning of the planets list.'
#TODO: Perform action above
log_planets()

print 'Removing "Pluto" from the end of the planets list.'
#TODO: Perform action above
log_planets()

print 'Finding and logging the index of "Earth" in the planets list.'
#TODO: Perform action above
log_planets()

print 'Removing the planet after "Earth".'
#TODO: Perform action above.  
log_planets()

print 'Addding back in the planet removed after "Earth".'
#TODO: Perform action above
log_planets()

print 'Reversing the order of the planets list.'
#TODO Perform action above
log_planets()

print 'Sorting the planets list'
#TODO Perform action above
log_planets()