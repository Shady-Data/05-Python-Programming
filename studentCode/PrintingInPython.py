#  1. Write a program that displays the following information:
# 	• Your name
# 	• Your address, with city, state, and ZIP
# 	• Your telephone number
# 	• Your MOS

def personal_info():
    name = "Robert Chunn"
    address_street = "1333 wouldn't you like to know"
    address_city = "Somethingorother City"
    address_state = "Texas"
    address_ZIP = "78XXX"
    phone = "(405) 820-3233"
    MOS = "1B4X1"

    print("Name: %s"% name)
    print("Address: {} \n {:>29}, {} {}".format(address_street, address_city, address_state, address_ZIP))
    print(f"Phone: {phone}")
    print('AFSC: %s'% MOS)

personal_info()
print("\n")

# 2.  A company has determined that its annual profit is typically 23 percent of total sales. Write
# a program that asks the user to enter the projected amount of total sales, and then displays
# the profit that will be made from that amount.

def annual_profit_calc():
    total_sales = float(input("Enter the projected total sales for the year: "))
    projected_profit = total_sales * 0.23
    print("The current projected profit is ${:.2f}".format(projected_profit))

annual_profit_calc()
print("\n")

# 3.  One acre of land is equivalent to 43,560 square feet. Write a program that asks the user to
# enter the total square feet in a tract of land and calculates the number of acres in the tract.

def acre_calc():
    land_square_feet = int(input("Enter the square footage of the land: "))
    acres = land_square_feet / 43560
    print("{} sqft is {:.2f} acres".format(land_square_feet, acres))

acre_calc()
print("\n")

#  4. A customer in a store is purchasing five items. Write a program that asks for the price of
# each item, and then displays the subtotal of the sale, the amount of sales tax, and the total.
# Assume the sales tax is 6 percent.

def total_cart(cartsize):
    item = 1
    subtotal = 0
    while item < cartsize + 1:
        subtotal += float(input("Please enter item " + str(item) + "'s cost: $"))
        item += 1
    print("\nSubtotal:      $%.2f" % subtotal)
    print("6% Sales Tax:  ${:.2f}".format(subtotal*0.06))
    total = subtotal + (subtotal * 0.06)
    print(f"Total:         ${total:.2f}")

total_cart(5)
print("\n")

# 5.  Assuming there are no accidents or delays, the distance that a car travels down the interstate can be calculated with the following formula:
# Distance = Speed * Time

#  A car is traveling at 60 miles per hour. Write a program that displays the following:
# 	• The distance the car will travel in 5 hours
# 	• The distance the car will travel in 8 hours
# 	• The distance the car will travel in 12 hours

def distance_travel():
    speed = 60
    distance = {}
    hours = [5, 8, 12]
    for hour in hours:
        distance[hour] = speed * hour
    for h, dist in distance.items():
        print(f'The distance the car will travel in {h:2d} hours is {dist:d}')

distance_travel()
print("\n")

# 6.  Write a program that will ask the user to enter the amount of a purchase. The program
# should then compute the state and county sales tax. Assume the state sales tax is 4 percent
# and the county sales tax is 2 percent. The program should display the amount of the purchase, the state sales tax, the county sales tax, the total sales tax, and the total of the sale
# (which is the sum of the amount of purchase plus the total sales tax).

def tax_calc():
    purchase_cost = float(input("Enter the amount of the large purchase: "))
    state_sales_tax = purchase_cost * 0.04
    county_sales_tax = purchase_cost * 0.02
    tax_total = state_sales_tax + county_sales_tax
    sales_total = purchase_cost + tax_total
    print(f"Purchase:      ${purchase_cost:.2f}")
    print("--------------------------------")
    print(f"4% State Tax:  ${state_sales_tax:.2f}")
    print(f"2% County Tax: ${county_sales_tax:.2f}")
    print(f"Total Tax:     ${tax_total:.2f}")
    print("--------------------------------")
    print(f"Total Sales:   ${sales_total:.2f}")

tax_calc()
print("\n")

# 7.  A car’s miles-per-gallon (MPG) can be calculated with the following formula:
#  MPG = Miles driven / Gallons of gas used
# Write a program that asks the user for the number of miles driven and the gallons of gas
# used. It should calculate the car’s MPG and display the result.

