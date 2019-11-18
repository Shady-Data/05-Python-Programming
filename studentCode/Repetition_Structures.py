# 1. Bug Collector
# A bug collector collects bugs every day for seven days. Write a program that keeps a running total of the number of bugs collected during the seven days. The loop should ask for the number of bugs collected for each day, and when the loop is finished, the program should display the total number of bugs collected.

def bug_collector():
    '''
    Requests user to input the number of bugs they've collected over a 7-day period
    and prints the accumalated total of bugs collected.
    '''
    # initialize the accumalator
    bugs_collected = 0
    # iterate over 7 days
    for day in range(1, 8):
        # Prompt the user for input and add interger input to the accumaltor
        bugs_collected += int(input(f'Enter the number of bugs collected for day {day}: '))
    # print the accumalated total after all loop iterations complete
    print(f'Total bugs collected this week: {bugs_collected}')

# bug_collector()
# print('-------------------------------------')

# 2. Calories Burned
# Running on a particular treadmill you burn 3.9 calories per minute. Write a program that uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.

def draw_calories_burned():
    '''
    Draws a table of calories burned on a particular treadmill over 10, 15, 20, 25, and 30 minutes
    '''
    # set the constant calories burned per minute to 3.9
    CALS_BURNED_PER_MIN = 3.9
    # Populate a list with the numbers requested for the table
    minutes = [10, 15, 20, 25, 30]
    cals_burned = [m * CALS_BURNED_PER_MIN for m in minutes]
    # print the table headers
    print('-------------------------------------')
    print('|     Minutes     |   Cals Burned   |')
    print('-------------------------------------')
    # iterate over the items in the list
    # for minute in minutes:
        # calculate the amount burned for the minutes from the list
        # cals_burned = minute * CALS_BURNED_PER_MIN
        # print the table contents of minute value from list iteration and the calculated amount burned
    for minute, cals in zip(minutes, cals_burned):
        print(f'|{minute:^17}|{cals:^17}|')
    print('-------------------------------------')

# draw_calories_burned()

# 3. Budget Analysis
# Write a program that asks the user to enter the amount that he or she has budgeted for a month. A loop should then prompt the user to enter each of his or her expenses for the month and keep a running total. When the loop finishes, the program should display the amount that the user is over or under budget.

def budget_analysis():
    '''
    Requests a budget amount then accumalates expenses incurred for the month
    and finally reports back if accumalted expenses is over or under the budget amount
    '''
    # Prompt the user for monthly budget amount
    budget = float(input('Enter your budget for the month: '))
    # initialize the expense accumalator
    total_expenses = 0.0
    # initialize the sentinel value with a non-zero value
    expense = 1.0

    # Continue prompting for input until the user enters 0
    while expense != 0:
        # Prompt user for expense entry
        expense = float(input('\nEnter an expense for the month\nEnter 0 to finish entering expenses: '))
        # add expense to the accumalator
        total_expenses += expense
    
    # check if the accumalted expenses is over the entered budget
    if total_expenses > budget:
        # print the overage statement/amount
        print('User is over budget by {:.2f}'.format(total_expenses - budget))
    else:
        # print the under budget statement/amount
        print('User is under budget by {:.2f}'.format(budget - total_expenses))

# budget_analysis()
# print('-------------------------------------')

# 4. Distance Traveled
# The distance a vehicle travels can be calculated as follows:

#    distance = speed * time

# For example, if a train travels 40 miles per hour for three hours, the distance traveled is 120 miles. Write a program that asks the user for the speed of a vehicle (in miles per hour) and the number of hours it has traveled. It should then use a loop to display the distance the vehicle has traveled for each hour of that time period.

def distance_traveled():
    '''
    Takes a speed in miles per hour (mph) and a number of hours traveled
    then creates a table of distances traveled (speed * hours) for each hour of travel
    '''
    # Prompt the user to input the rate/speed of travel
    speed = int(input('Enter the travel speed in mph: '))
    # Prompt the user to input the number of hours traveled
    hours_traveled = int(input('Enter the number of hours traveling: '))

    # Print the table headers
    print('----------------------')
    print('|  hours  | distance |')
    print('----------------------')
    # iterate through the range 1 to the number of hours traveled + 1
    # for hour in range(1, hours_traveled + 1):
    hours = [h for h in range(1, hours_traveled + 1)]
        # calculate the distance traveled for the hour/iteration of the loop
        # distance = speed * hour
    distance = lambda h: speed * h
    distances = map(distance, hours)
        # Print the table contents
    for hour, dist in zip(hours, distances):
        print(f'|{hour:^9}|{dist:>7} mi|')
    # print('----------------------')

