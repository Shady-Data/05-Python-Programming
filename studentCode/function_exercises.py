# #1. Kilometer Converter

# Design a modular program that asks the user to enter a distance in kilometers, and then converts that distance to miles. The conversion formula is as follows:

# ![image](https://user-images.githubusercontent.com/47218880/67329523-99b2e300-f4e0-11e9-8a30-3f31fbd76ae1.png)

def kilometer_convert():
    kilometers = get_kilometers()
    miles = kilometers2miles(kilometers)
    print(f"{kilometers} converts to {miles:.2f}")

def get_kilometers():
    return float(input('Enter the distance in kilometers: '))

def kilometers2miles(p_kilometers):
    return p_kilometers * 0.6214

kilometer_convert()
print('---------------------')

# #3. How Much Insurance?

# Many financial experts advise that property owners should insure their homes or buildings for at least 80 percent of the amount it would cost to replace the structure. Design a modular program that asks the user to enter the replacement cost of a building and then displays the minimum amount of insurance he or she should buy for the property.

def insurance_calc():
    bldg_cost = get_building_replace_cost()
    min_insurance = get_80_percent(bldg_cost)
    print("You should get insurance that covers at least ${:.2f}".format(min_insurance))

def get_building_replace_cost():
    return float(input("What is the replacement cost of the building?: "))

def get_80_percent(p_amount):
    return p_amount * 0.8

insurance_calc()
print('---------------------')

# #4. Automobile Costs

# Design a modular program that asks the user to enter the monthly costs for the following expenses incurred from operating his or her automobile: loan payment, insurance, gas, oil, tires, and maintenance. The program should then display the total monthly cost of these expenses, and the total annual cost of these expenses.

def automobile_cost():
    auto_costs = {'loan': 0, 'insurance': 0, 'gas': 0, 'oil': 0, 'tires': 0, 'maintenance': 0}
    for key in auto_costs:
        auto_costs[key] = get_monthly_cost(key):

    monthly_cost = sum_dict_values(auto_costs)
    annual_cost = monthly_cost * 12
    print("Monthly cost of vehicle: ${:.2f}".format(monthly_cost))
    print("Annual cost of vehicle: ${:.2f}".format(annual_cost))

def get_monthly_cost(p_bill):
    return float(input(f'Enter the monthly {p_bill} payment: '))

def sum_dict_values(p_dict):
    return sum(p_dict.values())

automobile_cost()
print('---------------------')

# #5. Property Tax

# A county collects property taxes on the assessment value of property, which is 60 percent of the property’s actual value. For example, if an acre of land is valued at $10,000, its assessment value is $6,000. The property tax is then 64¢ for each $100 of the assessment value. The tax for the acre assessed at $6,000 will be $38.40. Design a modular program that asks for the actual value of a piece of property and displays the assessment value and property tax

def property_tax():
    property_value = get_property_value()
    assessed_value = calc_assessed_value(property_value)
    tax_property = calc_tax_assessed(assessed_value)
    print("Assessment Value: ${:.2f}".format(assessed_value))
    print("Property Tax: ${:.2f}".format(tax_property))

def get_property_value():
    return float(input('Property Value: $'))

def calc_assessed_value(p_pvalue):
    return p_pvalue * 0.6

