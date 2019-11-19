# #1. Kilometer Converter

# Design a modular program that asks the user to enter a distance in kilometers, and then converts that distance to miles. The conversion formula is as follows:

# ![image](https://user-images.githubusercontent.com/47218880/67329523-99b2e300-f4e0-11e9-8a30-3f31fbd76ae1.png)

def kilometer_convert():
    # call get_kilometers and set the return to the kilometers variable
    kilometers = get_kilometers()
    # call kilometers2miles with the kilometers varible and set the result to miles
    miles = kilometers2miles(kilometers)
    # Display the miles return from the kilometers conversion calculation
    print(f"{kilometers}km converts to {miles:.2f}mi")

def get_kilometers():
    # Prompt the user for kilometers, convert it to a float, and return it
    return float(input('Enter the distance in kilometers: '))

def kilometers2miles(p_kilometers):
    # Takes the kilometers parameter and returns the product of kilometers * 0.6214
    return p_kilometers * 0.6214

# kilometer_convert()
# print('---------------------')

# #3. How Much Insurance?

# Many financial experts advise that property owners should insure their homes or buildings for at least 80 percent of the amount it would cost to replace the structure. Design a modular program that asks the user to enter the replacement cost of a building and then displays the minimum amount of insurance he or she should buy for the property.

def insurance_calc():
    # call get_building_replace_cost and assign the returned value to a variable
    bldg_cost = get_building_replace_cost()
    # call get_80_percent with the bldg cost variable and assign the returned value to a variable
    min_insurance = get_80_percent(bldg_cost)
    # Display the minimal amount of insurance message
    print("You should get insurance that covers at least ${:.2f}".format(min_insurance))

def get_building_replace_cost():
    # Prompt the user for the replacement cost of a building and return the float converted value
    return float(input("What is the replacement cost of the building?: "))

def get_80_percent(p_amount):
    # Take the p_amount parameter and returns the product of the amount * 0.8 (80% of the amount)
    return p_amount * 0.8

# insurance_calc()
# print('---------------------')

# #4. Automobile Costs

# Design a modular program that asks the user to enter the monthly costs for the following expenses incurred from operating his or her automobile: loan payment, insurance, gas, oil, tires, and maintenance. The program should then display the total monthly cost of these expenses, and the total annual cost of these expenses.

def automobile_cost():
    auto_costs = {'loan': 0, 'insurance': 0, 'gas': 0, 'oil': 0, 'tires': 0, 'maintenance': 0}
    for key in auto_costs.keys():
        auto_costs[key] = get_monthly_cost(key)

    monthly_cost = sum_dict_values(auto_costs)
    annual_cost = monthly_cost * 12
    print("Monthly cost of vehicle: ${:.2f}".format(monthly_cost))
    print("Annual cost of vehicle: ${:.2f}".format(annual_cost))

def get_monthly_cost(p_bill):
    return float(input(f'Enter the monthly {p_bill} payment: '))

def sum_dict_values(p_dict):
    return sum(p_dict.values())

# automobile_cost()
# print('---------------------')

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

# property_tax()
# print('---------------------')

# # 6. Body Mass Index
# # Write a program that calculates and displays a person’s body mass index (BMI). TheBMI is often used to determine whether a person is overweight or underweight for his or her height. A person’s BMI is calculated with the following formula

# # BMI = weight * 703/(height**2)

# # where weight is measured in pounds and height is measured in inches.

def get_BMI():
    height = get_height_inches()
    weight = get_weight_pounds()
    body_mass_index = calc_BMI(height, weight)
    print(f"A person of {height:.1f}in. and weighs {weight:.1f}lbs has a BMI of {body_mass_index:.2f}")

def get_height_inches():
    return float(input('Please enter the height in inches: '))

def get_weight_pounds():
    return float(input('Please enter the weight in pounds: '))

def calc_BMI(p_height, p_weight):
    return p_weight * (703 / (p_height ** 2))

# get_BMI()
# print('---------------------')

