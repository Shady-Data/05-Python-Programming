'''
3. continued...
    Write a test program that prompts the user to enter the three sides of the 
    triangle, a color, and 1 or 0 to indicate whether the triangle is filled. 
    The program should create a Triangle object with these sides and set the 
    color and filled properties using the input. The program should display the 
    triangle’s area, perimeter, color, and True or False to indicate whether the 
    triangle is filled or not.
'''

# import the triangle class module
import triangle_class

def main():
    # instantiate a 3 triangle objects
    triangle = get_triangle()
    # print the triangle object, __str__ calls getPerimeter() and getArea() methods
    print(triangle)

def get_triangle():
    # Create a dictionary to store the triangles arguments default values are class defaults
    args_dict = {'color': 'green', 'filled': True, 'side1': 1.0, 'side2': 1.0, 'side3': 1.0}
    for key in args_dict.keys():
        # if the key is not the filled key
        if key != 'filled':
            # get user input for each key
            args_dict[key] = input(f'{key}: ')
        else:
            # set a deafualt value for user input validation
            filled = -1
            # get the user input for the filled key
            while filled != 1 and filled != 0:
                try:
                    # get the user input for the filled value until filled is 1 of 0
                    filled = int(input('Is the triange filled, 1 = yes 0 = no: '))
                except ValueError as e:
                    # if an error occurs print the error and set the filled value to -1
                    print(e)
                    filled = -1
            # assign the filled argument with True of False based on filled
            if filled == 1:
                args_dict[key] = True
            else:
                args_dict[key] = False
    # return the triangle object
    return triangle_class.Triangle(args_dict['color'], args_dict['filled'], args_dict['side1'], args_dict['side2'], args_dict['side3'])

# call the main function
main()