def mpg_calc():
    miles_driven = int(input("Miles driven: "))
    gas_used = int(input("Gallons of gas used: "))
    mpg = miles_driven // gas_used
    print("Miles per gallon (MPG) is %2d" % mpg)

mpg_calc()
print('\n')

# 8.  Write a program that calculates the total amount of a meal purchased at a restaurant. The
# program should ask the user to enter the charge for the food, and then calculate the amount
# of a 15 percent tip and 7 percent sales tax. Display each of these amounts and the total.

def restaurant_calc():
    meal_cost = float(input("What is the cost of the meal? "))
    tip_amount = meal_cost * 0.15
    meal_sales_tax = meal_cost * 0.07
    total_meal_cost = meal_cost + meal_sales_tax + tip_amount
    print('----------------------')
    print("Subtotal:   $%.2f" % meal_cost)
    print(f"15% Tip:    ${tip_amount:.2f}")
    print(f"Sales Tax:  ${meal_sales_tax:.2f}")
    print('----------------------')
    print(f"Total:      ${total_meal_cost:.2f}")
    

restaurant_calc()
print('\n')

# 9. Write a program that converts Celsius temperatures to Fahrenheit temperatures. The formula is as follows:

#  F = (9/5)C + 32

#  The program should ask the user to enter a temperature in Celsius, and then display the
# temperature converted to Fahrenheit.

def celsius_to_fahrenheit():
    celsius = int(input("Enter the temperature in Celsius: "))
    fahrenheit = int(((9/5) * celsius) + 32)
    print("%d°C is %d°F" % (celsius, fahrenheit))

celsius_to_fahrenheit()
print('\n')

# 10.  Last month Joe purchased some stock in Acme Software, Inc. Here are the details of the
# purchase:
# • The number of shares that Joe purchased was 1,000.
# • When Joe purchased the stock, he paid $32.87 per share.
# • Joe paid his stockbroker a commission that amounted to 2 percent of the amount he paid
# for the stock.
# Two weeks later Joe sold the stock. Here are the details of the sale:
# • The number of shares that Joe sold was 1,000.
# • He sold the stock for $33.92 per share.
# • He paid his stockbroker another commission that amounted to 2 percent of the amount
# he received for the stock.

#  Write a program that displays the following information:
# • The amount of money Joe paid for the stock.
# • The amount of commission Joe paid his broker when he bought the stock.
# • The amount that Joe sold the stock for.
# • The amount of commission Joe paid his broker when he sold the stock.
# • Display the amount of money that Joe had left when he sold the stock and paid his
# broker (both times). If this amount is positive, then Joe made a profit. If the amount is
# negative, then Joe lost money

def stock_calc():
    stocks_purchase = {'amount': 1000, 'costper': 32.87}
    stocks_purchase['costforamount'] = stocks_purchase['amount'] * stocks_purchase['costper']
    stocks_purchase['commission'] = stocks_purchase['costforamount'] * 0.02
    stocks_purchase['total'] = stocks_purchase['costforamount'] + stocks_purchase['commission']
    stocks_sold = {'amount': 1000, 'costper': 33.92}
    stocks_sold['costforamount'] = stocks_sold['amount'] * stocks_sold['costper']
    stocks_sold['commission'] = stocks_sold['costforamount'] * 0.02
    stocks_sold['total'] = stocks_sold['costforamount'] - stocks_sold['commission']
    headers = ['Purchase', 'Sell']
    print("                   |{:^12} |{:^12}".format(headers[0], headers[1]))
    print("Amount Paid/Earned |${:>12.2f}|${:>12.2f}".format(stocks_purchase['costforamount'], stocks_sold['costforamount']))
    print("Commission Paid    |${:>12.2f}|${:>12.2f}".format(stocks_purchase['commission'], stocks_sold['commission']))
    stocks_profit = stocks_sold['total'] - stocks_purchase['total']
    if stocks_profit < 0:
        print("\nJoe lost $%.2f from his stocks adventure." % abs(stocks_profit))
    elif stocks_profit > 0:
        print("\nJoe made $%.2f from his stocks adventure." % stocks_profit)
    else:
        print("\nJoe, somehow, broke even from his stocks adventure.")
    
stock_calc()
    