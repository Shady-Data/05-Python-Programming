'''
3. 
(The Triangle class) Design a class named Triangle that extends the
GeometricObject class defined below. The Triangle class contains:
    - Three float data fields named side1, side2, and side3 to denote the three
    sides of the triangle.
    - A constructor that creates a triangle with the specified side1, side2, and
    side3 with default values 1.0.
    - The accessor methods for all three data fields.
    - A method named getArea() that returns the area of this triangle.
    - A method named getPerimeter() that returns the perimeter of this triangle.
    - A method named __str__() that returns a string description for the triangle.

        Write a test program that prompts the user to enter the three sides of the 
    triangle, a color, and 1 or 0 to indicate whether the triangle is filled. 
    The program should create a Triangle object with these sides and set the 
    color and filled properties using the input. The program should display the 
    triangle’s area, perimeter, color, and True or False to indicate whether the 
    triangle is filled or not.
​'''

from math import sqrt

class GeometricObject:
    def __init__(self, color = "green", filled = True):
        self.color = color
        self.filled = filled

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def isFilled(self):
        return self.filled

    def setFilled(self, filled):
        self.filled = filled

    def toString(self):
        return "color: " + self.color + " and filled: " + str(self.filled)

class Triangle(GeometricObject):
    # def the constructor for the triangle with parents requirements + 3 sides, the default value for sides = 1.0
    def __init__(self, p_color='green', p_filled=True, p_side1=1.0, p_side2=1.0, p_side3=1.0):
        # call the parents init function to set the parent and filled attributes
        super().__init__(p_color, p_filled)
        # set the 3 new side attributes with the float type values
        self.__side1 = float(p_side1)
        self.__side2 = float(p_side2)
        self.__side3 = float(p_side3)

    # define the mutator for the new attributes
    def set_side1(self, p_side1):
        self.__side1 = float(p_side1)

    def set_side2(self, p_side2):
        self.__side2 = float(p_side2)

    def set_side3(self, p_side3):
        self.__side3 = float(p_side3)

    # define the accessor for the new attributes
    def get_side1(self):
        return self.__side1

    def get_side2(self):
        return self.__side2

    def get_side3(self):
        return self.__side3

    # define the getArea() method
    def getArea(self):
        # If you have all three sides, you'll use Heron's formula, and the formula for the area of a triangle.
        # assumed side2 as the base
        # s = (a+b+c)/2
        # Area = 1/2bh
        # Heron's formaula: Area = 2*(sqr(s(s-a)(s-b)(s-c)) or h = sqr(s(s-a)(s-b)(s-c)))/b
        # make a list of the triangles sides
        sides = [self.__side1, self.__side2, self.__side3]
        # get s by dividing the perimeter by 2
        s = self.getPerimeter()/2
        # Calculate the height assuming side 2 as the base, h = sqr(s(s-a)(s-b)(s-c))/2b
        h = 2 * (sqrt(s*(s - sides[0]) * (s - sides[1]) * (s - sides[2]))) / (sides[1])
        # return the calculated area
        return 0.5 * sides[1] * h

    # define the getPerimeter() method
    def getPerimeter(self):
        return self.__side1 + self.__side2 + self.__side3

    # define the __str__() method
    def __str__(self):
        # return the attributes of the triangle
        return self.toString() + f' with Sides: {self.__side1:.1f}, {self.__side2:.1f}, {self.__side1:.1f} Perimeter: {self.getPerimeter()}, Area: {self.getArea()}'