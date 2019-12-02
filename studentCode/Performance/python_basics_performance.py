"""
Python Basics Performance Exam
​
    This exam is open note, open book, and open internet. Feel free to use any resources
    you can (other than someone else) to solve the following problems. Direct collaboration with another
    individual will result in immediate failure and consequences to follow. If you are unsure about 
    whether or not you can use a resource please ask me. If you are unsure about any of the prompts I can clarify. 
​
    Comments are necessary. 
​
    Each problem will weigh the same towards the final grade. 4 Problems at 25% each. 
​
    Please send each problem as a .py file separately. Please direct message them to me (Daniel Curran) 
    through slack. If there are supporting files for a problem then please send them with the .py file 
    as a zipped folder. 
​
    You will have 3 hours to complete this exam. If you complete this portion early and I have verified
    I have everything needed to grade your exam then you will be released.
​
    Happy Thanksgiving. 
​
1. 
    (Remove text) Write a program that removes all the occurrences of a specified
    string from a text file named pointsOfAuthority.txt. Your program should prompt the user to enter 
    a filename and a string to be removed.
​
    Points Of Authority - Linkin Park
​
        Forfeit the game
        Before somebody else
        Takes you out of the frame
        And puts your name to shame
        Cover up your face
        You can't run the race
        The pace is too fast
        You just won't last
​
        You love the way I look at you
        While taking pleasure in the awful things you put me through
        You take away if I give in
        My life, my pride is broken
​
        You like to think you're never wrong
        (You live what you've learned)
        You have to act like you're someone
        (You live what you've learned)
        You want someone to hurt like you
        (You live what you've learned)
        You want to share what you've been through
        (You live what you've learned)
​
        You love the things I say I'll do
        The way I'll hurt myself again just to get back at you
        You take away when I give in
        My life, my pride is broken
​
        You like to think you're never wrong
        (You live what you've learned)
        You have to act like you're someone
        (You live what you've learned)
        You want someone to hurt like you
        (You live what you've learned)
        You want to share what you've been through
        (You live what you've learned)
​
        Forfeit the game
        Before somebody else
        Takes you out of the frame
        And puts your name to shame
        Cover up your face
        You can't run the race
        The pace is too fast
        You just won't last
​
        Forfeit the game
        Before somebody else
        Takes you out of the frame
        And puts your name to shame
        Cover up your face
        You can't run the race
        The pace is too fast
        You just won't last
​
        You like to think you're never wrong
        (You live what you've learned)
        You have to act like you're someone
        (You live what you've learned)
        You want someone to hurt like you
        (You live what you've learned)
        You want to share what you've been through
        (You live what you've learned)
​
​
2.
    (Locate the largest element) Write the following function that returns the location
    of the largest element in a two-dimensional list:
    
    def locateLargest(a):
        The return value is a one-dimensional list that contains two elements. These
        two elements indicate the row and column indexes of the largest element in the
        two-dimensional list. Write a test program that prompts the user to enter a 
        two-dimensional list and displays the location of the largest element in the list. 
    
    Here is a sample run(You don't have to mimic this, this is just a guide):
​
        Enter the number of rows in the list: 3
        Enter a row: 23.5  35  2    10
        Enter a row: 4.5   3   45   3.5
        Enter a row: 35    44  5.5  11.6
        The location of the largest element is at (1,2)
​
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
​
​
    class GeometricObject:
        def __init__(self, color = "green", filled = True):
            self.color = color
            self.filled = filled
​
        def getColor(self):
            return self.color
​
        def setColor(self, color):
            self.color = color
​
        def isFilled(self):
            return self.filled
​
        def setFilled(self, filled):
            self.filled = filled
    
        def toString(self):
            return "color: " + self.color + " and filled: " + str(self.filled)
​
​
    Write a test program that prompts the user to enter the three sides of the 
    triangle, a color, and 1 or 0 to indicate whether the triangle is filled. 
    The program should create a Triangle object with these sides and set the 
    color and filled properties using the input. The program should display the 
    triangle’s area, perimeter, color, and True or False to indicate whether the 
    triangle is filled or not.
​
4. 
    (The sqrt function) Write a program that prints the following table
    using your knowledge of loops and the sqrt function in the math module.
    Make sure your table is neat by using print formatting methods we've learned. 
​
        Number  Square Root
        0       0.0000
        1       1.0000
        2       1.4142
        ...
        18      4.2426
        20      4.4721
​
"""