'''
5. Property Tax
    A county collects property taxes on the assessment value of property, which is 60 percent
    of the property’s actual value. If an acre of land is valued at $10,000, its assessment value
    is $6,000. The property tax is then $0.64 for each $100 of the assessment value. The tax
    for the acre assessed at $6,000 will be $38.40. Write a GUI program that displays the
    assessment value and property tax when a user enters the actual value of a property.
'''

import tkinter as tk

def main():
    # instantiate the window
    window = tk.Tk()
    
    # Set the window title and geometry (as desired)
    window.title('Property Tax Calculator')
    # window.geometry('400x400')

    # define the property tax calculation function
    def calc_property_tax():
        # get the entered property value
        value_property = prop_var.get()
        # calculate the assessed value to be 60% of the property value
        value_assessed = value_property * 0.6
        # calulate the property tax to be assessed value/100 * 0.64 ($0.64 per $100 of the assessed value)
        tax_property = (value_assessed/100) * 0.64
        # build the return labels
        label_assessed = tk.Label(text=f'${value_assessed:,.2f}', justify='center')
        label_assessed.grid(row=1, column=1, padx=5, pady=5)
        label_tax = tk.Label(text=f'${tax_property:,.2f}', justify='center')
        label_tax.grid(row=1, column=2, padx=5, pady=5)

    # Create the Label headers
    label_head_property_val = tk.Label(text='Actual Property Value:')
    label_head_property_val.grid(row=0, column=0, padx=5, pady=15)
    label_head_assessed_val = tk.Label(text='Assessed Property Value:')
    label_head_assessed_val.grid(row=0, column=1, padx=5, pady=15)
    label_head_property_tax = tk.Label(text='Property Tax:')
    label_head_property_tax.grid(row=0, column=2, padx=5, pady=15)

    # create the property value variable and entry fields
    prop_var = tk.IntVar()
    entry_property_val = tk.Entry(textvariable=prop_var, justify='center')
    entry_property_val.grid(row=1, column=0, padx=5, pady=5)

    # create the button to call the calc_property_tax function when clicked
    button_calc = tk.Button(text='Calculate Propery Tax', command=calc_property_tax)
    button_calc.grid(row=2, column=1, pady=15)

    # call the window mainloop
    window.mainloop()
# Call the main function
main()