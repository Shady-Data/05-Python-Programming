'''
3. Miles Per Gallon Calculator
    Write a GUI program that calculates a car’s gas mileage. The program’s window should
    have Entry widgets that let the user enter the number of gallons of gas the car holds, and
    the number of miles it can be driven on a full tank. When a Calculate MPG button is
    clicked, the program should display the number of miles that the car may be driven per gallon of 
    gas. Use the following formula to calculate miles-per-gallon:
​
        MPG = miles/gallons
'''

import tkinter as tk

def main():
    # instantiate the window
    window = tk.Tk()

    # Set the title and geometry of the window
    window.title('Miles Per Gallon Calculator')
    window.geometry('400x400')

    # define the calc_miles_per_gallon function
    def calc_miles_per_gallon():
        # get the miles and gallons from user entry
        miles = miles_var.get()
        gallons = gallons_var.get()
        # calculate mpg = miles/gallons
        mpg = miles/gallons
        # Create a label and display the result
        mpg_label = tk.Label(master=window, text=f'{mpg:.2f} miles per gallon')
        mpg_label.grid(row=3, column=0, columnspan=3, sticky='nsew')

    # Create headers for the window
    label_miles = tk.Label(text='# of Miles')
    label_miles.grid(row=0, column=0, padx=10, pady=20)
    label_gallons = tk.Label(text='# of Gallons used')
    label_gallons.grid(row=0, column=2, padx=10, pady=20)

    # establish variable to store the expected input
    miles_var = tk.IntVar()
    gallons_var = tk.IntVar()
    # Create the entry boxes
    miles_entry = tk.Entry(textvariable=miles_var, justify='center')
    miles_entry.grid(row=1, column=0, padx=10)
    gallons_entry = tk.Entry(textvariable=gallons_var, justify='center')
    gallons_entry.grid(row=1, column=2, padx=10)

    # Create a button to call the calulation function
    button = tk.Button(text='Calculate MPG', command=calc_miles_per_gallon)
    button.grid(row=2, column=0, columnspan=3, padx=5, pady=10, sticky='nsew')

    # call the mainloop function
    window.mainloop()

# call the main function
main()