# 7. Calories from Fat and Carbohydrates
# A nutritionist who works for a fitness club helps members by evaluating their diets. As part of her evaluation, she asks members for the number of fat grams and carbohydrate grams that they consumed in a day. Then, she calculates the number of calories that result from the fat, using the following formula:
#     calories from fat = fat grams * 9
# Next, she calculates the number of calories that result from the carbohydrates, using the following formula:
#     calories from carbs = carb grams * 4
# The nutritionist asks you to write a program that will make these calculations.

# Module fatGramCalc
def calories_fat_carbs():
# 	Declare Integer fatGrams, calories
# 	Declare Real percentCalsFromFat
    calories = {'fat grams': 0, 'carb grams': 0}

# 	Display "Please enter the amount of grams of fat: "
# 	Input fatGrams
    for key in calories.keys():
        calories[key] = get_grams(key)

    calories['calsFat'] = calc_cals_fat(calories['fat grams'])
    calories['calsCarbs'] = calc_cals_carbs(calories['carb grams'])
    calories_from_fat_carbs = calories['calsFat'] + calories['calsCarbs']

    print("You consumed {} calories from {} grams of fat and {} grams of carbohydrates today.".format(calories_from_fat_carbs, calories['fat grams'], calories['carb grams']))

def get_grams(p_nutrient):
    return float(input(f"Enter the number of {p_nutrient} eaten today: "))

def calc_cals_fat(p_fatGrams):
    return p_fatGrams * 9

def calc_cals_carbs(p_carbGrams):
    return p_carbGrams * 4

# calories_fat_carbs()
# print('---------------------')

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

from random import randint

# Module main
def stadium_seating():
# 	Declare real revenue, sectionAProfits, sectionBProfits, sectionCProfits
# 	Constant Integer MAX_SEATS_A = 300
# 	Constant Integer MAX_SEATS_B = 500
# 	Constant Integer MAX_SEATS_C = 200
    tiers = {
        'A': {'tier': 'A', 'price': 15, 'MAX': 300, 'sold': 0},
        'B': {'tier': 'B', 'price': 12, 'MAX': 500, 'sold': 0},
        'C': {'tier': 'C', 'price': 9, 'MAX': 200, 'sold': 0}
        }
    # sales = {'A': 0, 'B': 0, 'C': 0}
# 	Set sectionAProfits = getTicketsSales(20, MAX_SEATS_A)
# 	Set sectionBProfits = getTicketsSales(15, MAX_SEATS_B)
# 	Set sectionCProfits = getTicketsSales(10, MAX_SEATS_C)
# 	Set revenue = sectionAProfits + sectionBProfits + sectionCProfits
    for tier in tiers.keys():
        tiers[tier]['sold'] = get_ticket_sales(tiers[tier])
        # sales[tier] = get_sales(tiers[tier])
    sales = {t : tiers[t]['price'] * tiers[t]['sold'] for t in tiers.keys()}
    # print(sales)
    total_sales = sum_dict_values(sales)

    print("Total Sales from all tiers: ${:.2f}".format(total_sales))
# 	Display "$", revenue
# End Module

# Function Real getTicketsSales(Real price, Integer maxSeats)
def get_ticket_sales(p_tiers_dict):
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
    # seats_sold = int(input("Enter the number of seat sold for section {}: ".format(p_tiers_dict['tier'])))

# 	While ticketsSold < 0 OR tiscketsSold > maxSeats
    # while seats_sold < 0 or seats_sold > p_tiers_dict['MAX']:
# 		Display "Ticket sales for section ", sectionID," cannot be negative or exceed the number of seats in the section (", maxSeats, ")"
        # print('Invalid input:\n\
            # seats sold for section {} cannot be less than 0\n \
            # or greater than {}.'.format(p_tiers_dict['tier'], p_tiers_dict['MAX']))
# 		Display "Enter number of seats sold for ", sectionID, ": "
        # seats_sold = int(input("Enter the number of seat sold for section {}: ".format(p_tiers_dict['tier'])))
# 		Input ticketsSold
# 	End While
    # return seats_sold
    return randint(1, p_tiers_dict['MAX'])

# 	Return price * ticketsSold
def get_sales(p_tier_dict):
    return float(p_tier_dict['price'] * p_tier_dict['sold'])
# End Function

stadium_seating()
# print('---------------------')

# #9. Paint Job Estimator