def calc_tax_assessed(p_avalue):
    # floor divide the assessed value by 100 and multiply it by 0.64 to get $0.64 per $100 of the assed value
    return (p_avalue // 100) * 0.64

property_tax()
print('---------------------')

# # 6. Body Mass Index Program Enhancement
# # Write a program that calculates and displays a person’s body mass index (BMI). TheBMI is often used to determine whether a person is overweight or underweight for hisor her height. A person’s BMI is calculated with the following formula

# # BMI = weight * 703/(height**2)

# # where weight is measured in pounds and height is measured in inches.


# 7. Calories from Fat and Carbohydrates
# A nutritionist who works for a fitness club helps members by evaluating their diets. As partof her evaluation, she asks members for the number of fat grams and carbohydrate gramsthat they consumed in a day. Then, she calculates the number of calories that result fromthe fat, using the following formula:
#     calories from fat = fat grams * 9
# Next, she calculates the number of calories that result from the carbohydrates, using thefollowing formula:
#     calories from carbs = carb grams * 4
# The nutritionist asks you to write a program that will make these calculations.

# Module fatGramCalc
# 	Declare Integer fatGrams, calories
# 	Declare Real percentCalsFromFat

# 	Do
# 		Display "Please enter the total calories: "
# 		Input calories
# 	While calories < 0

# 	Display "Please enter the amount of grams of fat: "
# 	Input fatGrams
	
# 	While fatGrams < 0 OR fatGrams * 9 > calories
# 		Display "Invalid entry! Amount of grams of fat cannot be negative"
# 		Display "Calculated calories from fat cannot exceed total calories (grams of fat * 9)"
# 		Display "Please enter the amount of grams of fat: "
# 		Input fatGrams
# 	End While

# 	Set percentCalsFromFat = ((fatGrams * 9) / calories) * 100
# 	Display "%", percentCalsFromFat, " calories from fat."
# 	If percentCalsFromFat < 30 Then
# 		Display "Low-Fat"
# 	End If
# End Module

# #8. Stadium Seating

# There are three seating categories at a stadium. For a softball game, Class A seats cost $15, Class B seats cost $12, and Class C seats cost $9. Design a modular program that asks how many tickets for each class of seats were sold, and then displays the amount of income generated from ticket sales.

# Module main
# 	Declare real revenue, sectionAProfits, sectionBProfits, sectionCProfits
# 	Constant Integer MAX_SEATS_A = 300
# 	Constant Integer MAX_SEATS_B = 500
# 	Constant Integer MAX_SEATS_C = 200

# 	Set sectionAProfits = getTicketsSales(20, MAX_SEATS_A)
# 	Set sectionBProfits = getTicketsSales(15, MAX_SEATS_B)
# 	Set sectionCProfits = getTicketsSales(10, MAX_SEATS_C)
# 	Set revenue = sectionAProfits + sectionBProfits + sectionCProfits

# 	Display "$", revenue
# End Module

# Function Real getTicketsSales(Real price, Integer maxSeats)
# 	Declare Integer ticketsSold
# 	Declare String sectionID

# 	Select maxSeats
# 		Case 300:
# 			Set sectionID = "A"
# 		Case 500:
# 			Set sectionID = "B"
# 		Case 200:
# 			Set sectionID = "C"
# 	End Select

# 	Display "Enter number of seats sold for ", sectionID, ": "
# 	Input ticketsSold

# 	While ticketsSold < 0 OR tiscketsSold > maxSeats
# 		Display "Ticket sales for section ", sectionID," cannot be negative or exceed the number of seats in the section (", maxSeats, ")"
# 		Display "Enter number of seats sold for ", sectionID, ": "
# 		Input ticketsSold
# 	End While

# 	Return price * ticketsSold
# End Function


# #9. Paint Job Estimator

# A painting company has determined that for every 115 square feet of wall space, one gallon of paint and eight hours of labor will be required. The company charges $20.00 per hour for labor. Design a modular program that asks the user to enter the square feet of wall space to be painted and the price of the paint per gallon. The program should display the following data:
# ```
# The number of gallons of paint required

# The hours of labor required

# The cost of the paint

# The labor charges

# The total cost of the paint job
# ```
# #10. Monthly Sales Tax

# A retail company must file a monthly sales tax report listing the total sales for the month, and the amount of state and county sales tax collected. The state sales tax rate is 4 percent and the county sales tax rate is 2 percent. Design a modular program that asks the user to enter the total sales for the month. From this figure, the application should calculate and display the following:
# ```
# The amount of county sales tax

# The amount of state sales tax

# The total sales tax (county plus state)

# In the pseudocode, represent the county tax rate (0.02) and the state tax rate (0.04) as named constants.
# ```