# distance_traveled()

# 5. Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years. The program should first ask for the number of years. The outer loop will iterate once for each year. The inner loop will iterate twelve times, once for each month. Each iteration of the inner loop will ask the user for the inches of rainfall for that month. After all iterations, the program should display the number of months, the total inches of rainfall, and the average rainfall per month for the entire period.

def average_rainfall():
    '''
    Takes a number of years and requests the amount of rainfall for each month of that year
    then calculates the total rainfall for all months and the average monthly rainfall
    '''
    # Dictionary with the month being a key, and the value is the amount of rainfall for the month
    months = {'January': 0, 'February': 0, 'March': 0, 'April': 0, 'May': 0, 'June': 0, 'July': 0, 'August': 0, 'September': 0, 'October': 0, 'November': 0, 'December': 0}
    # Prompt user for the number of years to be entered
    years = int(input("Enter the number of years for the rainfall study: "))
    # initialize a variable to accumalate the number of months in the study, should equal 12 * years at the end
    accum_months = 0
    # initialize an accumalator to total rainfall
    total_rainfall = 0.0

    # Iterate over a range of 1 to the number of years entered + 1 (used for input)
    for year in range(1, years + 1):
        # Display a year seperator for data entry
        print('---------------')
        # iterate over each month
        for month in months.keys():
            # Prompt user for the amount rainfall of the month and assign the value to the month in the months dictionary
            months[month] = float(input(f'Enter the amount of rainfall, in inches, for {month}, of year {year} of the study: '))
            # increment the month accumalator
            accum_months += 1
        # sum the values entered for each month and add it to total_rainfall
        total_rainfall += sum(months.values())
    # print a seperator to signify the end of user inputs
    print('---------------')

    # calculate average rainfall by dividing the total rainfall by the number of months of data entered
    average_monthly_rainfall = total_rainfall / accum_months
    # Display the number of months in the study
    print(f"\nTotal number of month in the study: {accum_months}")
    # Display the total rainfall
    print(f'Total rainfall:                     {total_rainfall:.2f}in.')
    # Display the average monthly rainfall
    print(f'Average Monthly rainfall:           {average_monthly_rainfall:.2f}in.')

# average_rainfall()
# print('----------------------')

# 6. Celsius to Fahrenheit Table
# Write a program that displays a table of the Celsius temperatures 0 through 20 and their Fahrenheit equivalents. The formula for converting a temperature from Celsius to Fahrenheit is
   
#     F = (9/5)C + 32

# where F is the Fahrenheit temperature and C is the Celsius temperature. Your program must use a loop to display the table.

# Module main
def draw_table_celsius_fahr():
#     Declare Integer celsius
#     Declare Real fahrenheit

#     Display "╔══════════╤════════════╗" // starting line of table
    print("╔══════════╤════════════╗")
#     Display "║ Celsius  | Fahrenheit ║" // column headers
    print("║ Celsius  | Fahrenheit ║")
#     Display "╠══════════╪════════════╣"
    print("╠══════════╪════════════╣")
#     For celsius = 0 to 20 step 1
    # for celsius in range(21):
#         set fahrenheit = (9/5) * celsius + 32
        # fahrenheit = ((9/5) * celsius) + 32
#         If celsius < 10 Then
#             Display "║     ", celsius, "     |    ", fahrenheit, "    ║"
#         Else
#             Display "║     ", celsius, "    |    ", fahrenheit, "    ║"
#         End If
    # Build a list with the fahrenheit converted numbers
    fahrenheit = [((9/5) * x) + 32 for x in range(21)]
    # enumerate the list contaning the fahrenheit values
    for cel, fah in enumerate(fahrenheit):
        # print the index == celcius and the fahhrenheit value
        print(f'║{cel:^10d}|{fah:^12.1f}║')
#         If celsius == 20 Then
        if cel == 20:
#             Display "╚══════════╧════════════╝" // Last line of the table
            print("╚══════════╧════════════╝")
#         Else
        else:
