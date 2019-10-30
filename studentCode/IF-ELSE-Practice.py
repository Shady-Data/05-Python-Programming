# 1. Roman Numerals

# Design a program that prompts the user to enter a number within the range of 1 through 10. The program should display the Roman numeral version of that number. If the number is outside the range of 1 through 10, the program should display an error message.

# Start // romanNumeral
def to_roman_numeral():
#     Declare Integer numEntry
#     Display "Enter a number between 1 and 10, inclusive: "
#     Input numEntry
    num_to_roman = int(input("Enter a number between 1 and 10: "))
    roman_dict = {1: "I", 2: "II", 3: "III", 4: "IV" , 5: "V" , 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X"}
#     Select numEntry
#         Case 1:
#             Display "I"
#         Case 2:
#             Display "II"
#         Case 3:
#             Display "III"
#         Case 4:
#             Display "IV"
#         Case 5:
#             Display "V"
#         Case 6:
#             Display "VI"
#         Case 7:
#             Display "VII"
#         Case 8:
#             Display "VIII"
#         Case 9:
#             Display "IX"
#         Case 10:
#             Display "X"
#         Default:
#             Display "Error: outside of expected input range."
#     End Select
    if num_to_roman in roman_dict.keys():
        print("{} is {} in roman numerals.".format(num_to_roman, roman_dict[num_to_roman]))
    else:
        print("Error: input is outside of expected range.")

# Stop
# to_roman_numeral()
print('')

# 2. Areas of Rectangles

# The area of a rectangle is the rectangle’s length times its width. Design a program that asks for the length and width of two rectangles. The program should tell the user which rectangle has the greater area, or whether the areas are the same.

# Start // rectangleAreaCompare
def rectangleAreaCompare():
#     Declare Real length1, width1, length2, width2, area1, area2
#     Display "Please enter the length of the first rectangle: "
#     Input length1
    rect_1_length = float(input("Please enter the length of the first rectangle: "))
#     Display "Please enter the width of the first rectangle: "
#     Input width1
    rect_1_width = float(input("Please enter the width of the first rectangle: "))
#     Display "Please enter the length of the second rectangle: "
#     Input length2
    rect_2_length = float(input("Please enter the length of the second rectangle: "))
#     Display "Please enter the width of the second rectangle: "
#     Input width2
    rect_2_width = float(input("Please enter the width of the second rectangle: "))

#     Set area1 = length1 * width1
    rect_1_area = rect_1_length * rect_1_width
#     Set area2 = length2 * width2
    rect_2_area = rect_2_length * rect_2_width

#     If area1 > area2 Then
    if rect_1_area > rect_2_area:
#         Display "The First Rectangle has the greater area."
        print("The first rectangle has the greater area.")
#     Else If area2 > area1 Then
    elif rect_1_area < rect_2_area:
#         Display "The second Rectangle has the greater area."
        print("The second rectangle has the greater area.")
#     Else
    else:
#         Display "Both Rectangles have the same area."
        print("Both Rectangles have the same area.")
# Stop

# rectangleAreaCompare()

# 3. Mass and Weight

# Scientists measure an object’s mass in kilograms and its weight in Newtons. If you know the amount of mass of an object, you can calculate its weight, in Newtons, with the following formula:

# ![image](https://user-images.githubusercontent.com/47218880/67404289-c6b2d480-f578-11e9-80c0-9bfa15de3df7.png)

# Design a program that asks the user to enter an object’s mass, and then calculates its weight. If the object weighs more than 1,000 Newtons, display a message indicating that it is too heavy. If the object weighs less than 10 Newtons, display a message indicating that it is too light.

def mass_weight_calc():
    '''
    Prompts a user to enter an object's mass, calulates a weight from the mass,
    and prints a statement based on the object's weight.
    '''
    # get the mass of the object from the user
    mass = float(input("Enter the mass of the object: "))
    # calculate weight = mass * 9.8
    weight = mass * 9.8

    # if weight is > than 1000 then
    if weight > 1000:
        # Display the object is too heavy
        print("The object is too heavy")
    # Else if weight < 10 then
    elif weight < 10:
        print("The object is too light")


# mass_weight_calc()

# 4. Magic Dates

# The date June 10, 1960, is special because when it is written in the following format, the month times the day equals the year:

# ![image](https://user-images.githubusercontent.com/47218880/67404336-d92d0e00-f578-11e9-9801-6742f67d71fe.png)

# Design a program that asks the user to enter a month (in numeric form), a day, and a two-digit year. The program should then determine whether the month times the day equals the year. If so, it should display a message saying the date is magic. Otherwise, it should display a message saying the date is not magic.

# def magic_dates():


# 5. Color Mixer

# The colors red, blue, and yellow are known as the primary colors because they cannot be made by mixing other colors. When you mix two primary colors, you get a secondary color, as shown here:
# ```
# When you mix red and blue, you get purple.

# When you mix red and yellow, you get orange.

# When you mix blue and yellow, you get green.
# ```
# Design a program that prompts the user to enter the names of two primary colors to mix. If the user enters anything other than “red,” “blue,” or “yellow,” the program should display an error message. Otherwise, the program should display the name of the secondary color that results.

# Start // colorMixer
def color_mixer():
#     Declare String priColor1, priColor2
    user_colors = {'color_1': "", 'color_2': ''}
    # dictionary of primary colors with values of dictionaries containing mix results
    colours = {"red": {"red": "red", "blue": "purple", "yellow": "orange"}, "blue": {"red": "purple", "blue": "blue", "yellow": "green"}, "yellow": {"red": "orange", "blue": "green", "yellow": "yellow"}}
#     Display "Please enter the first color to mix 'red, yellow, or blue': "
#     Input priColor1
#     Display "Please enter the second color to mix 'red, yellow, or blue': "
#     Input priColor2
    # iterate through user_colors keys to assign user input
    for key in user_colors.keys():
        # loop continuously until user input is in the colours keys
        while user_colors[key] not in colours.keys():
            # Prompt user for input and assign the all lowercase value of the input to the key of user_colors
            user_colors[key] = str.lower(input("Enter a primary color to mix, red, blue, or yellow: "))
        
#     Select priColor1
#         Case red:
#             Select priColor2
#                 Case red:
#                     Display "Mixed color is still red."
#                 Case blue:
#                     Display "Mixed color is purple."
#                 Case yellow:
#                     Display "Mixed color is orange."
#                 Default:
#                     Display "Error: not a primary color"
#             End Select
#         Case blue:
#             Select priColor2
#                 Case red:
#                     Display "Mixed color is purple."
#                 Case blue:
#                     Display "Mixed color is still blue."
#                 Case yellow:
#                     Display "Mixed color is green."
        #         Default:
        #             Display "Error: not a primary color"
        #     End Select
        # Case yellow:
        #     Select priColor2
        #         Case red:
        #             Display "Mixed color is orange."
        #         Case blue:
        #             Display "Mixed color is green."
        #         Case yellow:
        #             Display "Mixed color is still yellow."
        #         Default:
        #             Display "Error: not a primary color"
        #     End Select
        # Default:
#             Display "Error: not a primary color"
#     End Select
    print("{} and {} become {} when mixed.".format(user_colors['color_1'], user_colors['color_2'], colours[user_colors['color_1']][user_colors['color_2']]))

# Stop

color_mixer()

# 6. Change for a Dollar Game

# Design a change-counting game that gets the user to enter the number of coins required to make exactly one dollar. The program should ask the user to enter the number of pennies, nickels, dimes, and quarters. If the total value of the coins entered is equal to one dollar, the program should congratulate the user for winning the game. Otherwise, the program should display a message indicating whether the amount entered was more than or less than one dollar.

# def dollar_game():


# 7. Book Club Points

# Serendipity Booksellers has a book club that awards points to its customers based on the number of books purchased each month. The points are awarded as follows:
# ```
# If a customer purchases 0 books, he or she earns 0 points.

# If a customer purchases 1 book, he or she earns 5 points.

# If a customer purchases 2 books, he or she earns 15 points.

# If a customer purchases 3 books, he or she earns 30 points.

# If a customer purchases 4 or more books, he or she earns 60 points.
# ```

# Design a program that asks the user to enter the number of books that he or she has purchased this month and displays the number of points awarded.

# Module main()
def book_points_earned():
#     Declare int booksPurchased

#     getBooksPurchased(booksPurchased)
    books_purchased = int(input("Please enter the number of books you purchased this month: "))
#     If booksPurchased < 0 Then  // Check if a negative number was entered
    if books_purchased < 0:
#         Set booksPurchased = 0  // Set negative number to avoid default case
        books_purchased = 0
#     End If
#     Select booksPurchased
#         Case 0:
    if books_purchased == 0:
#             Display "0 Points earned for this month."
        print("0 Points earned for this month.")
#         Case 1:
    elif books_purchased == 1:
#             Display "5 Points earned for this month."
        print("5 Points earned for this month.")
#         Case 2:
    elif books_purchased == 2:
#             Display "15 Points earned for this month."
        print("15 Points earned for this month.")
#         Case 3:
    elif books_purchased == 3:
#             Display "30 Points earned for this month."
        print("30 Points earned for this month.")
#         Default:
    elif books_purchased >= 4:
#             Display "60 Points earned for this month."
        print("60 Points earned for this month.")
#     End Select
    else:
        print("Error: You shouldn't see this!")
# Stop

# Module getBooksPurchased(int ref booksPurchased)
#     Display "Please enter the number of books you purchased this month: "
#     Input booksPurchased
# return

# book_points_earned()

# 8. Software Sales

# A software company sells a package that retails for $99. Quantity discounts are given according to the following table:

# ![image](https://user-images.githubusercontent.com/47218880/67404439-04aff880-f579-11e9-8496-6a778d4ce7d1.png)

# Design a program that asks the user to enter the number of packages purchased. The program should then display the amount of the discount (if any) and the total amount of the purchase after the discount.



# 9. Shipping Charges

# The Fast Freight Shipping Company charges the following rates:
# ![image](https://user-images.githubusercontent.com/47218880/67404533-26a97b00-f579-11e9-8944-5cfaa2dc2729.png)
# Design a program that asks the user to enter the weight of a package and then displays the shipping charges.

# 10. Body Mass Index Program Enhancement
# In programming Exercise #6 in Chapter 3 you were asked to write a program that calculates a person’s body mass index (BMI). Recall from that exercise that the BMI is often usedto determine whether a person is overweight or underweight for their height. A person’sBMI is calculated with the formula

# BMI = weight * 703/(height**2)

# where weight is measured in pounds and height is measured in inches. Enhance the program so it displays a message indicating whether the person has optimal weight, isunderweight, or is overweight. A person’s weight is considered to be optimal if his orher BMI is between 18.5 and 25. If the BMI is less than 18.5, the person is consideredto be underweight. If the BMI value is greater than 25, the person is considered to beoverweight.



# 11. Time Calculator

# Design a program that asks the user to enter a number of seconds, and works as follows:

# * There are 60 seconds in a minute. If the number of seconds entered by the user is greater than or equal to 60, the program should display the number of minutes in that many seconds.

# * There are 3,600 seconds in an hour. If the number of seconds entered by the user is greater than or equal to 3,600, the program should display the number of hours in that many seconds.

# * There are 86,400 seconds in a day. If the number of seconds entered by the user is greater than or equal to 86,400, the program should display the number of days in that many seconds.

# Module main
def time_calc():
#     Declare Integer secondsEntry, secondsCalc, minutesCalc, hoursCalc, daysCalc
    time_dict = {'seconds': 0, 'minutes': 0, 'hours': 0, 'days': 0}
#     call getSeconds()
    seconds_entry = int(input("Enter the number of whole seconds you wish to convert: "))
#     set secondsCalc = secondsEntry // copy user input into another variable to work with, preserves original input
    time_dict['seconds'] = seconds_entry
#     While secondsCalc > 60 // loop until the secondsCalc is less then 1 minute
    while time_dict['seconds'] > 60:
#         If secondsCalc > 86400 Then // check if any days are able to be pulled out of seconds
        if time_dict['seconds'] > 86400:
#             set daysCalc = call calcDays(secondsCalc)
            time_dict['days'] = time_dict['seconds'] // 86400
            # set time_dict seconds to the remainder
            time_dict['seconds'] = time_dict['seconds'] % 86400
#         Else If secondsCalc > 3600 Then // check if any hours are able to be pulled out of seconds
        elif time_dict['seconds'] > 3600:
#             set hoursCalc = call calcHours(secondsCalc)
            time_dict['hours'] = time_dict['seconds'] // 3600
            # set time_dict seconds to the remainder
            time_dict['seconds'] = time_dict['seconds'] % 3600
#         Else If secondsCalc > 60 Then // check if any minutes are able to be pulled out of seconds
        elif time_dict['seconds'] > 60:
#             set minutesCalc = call calcMinutes(secondCalc)
            time_dict['minutes'] = time_dict['seconds'] // 60
            # set time_dict seconds to the remainder
            time_dict['seconds'] = time_dict['seconds'] % 60
#         Else:
        else:
#             Display "Something went wrong, You shouldn't be seeing this message! \n\nWhile loop failed to terminate"
            print("Error: loop run/failed to terminate at the expected point")
            break
#             break
#         End If

#     Display secondsEntry, "is equivalent to ", daysCalc, " days ", hoursCalc, " hours ", minutesCalc, " minutes and ", secondsCalc, " seconds."
    print("{} seconds is equivalent to {} days, {} hours, {} minutes, and {} seconds.".format(seconds_entry, time_dict['days'], time_dict['hours'], time_dict['minutes'], time_dict['seconds']))
# End Module

# time_calc()