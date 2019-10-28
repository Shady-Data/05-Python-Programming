# Calculate the cost of an item with the added calculated tax amount.
def taxCalculator():
    # hard coded item price and sales tax cost for the moment
    itemPrice = 12.96
    salesTax = .06
    # calaculate the cost by adding the original price with the product of the original price times the sales tax
    totalItemCost = itemPrice + (itemPrice*salesTax)
    # return the calculated total cost of the item
    return totalItemCost

# call the function and print the results
print("$%.2f"% taxCalculator())

# functional lambda expression that takes 2 arugments to accomplish the same as taxCalculator
funcItemCostCalc = lambda itemCost, calcTax: itemCost+(itemCost*calcTax)

# call the stored lambda function with appropriate cost and salestax
print("$%.2f"% funcItemCostCalc(14.99, 0.06))