#             Display "╟──────────┼────────────╢" // 
            print("╟──────────┼────────────╢")
#         End If
#     End For
# End Module

# draw_table_celsius_fahr()
# print('----------------------')

# 7. Pennies for Pay
# Write a program that calculates the amount of money a person would earn over a period of time if his or her salary is one penny the first day,
# two pennies the second day, and continues to double each day. The program should ask the user for the number of days.
# Display a table showing what the salary was for each day, and then show the total pay at the end of the period.
# The output should be displayed in a dollar amount, not the number of pennies.

def pennies_for_pay():
    # Prompt user for the number of days
    num_days = int(input('Please enter the number of days to calculate pay for: '))
    # set the starting pay to .01 for one penny
    pay_day = 0.01
    # initialize the total accumalator
    total_pay = 0

    # Display the table headers 
    print("╔═══════╤═══════════════╗")
    print("║  Day  |      Pay      ║")
    print("╠═══════╪═══════════════╣")
    # iterate over a range of 1 to the number of days + 1
    for day in range(1, num_days + 1):
        # print the current day and pay for that day
        print(f'║{day:^7}|${pay_day:>14,.2f}║')
        # Add current day's pay to the total
        total_pay += pay_day
        # calculate the next day's pay
        pay_day *= 2

    # print the last line in the table
    print("╚═══════╧═══════════════╝")
    # print the total pay over the period
    print(f'You will be paid ${total_pay:,.2f} over a period of {num_days} days.')

# call pennies_for_pay
# pennies_for_pay()

# 8. Sum of Numbers
# Write a program with a loop that asks the user to enter a series of positive numbers. The user should enter a negative number to signal the end of the series.
# After all the positive numbers have been entered, the program should display their sum.

from functools import reduce

def sum_of_nums():
    # initialize the total variable
    # total_sum = 0
    numbers = []
    # set a sentinal value for loop
    num_input = 0.01

    print("Enter numbers to sum together.\nEnter a negative number to finish,\n")
    # coninously grab user input until a negative number is entered
    while num_input >= 0:
        # Prompt user for a positive number and convert it to a float
        num_input = input("Enter a positve number: ")
        # if user input is blank or negative
        if num_input == '' or float(num_input) < 0:
            # set the num_input to -1
            num_input = -1
            # break out of the loop
            break
        # else
        else:
            #set num_input to float
            num_input = float(num_input)
            # add the user input to the total accumalator
            # total_sum += num_input
            numbers.append(num_input)

    total_sum = reduce(lambda x, y: x + y, numbers)
    # Display the total of all numbers entered.
    print(f'The sum of all numbers entered is {total_sum:,.2f}.')

# call sum_of_numbers
# sum_of_nums()


# 9. Write a program that uses nested loops to draw this pattern:
# *******
# ******
# *****
# ****
# ***
# **
# *

def pattern_draw_1():
    # Set loops variable to the number (lines to print)|(loops to run)
    loops = 7
    # while loops > 0 Then
    while loops > 0:
        # Set pattern = '' // Clears the pattern variable for the loop
        # pattern = ''
        # For n ( <= unused variable) in range 0 to the number of loops:
        # for n in range(loops):
            # Set pattern = pattern + '*' // builds the pattern to be printed
            # pattern += "*"
        pattern = ''.join('*'*loops)
        # Print the built pattern
        print(pattern)
        # Set loops = loops -1 // Decrement the sentinal value
        loops -= 1

# pattern_draw_1()
# print('-------------------------------------')

# 10. Write a program that uses nested loops to draw this pattern:
# ##
# # #
# #  #
# #   #
# #    #
# #     #

def pattern_draw_2():
    # initialize the an accumalator for spaces inserted in the pattern
    spaces = 0
    # While accumalator < number of repetitions of the pattern
    while spaces < 6:
        # Set pattern = '#' // clears the pattern and starts a new one
        pattern = ''.join('#' + ' ' * spaces + '#')
        # For space ( <= unused variable) in range 0 to accumalated spaces
        # for space in range(spaces):
            # Set pattern = pattern + ' ' // builds the number of empty spaces in the pattern
            # pattern += " "
        # Set pattern = pattern + '#' // adds the remaing char to the pattern for the loop
        # pattern += '#'
        # print the pattern
        print(pattern)
        # Set spaces = spaces + 1
        spaces += 1

# pattern_draw_2()