# A painting company has determined that for every 115 square feet of wall space, one gallon of paint and eight hours of labor will be required. The company charges $20.00 per hour for labor. Design a modular program that asks the user to enter the square feet of wall space to be painted and the price of the paint per gallon. The program should display the following data:
# ```
# The number of gallons of paint required

# The hours of labor required

# The cost of the paint

# The labor charges

# The total cost of the paint job
# ```

def paint_job_estimator():
    paint_job_quote = {'requested': 0, 'MAX_SQFT_PER_DAY': 115, 'HOURLY_COST': 20.00, 'GALLONS_PER_DAY': 1, 'LABOR_PER_DAY': 8,
    'gallons_req': 0, 'labor_hours': 0, 'labor_cost': 0.0, 'days_req': 0, 'paint_cost': 0.0, 'cost_per_gallon': 0.0, 'quote': 0.0}
    
    paint_job_quote['requested'] = get_job_request()
    paint_job_quote['cost_per_gallon'] = get_paint_cost()
    paint_job_quote['days_req'] = paint_job_quote['requested'] / paint_job_quote['MAX_SQFT_PER_DAY']
    paint_job_quote['gallons_req'] = calc_job_quote(paint_job_quote['days_req'], paint_job_quote['GALLONS_PER_DAY'])
    paint_job_quote['labor_hours'] = calc_job_quote(paint_job_quote['days_req'], paint_job_quote['LABOR_PER_DAY'])
    paint_job_quote['labor_cost'] = calc_job_quote(paint_job_quote['labor_hours'], paint_job_quote['HOURLY_COST'])
    paint_job_quote['paint_cost'] = calc_job_quote(paint_job_quote['gallons_req'], paint_job_quote['cost_per_gallon'])
    paint_job_quote['quote'] = paint_job_quote['paint_cost'] + paint_job_quote['labor_cost']

    print_quote(paint_job_quote)

def get_job_request():
    return int(input('Enter the total area, square footage, to be painted: '))

def get_paint_cost():
    return float(input("Enter the cost of a gallon of the requested paint: "))

def calc_job_quote(p_job, p_CONSTANT):
    return p_job * p_CONSTANT

def print_quote(p_quote_dict):
    print('\nGallons of paint required: {:.2f} gallons'.format(p_quote_dict['gallons_req']))
    print('Hours of Labor estimated:  {:.1f} hours'.format(p_quote_dict['labor_hours']))
    print('\nCost of paint:            ${:.2f}'.format(p_quote_dict['paint_cost']))
    print('Labor Cost:               ${:.2f}'.format(p_quote_dict['labor_cost']))
    print('Total Cost for the job:   ${:.2f}'.format(p_quote_dict['quote']))

# paint_job_estimator()
# print('---------------------')

# #10. Monthly Sales Tax

# A retail company must file a monthly sales tax report listing the total sales for the month, and the amount of state and county sales tax collected. The state sales tax rate is 4 percent and the county sales tax rate is 2 percent. Design a modular program that asks the user to enter the total sales for the month. From this figure, the application should calculate and display the following:
# ```
# The amount of county sales tax

# The amount of state sales tax

# The total sales tax (county plus state)

# In the pseudocode, represent the county tax rate (0.02) and the state tax rate (0.04) as named constants.
# ```

def monthly_sales_tax():
    STATE_SALES_TAX_RATE = 0.04
    COUNTY_SALES_TAX_RATE = 0.02

    monthly_sales = get_monthly_sales()
    state_sales_tax = calc_tax(monthly_sales, STATE_SALES_TAX_RATE)
    county_sales_tax = calc_tax(monthly_sales, COUNTY_SALES_TAX_RATE)
    total_sales_tax = state_sales_tax + county_sales_tax

    print(f'\nCounty Sales Tax:   ${county_sales_tax:.2f}')
    print(f'State Sales Tax:    ${state_sales_tax:.2f}')
    
    print(f'\nTotal Sales Tax:    ${total_sales_tax:.2f}')

def get_monthly_sales():
    return float(input('Enter Monthly Sales: $'))

def calc_tax(p_sales, p_RATE):
    return p_sales * p_RATE

# monthly_sales_tax()